from PySide6 import QtWidgets, QtCore

from .ui import Ui_cartridge


class ProfileCartridge(QtWidgets.QWidget, Ui_cartridge):
    """shows selected profile cartridge property"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, cartridge):
        super(ProfileCartridge, self).setupUi(cartridge)
        self.cartridgeGroupBox.setCheckable(False)
        self.cartridgeGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)
