# -*- coding: utf-8 -*-
from PySide6 import QtWidgets, QtGui, QtCore
import sys
# from modules import env_update
from .add_button import AddButton
from .profile_tab.profile_item import ProfileItem
from .profile_tab.profile_wizard import ProfileWizard
from .ui import Ui_MainWindow
from ..footer import FooterWidget
from .profile_tab import ProfileTab
from .profiles_tools import ProfilesTools
from ..settings import AppSettings
# from gui import CatalogTab
# from gui import TemplatesTab
# from modules.env_update import CONFIG_PATH
# from gui.app_settings import AppSettings
# from gui.spinner import Spinner

# assert Spinner
from ...file import open_files


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, app=None):
        super().__init__()

        self.setupUi(self)
        self.app = app
        self.translator_custom = QtCore.QTranslator()
        # self.translator_qt = QtCore.QTranslator()
        # self.app_settings = self.app.settings

        self.setConnects()

    def open_wizard(self):
        # dlg = ProfileWizard(self, profile=new_item)
        # if dlg.exec_():
        #     prof = dlg.profile
        #     profile_tab = ProfileTab(prof)
        #     self.profilesTabs.addTab(profile_tab, prof.profile.profile_name[:12])
        # self.switch_stacked()
        ...

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
            profiles = open_files(file_names)
            for prof in profiles:
                profile_tab = ProfileTab(prof)
                self.profilesTabs.addTab(profile_tab, prof.profile.profile_name[:12])
            self.switch_stacked()

    def switch_stacked(self):
        count = self.profilesTabs.count()
        self.stacked.setCurrentIndex(count > 0)

    def setConnects(self):
        self.add_button.add.clicked.connect(self.open_file_dialog)
        self.profile_tools.openFile.clicked.connect(self.open_file_dialog)
        self.profile_tools.newProfileButton.clicked.connect(self.open_wizard)
        self.profilesTabs.tabCloseRequested.connect(self.close_tab)

    def close_tab(self, index):
        self.profilesTabs.removeTab(index)
        self.switch_stacked()

    def setupUi(self, main_window: 'MainWindow'):
        super().setupUi(main_window)
        self.profilesTabs.setTabsClosable(True)
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
