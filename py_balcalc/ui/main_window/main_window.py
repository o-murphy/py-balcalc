# -*- coding: utf-8 -*-
import os
from pathlib import Path

import a7p
from PySide6 import QtWidgets, QtCore, QtGui
from .add_button import AddButton
from .profile_wizard import ProfileWizard
from .footer import FooterWidget
from .profile_tab import ProfileTab
from .profiles_tools import ProfilesTools

from py_balcalc.file import open_files, save_file
from py_balcalc.settings import app_settings, get_user_dir
from py_balcalc.translator import tr
from ...signals_manager import appSignalMgr


class MainWindow(QtWidgets.QMainWindow):
    filesDropped = QtCore.Signal(object)

    def __init__(self, app=None):
        super().__init__()

        self.init_ui()
        self.app = app
        self.translator_custom = QtCore.QTranslator()

        self.__post_init__()

    def __post_init__(self):
        self.add_button.clicked.connect(self.open_file_dialog)
        self.profile_tools.openFile.clicked.connect(self.open_file_dialog)
        self.profile_tools.newProfileButton.clicked.connect(self.open_wizard)
        self.profilesTabs.tabCloseRequested.connect(self.close_tab)

        self.profile_tools.saveAsButton.clicked.connect(self.save_file_as)
        self.profile_tools.saveButton.clicked.connect(self.on_save_button)

        self.filesDropped.connect(lambda file_names: self.open_files(*file_names))

    #     self.setAcceptDrops(True)
    #
    # def dragEnterEvent(self, event) -> None:
    #     if self.profilesTabs.count() > 0:
    #         self.stacked.setCurrentIndex(0)
    #     super(MainWindow, self).dragEnterEvent(event)
    #
    # def dragLeaveEvent(self, event) -> None:
    #     if self.profilesTabs.count() > 0:
    #         self.stacked.setCurrentIndex(1)
    #     super(MainWindow, self).dragLeaveEvent(event)

    def open_wizard(self):

        def on_wizard_accept():
            data = a7p.A7PFile.dumps(dlg.export_a7p())

            file_name = self.save_file_dialog(dlg.create_name())
            if file_name:
                with open(file_name, 'wb') as fp:
                    fp.write(data)
                dlg.accept()
                self.open_files(file_name)

        dlg = ProfileWizard(self)
        dlg.onAccepted.connect(on_wizard_accept)
        dlg.exec()

    def save_file_dialog(self, file_name):
        if not Path(file_name).exists():
            file_name = Path(get_user_dir(), Path(file_name).name).as_posix()
        options = QtWidgets.QFileDialog.Options()
        _file_name, file_format = QtWidgets.QFileDialog.getSaveFileName(
            self,
            caption="Save file",
            dir=file_name,
            filter="ArcherBC2 Profile (*.a7p)",
            options=options
        )
        if _file_name:
            app_settings.setValue("env/user_dir", Path(_file_name).parent)
        return _file_name

    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        file_names, file_format = QtWidgets.QFileDialog.getOpenFileNames(
            self,
            caption="Open files",
            dir=Path(get_user_dir()).as_posix(),
            filter="ArcherBC2 Profile (*.a7p)",
            options=options
        )
        if file_names:
            self.open_files(*file_names)

    def switch_stacked(self):
        count = self.profilesTabs.count()
        self.stacked.setCurrentIndex(count > 0)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        self.filesDropped.emit(files)

    def open_files(self, *file_names):
        profiles = open_files(*file_names)
        for i, (path, payload) in enumerate(profiles):
            profile_tab = ProfileTab(self, payload, path)
            self.profilesTabs.addTab(profile_tab, Path(profile_tab.file_name).name)
        self.switch_stacked()
        self.profilesTabs.setCurrentIndex(self.profilesTabs.count() - 1)

    def save_file_as(self, tab=None):
        if not tab:
            tab: ProfileTab = self.profilesTabs.currentWidget()
        if not tab.validate():
            return
        data = a7p.A7PFile.dumps(tab.export_a7p())
        file_name = self.save_file_dialog(tab.create_name())
        if file_name:
            with open(file_name, 'wb') as fp:
                fp.write(data)
                tab.file_name = file_name
                return file_name

    def on_save_button(self):
        tab: ProfileTab = self.profilesTabs.currentWidget()
        self.save_file(tab, False)

    def save_file(self, tab, discard=True):

        std_btns = QtWidgets.QMessageBox.StandardButton
        buttons = std_btns.Save | std_btns.Cancel
        if discard:
            buttons |= std_btns.Discard

        if not self.is_file_exists(tab.file_name):
            dlg = QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Warning,
                "Warning",
                f"File not saved, are you want to save changes?\n{tab.create_name()}",
                buttons
            )
            result = dlg.exec()
            if result == QtWidgets.QMessageBox.StandardButton.Save.value:
                if not tab.validate():
                    return False
                file_name = self.save_file_as(tab)
                if file_name:
                    tab.file_name = file_name
                    return True
            elif result == QtWidgets.QMessageBox.StandardButton.Discard.value:
                return True
            return False

        else:
            data = self.is_data_updated(tab)
            if data:

                dlg = QtWidgets.QMessageBox(
                    QtWidgets.QMessageBox.Icon.Warning,
                    "Warning",
                    f"File updated, are you want to save changes?\n{tab.file_name}",
                    buttons
                )
                result = dlg.exec()
                if result == QtWidgets.QMessageBox.StandardButton.Save.value:
                    if not tab.validate():
                        return False
                    save_file(tab.file_name, data)
                    return True
                elif result == QtWidgets.QMessageBox.StandardButton.Discard.value:
                    return True
            else:
                return True
        return False

    def close_tab(self, index):
        tab: ProfileTab = self.profilesTabs.widget(index)

        if self.save_file(tab):
            self.profilesTabs.removeTab(index)
            self.switch_stacked()
            return True
        return False

    def is_file_exists(self, file_name):
        return os.path.exists(file_name)

    def is_data_updated(self, tab):

        tab_data = tab.export_a7p()
        try:
            filename, file_data = open_files(tab.file_name)[0]

            # for field_descriptor, field_value in file_data.profile.ListFields():
            #     v = tab_data.profile.__getattribute__(field_descriptor.name)
            #     if field_value != v:
            #         print(field_descriptor.name, field_value, v)

            if file_data != tab_data:
                raise IOError
        except IOError:
            return tab_data
        return False

    def closeEvent(self, event) -> None:
        self.custom_close(event)

    def custom_close(self, event):
        for i in range(self.profilesTabs.count()):
            if not self.close_tab(self.profilesTabs.currentIndex()):
                event.ignore()
                return

    def init_ui(self):
        self.setObjectName("main_window")
        self.setEnabled(True)
        self.resize(720, 580)

        self.setMinimumSize(self.size())
        icon = QtGui.QIcon(':/app_icon.ico')
        # icon.addPixmap(QtGui.QPixmap(":/title/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.vlayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vlayout.setContentsMargins(-1, -1, -1, 9)
        self.vlayout.setObjectName("gridLayout")

        self.profilesTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.profilesTabs.setObjectName("tabWidget")

        self.vlayout.addWidget(self.profilesTabs, 0)
        self.setCentralWidget(self.centralwidget)

        self.profilesTabs.setTabsClosable(True)
        self.profilesTabs.setMovable(True)
        self.profilesTabs.setDocumentMode(True)
        self.profilesTabs.setElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.profilesTabs.setUsesScrollButtons(True)

        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.profile_tools = ProfilesTools(self)
        self.vlayout.addWidget(self.profile_tools)
        self.stacked = QtWidgets.QStackedWidget(self)
        self.vlayout.addWidget(self.stacked)
        self.add_button = AddButton(self)
        self.stacked.addWidget(self.add_button)
        self.stacked.addWidget(self.profilesTabs)
        self.profilesTabs.setObjectName('ProfilesTabs')
        self.footer_widget = FooterWidget(self)
        self.vlayout.addWidget(self.footer_widget)

        self.tr_ui()
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        self.setWindowTitle(tr("main_window", "PyBalCalc"))
