from PySide6 import QtWidgets, QtCore

from py_balcalc.signals_manager import appSignalMgr
from .ui import Ui_cartridge


class ProfileCartridge(QtWidgets.QWidget, Ui_cartridge):
    """shows selected profile cartridge property"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._cur_profile = None
        appSignalMgr.appSettingsUpdated.connect(self.setUnits)

    def setupUi(self, cartridge):
        super(ProfileCartridge, self).setupUi(cartridge)
        self.cartridgeGroupBox.setCheckable(False)
        self.cartridgeGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)

    def setUnits(self):
        if self._cur_profile:
            _translate = QtCore.QCoreApplication.translate
            self.mv.set_raw_value(self._cur_profile.mv)
            self.temp.set_raw_value(self._cur_profile.temp)

            self.cartridgeName.setText(self._cur_profile.cartridgeName)
            self.ts.setValue(self._cur_profile.ts)

    def set_current(self, profile):
        """updates inner widgets data with selected profile data"""
        self._cur_profile = profile
        self.setUnits()
