# -*- coding: utf-8 -*-
from PySide6 import QtWidgets, QtGui, QtCore
import sys
# from modules import env_update
from .ui import Ui_MainWindow
# from gui import FooterWidget
from .profiles_tab import ProfilesTab
# from gui import CatalogTab
# from gui import TemplatesTab
# from modules.env_update import CONFIG_PATH
# from gui.app_settings import AppSettings
# from gui.spinner import Spinner

# assert Spinner

# from extensions import ExtendAll

# import configparser


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, app=None):
        super().__init__()
        self.profiles_tab = ProfilesTab(*sys.argv)
        self.setupUi(self)
        self.app = app
        self.translator_custom = QtCore.QTranslator()
        # self.translator_qt = QtCore.QTranslator()
        # self.app_settings = self.app.settings
        # self.lang = None
        # self.config = configparser.ConfigParser()
        # self.units = None
        # self.setUnits()
        # self.extend = ExtendAll(self)
        # self.setLang()

    def setupUi(self, main_window: 'MainWindow'):
        super().setupUi(main_window)
        self.tabWidget.setObjectName('MainTabWidget')
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.profiles_tab, QtGui.QIcon(":/material/material/list-ul-orange.svg"), 'Profiles')
        self.tabWidget.tabBar().setIconSize(QtCore.QSize(20, 20))

    # def setUnits(self):
    #     self.config.read(CONFIG_PATH)
    #     self.units = self.config['Units']
    #     for c in self.findChildren(QtWidgets.QWidget):
    #         if hasattr(c, 'setUnits'):
    #             c.setUnits()

    # def setLang(self):
    #     self.config.read(CONFIG_PATH)
    #     if not os.path.isfile(CONFIG_PATH):
    #         self.config.add_section('Locale')
    #
    #         self.config.set('Locale', 'system', QtCore.QLocale.system().name().split('_')[1].lower())
    #         self.config.set('Locale', 'current', QtCore.QLocale.system().name().split('_')[1].lower())
    #         with open(CONFIG_PATH, 'w') as fp:
    #             self.config.write(fp)
    #
    #     self.lang = self.config['Locale']['current']
    #
    #     app = QtCore.QCoreApplication.instance()
    #     app.removeTranslator(self.translator_qt)
    #     app.removeTranslator(self.translator_custom)
    #
    #     if self.lang != 'en':
    #         if not os.path.isfile(f'translate/eng-{self.lang}.qm'):
    #             self.lang = self.config['Locale']['system']
    #             self.config.set('Locale', 'current', self.lang)
    #
    #         with open(CONFIG_PATH, 'w') as fp:
    #             self.config.write(fp)
    #         if self.lang != 'en':
    #
    #             self.translator_custom = QtCore.QTranslator()
    #             self.translator_custom.load(f'translate/eng-{self.lang}.qm')
    #
    #             self.translator_qt = QtCore.QTranslator()
    #             self.translator_qt.load(f'translate/qtbase_{self.lang}.qm')
    #
    #             app.installTranslator(self.translator_qt)
    #             app.installTranslator(self.translator_custom)
    #     self.retranslateUi(self)
    #     for c in self.findChildren(QtWidgets.QWidget):
    #         if hasattr(c, 'retranslateUi'):
    #             c.retranslateUi(c)
    #     self.retranslate_tabs()
    #
    # # def setupDriverCheck(self):
    # #     self.lpc_dialog = LPC_dialog()

    def setupWidgets(self):
        # self.my_tab = TemplatesTab()
        # self.catalog_tab = CatalogTab()
        # self.tabWidget.addTab(self.my_tab, QtGui.QIcon(":/ballistics/templates.svg"), 'Templates')
        # self.tabWidget.addTab(self.catalog_tab, QtGui.QIcon(":/material/material/bag-check-orange.svg"), 'Catalog')

        # footer_widget = FooterWidget(self)
        # self.__setattr__('footer_widget', footer_widget)
        # self.gridLayout.addWidget(self.footer_widget, 1, 0, 1, 1)
        ...

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

    def retranslate_tabs(self):
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(0, _translate("main_window", 'Profiles'))
        self.tabWidget.setTabText(1, _translate("main_window", 'Templates'))
        self.tabWidget.setTabText(2, _translate("main_window", 'Catalog'))


