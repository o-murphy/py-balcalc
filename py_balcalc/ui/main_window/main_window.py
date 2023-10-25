# -*- coding: utf-8 -*-
from PySide6 import QtWidgets, QtGui, QtCore
import sys
# from modules import env_update
from .ui import Ui_MainWindow
from ..footer import FooterWidget
from .profiles_tab import ProfilesTab
from ..settings import AppSettings
# from gui import CatalogTab
# from gui import TemplatesTab
# from modules.env_update import CONFIG_PATH
# from gui.app_settings import AppSettings
# from gui.spinner import Spinner

# assert Spinner


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, app=None):
        super().__init__()
        self.profiles_tab = ProfilesTab(*sys.argv)
        self.setupUi(self)
        self.app = app
        self.translator_custom = QtCore.QTranslator()
        # self.translator_qt = QtCore.QTranslator()
        # self.app_settings = self.app.settings

    def setupUi(self, main_window: 'MainWindow'):
        super().setupUi(main_window)
        self.tabWidget.setObjectName('MainTabWidget')
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.profiles_tab, QtGui.QIcon(":/material/material/list-ul-orange.svg"), 'Profiles')
        self.tabWidget.tabBar().setIconSize(QtCore.QSize(20, 20))

        # self.my_tab = TemplatesTab()
        # self.catalog_tab = CatalogTab()
        # self.tabWidget.addTab(self.my_tab, QtGui.QIcon(":/ballistics/templates.svg"), 'Templates')
        # self.tabWidget.addTab(self.catalog_tab, QtGui.QIcon(":/material/material/bag-check-orange.svg"), 'Catalog')

        self.footer_widget = FooterWidget(self)
        self.gridLayout.addWidget(self.footer_widget, 1, 0, 1, 1)

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
