# -*- coding: utf-8 -*-
import a7p
from PySide6 import QtWidgets, QtCore
from .add_button import AddButton
from .profile_wizard import ProfileWizard
from .ui import Ui_MainWindow
from ..footer import FooterWidget
from .profile_tab import ProfileTab
from .profiles_tools import ProfilesTools

from py_balcalc.file import open_files


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    filesDropped = QtCore.Signal(object)

    def __init__(self, app=None):
        super().__init__()

        self.setupUi(self)
        self.app = app
        self.translator_custom = QtCore.QTranslator()

        self.setConnects()

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
        dlg = ProfileWizard(self)
        if dlg.exec_():
            data = a7p.A7PFile.dumps(dlg.export_a7p())

            file_name = self.save_file_dialog()
            if file_name:
                with open(file_name, 'wb') as fp:
                    fp.write(data)
                self.open_files(file_name)

    def save_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, file_format = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "QFileDialog.getSaveFileName()",
            # USER_RECENT,
            filter="ArcherBC2 Profile (*.a7p)",
            # filter="ArcherBC2 Profile (*.a7p);;JSON (*.json);;All Files (*)",
            options=options
        )
        return file_name

    def open_file_dialog(self):
        # self.close_file()
        # if self.is_saved:
        options = QtWidgets.QFileDialog.Options()
        file_names, file_format = QtWidgets.QFileDialog.getOpenFileNames(
            self,
            "QFileDialog.getOpenFileName()",
            # USER_RECENT,
            filter="ArcherBC2 Profile (*.a7p)",
            # filter="ArcherBC2 Profile (*.a7p);;JSON (*.json);;All Files (*)",
            options=options
        )
        if file_names:
            self.open_files(*file_names)

    def switch_stacked(self):
        count = self.profilesTabs.count()
        self.stacked.setCurrentIndex(count > 0)

    def setConnects(self):
        self.add_button.clicked.connect(self.open_file_dialog)
        self.profile_tools.openFile.clicked.connect(self.open_file_dialog)
        self.profile_tools.newProfileButton.clicked.connect(self.open_wizard)
        self.profilesTabs.tabCloseRequested.connect(self.close_tab)

        self.profile_tools.saveAsButton.clicked.connect(self.save_file_as)

        self.filesDropped.connect(lambda file_names: self.open_files(*file_names))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        self.filesDropped.emit(files)

    def open_files(self, *file_names):
        profiles = open_files(file_names)
        for payload in profiles:
            profile_tab = ProfileTab(self, payload)
            self.profilesTabs.addTab(profile_tab, payload.profile.profile_name)
        self.switch_stacked()
        self.profilesTabs.setCurrentIndex(self.profilesTabs.count() - 1)

    def save_file_as(self):
        tab: ProfileTab = self.profilesTabs.currentWidget()
        data = a7p.A7PFile.dumps(tab.export_a7p())
        file_name = self.save_file_dialog()
        if file_name:
            with open(file_name, 'wb') as fp:
                fp.write(data)

    def close_tab(self, index):
        self.profilesTabs.removeTab(index)
        self.switch_stacked()

    def setupUi(self, main_window: 'MainWindow'):
        super().setupUi(main_window)
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

    # def closeEvent(self, event) -> None:
    #     self.custom_close(event)
    #
    # def custom_close(self, event):
    #     if not self.profiles_tab.is_saved:
    #         choice = self.profiles_tab.close_file()
    #         if choice == QtWidgets.QMessageBox.Cancel or not self.profiles_tab.is_saved:
    #             event.ignore()
    #         else:
    #             QtGui.QCloseEvent()
    #     else:
    #         QtGui.QCloseEvent()
    #     # if hasattr(self, 'profiles_tab'):
    #     #     self.profiles_tab.save_backup()
    #     # sys.exit()
