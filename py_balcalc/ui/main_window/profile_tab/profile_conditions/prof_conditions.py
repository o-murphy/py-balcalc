from PySide6 import QtWidgets, QtCore

from .ui import Ui_conditions


class ProfileConditions(QtWidgets.QWidget, Ui_conditions):
    """shows selected profile atmo conditions"""
    def __init__(self, parent=None):
        super(ProfileConditions, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, conditions):
        super(ProfileConditions, self).setupUi(conditions)
        self.groupBox.setCheckable(False)
        self.groupBox.layout().setAlignment(QtCore.Qt.AlignLeft)
