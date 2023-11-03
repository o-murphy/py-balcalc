# -*u.- coding: utf-8 -*u.-

from PySide6 import QtCore, QtGui, QtWidgets

import qtawesome as qta

from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr
# top profiles_table toolbar
from py_balcalc.ui.settings import AppSettings


class ProfilesTools(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

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

        self.preferences.clicked.connect(self.open_app_settings)

    def on_context_menu(self, point):
        self.saveButtonMenu.exec_(self.saveButton.mapToGlobal(point))

    def open_app_settings(self):
        """opens AppSettings dialog and updates app settings if it changed"""
        AppSettings().exec_()

    def init_ui(self):
        self.setObjectName("profiles_tools")
        self.resize(325, 30)

        self._layout = QtWidgets.QHBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setObjectName("_layout")

        self.loadBookMark = QtWidgets.QToolButton(self)
        self.loadBookMark.setMinimumSize(QtCore.QSize(30, 30))
        self.loadBookMark.setIcon(qta.icon('mdi6.database', color='white'))
        self.loadBookMark.setIconSize(QtCore.QSize(24, 24))
        self.loadBookMark.setObjectName("loadBookMark")

        self.newProfileButton = QtWidgets.QToolButton(self)
        self.newProfileButton.setMinimumSize(QtCore.QSize(30, 30))
        self.newProfileButton.setIcon(qta.icon('mdi6.plus', color='white'))
        self.newProfileButton.setIconSize(QtCore.QSize(24, 24))
        self.newProfileButton.setObjectName("newProfileButton")

        self.saveButton = QtWidgets.QToolButton(self)
        self.saveButton.setMinimumSize(QtCore.QSize(30, 30))
        self.saveButton.setIcon(qta.icon('mdi6.content-save-outline', color='white'))
        self.saveButton.setIconSize(QtCore.QSize(24, 24))
        self.saveButton.setObjectName("saveButton")

        self.openFile = QtWidgets.QToolButton(self)
        self.openFile.setMinimumSize(QtCore.QSize(30, 30))
        self.openFile.setIcon(qta.icon('mdi6.file-outline', color='white'))
        self.openFile.setIconSize(QtCore.QSize(24, 24))
        self.openFile.setObjectName("openFile")

        self.saveAsButton = QtWidgets.QToolButton(self)
        self.saveAsButton.setMinimumSize(QtCore.QSize(30, 30))
        self.saveAsButton.setIcon(qta.icon('mdi6.content-save-settings-outline', color='white'))
        self.saveAsButton.setIconSize(QtCore.QSize(24, 24))
        self.saveAsButton.setObjectName("saveAsButton")

        self.preferences = QtWidgets.QToolButton(self)
        self.preferences.setMinimumSize(QtCore.QSize(30, 30))
        self.preferences.setIcon(qta.icon('mdi6.cog', color='white'))
        self.preferences.setIconSize(QtCore.QSize(24, 24))
        self.preferences.setObjectName("Preferences")

        self._layout.addWidget(self.openFile)
        self._layout.addWidget(self.saveButton)
        self._layout.addWidget(self.saveAsButton)
        self._layout.addWidget(self.newProfileButton)
        self._layout.addWidget(self.loadBookMark)
        self._layout.addWidget(self.preferences, alignment=QtCore.Qt.AlignRight)

        self.newProfileButton.setShortcut("Ctrl+N")
        self.saveButton.setShortcut("Ctrl+S")
        self.openFile.setShortcut("Ctrl+O")
        self.saveAsButton.setShortcut("Ctrl+Shift+S")

        self.tr_ui()
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        # tr = QtCore.QCoreApplication.translate
        self.loadBookMark.setToolTip(tr("profiles_tools", "Load from templates"))
        self.newProfileButton.setToolTip(tr("profiles_tools", "Add Profile (CTRL+N)"))
        self.saveButton.setToolTip(tr("profiles_tools", "Save File (CTRL+S)"))
        self.openFile.setToolTip(tr("profiles_tools", "Open File (CTRL+O)"))
        self.saveAsButton.setToolTip(tr("profiles_tools", "Save as File (CTRL+SHIFT+S)"))
        self.preferences.setToolTip(tr("profiles_tools", "Settings"))
