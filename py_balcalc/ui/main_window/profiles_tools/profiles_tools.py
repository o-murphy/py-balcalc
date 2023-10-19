# -*u.- coding: utf-8 -*u.-

from PySide6 import QtCore, QtGui, QtWidgets

from .ui import UiProfilesTools
import qtawesome as qta


# top profiles_table toolbar
from ...settings import AppSettings


class ProfilesTools(QtWidgets.QWidget, UiProfilesTools):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui(self)

        self.layout().setAlignment(QtCore.Qt.AlignLeft)
        self.saveButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.saveButtonMenu = QtWidgets.QMenu(self)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/saveasbtn_menu21a.png"),
                        QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.saveAsAction = QtGui.QAction(icon9, 'Save as... (CTRL+Shift+S)', self)
        self.saveButtonMenu.addAction(self.saveAsAction)

        self.saveButton.customContextMenuRequested.connect(self.on_context_menu)

        self.Preferences.clicked.connect(self.open_app_settings)

        # self.saveAsAction.triggered.connect(tabw.save_as_file_dialog)

    def setup_ui(self, profilesTools):
        super(ProfilesTools, self).setup_ui(profilesTools)
        self.Preferences = QtWidgets.QToolButton(self)
        self.Preferences.setMinimumSize(QtCore.QSize(30, 30))
        self.Preferences.setIcon(qta.icon('mdi6.cog', color='white'))
        self.Preferences.setIconSize(QtCore.QSize(24, 24))
        self.Preferences.setObjectName("Preferences")
        self._layout.addWidget(self.Preferences, alignment=QtCore.Qt.AlignRight)

    def on_context_menu(self, point):
        self.saveButtonMenu.exec_(self.saveButton.mapToGlobal(point))

    def open_app_settings(self):
        """opens AppSettings dialog and updates app settings if it changed"""
        AppSettings().exec_()
