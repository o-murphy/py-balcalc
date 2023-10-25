# -*- coding: utf-8 -*-

from PySide6 import QtWidgets, QtCore

from .ui import Ui_FooterWidget
from py_balcalc import __version__
from ..settings import AppSettings


# footer of the main app window
class FooterWidget(QtWidgets.QWidget, Ui_FooterWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.horizontalLayout.insertWidget(0, QtWidgets.QLabel(f"v{__version__}"), QtCore.Qt.AlignLeft)
        # self.horizontalLayout.setAlignment(QtCore.Qt.AlignRight)
        # self.Preferences.clicked.connect(self.open_app_settings)

    # def open_app_settings(self):
    #     """opens AppSettings dialog and updates app settings if it changed"""
    #     # dlg = self.window().settings
    #     if AppSettings().exec_():
    #         ...
        #     self.window().setUnits()
        #     self.window().setLang()
