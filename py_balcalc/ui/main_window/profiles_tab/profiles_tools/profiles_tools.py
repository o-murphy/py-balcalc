# -*u.- coding: utf-8 -*u.-

from PySide6 import QtCore, QtGui, QtWidgets

from .ui import Ui_profilesTools


# top profiles_table toolbar
class ProfilesTools(QtWidgets.QWidget, Ui_profilesTools):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.saveButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.saveButtonMenu = QtWidgets.QMenu(self)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ui_templates\\../.rsrc/res/drawable/saveasbtn_menu21a.png"),
                        QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.saveAsAction = QtGui.QAction(icon9, 'Save as... (CTRL+Shift+S)', self)
        self.saveButtonMenu.addAction(self.saveAsAction)

        self.saveButton.customContextMenuRequested.connect(self.on_context_menu)
        if self.parent():
            self.saveAsAction.triggered.connect(self.parent().save_as_file_dialog)

    def on_context_menu(self, point):
        self.saveButtonMenu.exec_(self.saveButton.mapToGlobal(point))
