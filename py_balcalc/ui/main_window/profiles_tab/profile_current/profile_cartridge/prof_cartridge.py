from PySide6 import QtWidgets, QtCore

from py_balcalc.settings import appSettings
from py_balcalc.signals_manager import appSignalMgr
from .ui import Ui_cartridge


# shows selected profile cartridge property
class ProfileCartridge(QtWidgets.QWidget, Ui_cartridge):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._cur_profile = None

        self.setConnects()
        appSignalMgr.appSettingsUpdated.connect(self.setUnits)

    def setupUi(self, cartridge):
        super(ProfileCartridge, self).setupUi(cartridge)
        self.cartridgeGroupBox.setCheckable(False)
        self.cartridgeGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)

    def setConnects(self):
        self.mv.valueChanged.connect(self._validate_mv)
        self.temp.valueChanged.connect(self._temp_changed)
        self.ts.valueChanged.connect(self._ts_changed)
        self.cartridgeName.textChanged.connect(self._cartridge_name_changed)

    def disconnect(self):
        self.mv.valueChanged.disconnect(self._validate_mv)
        self.temp.valueChanged.disconnect(self._temp_changed)
        self.ts.valueChanged.disconnect(self._ts_changed)
        self.cartridgeName.textChanged.disconnect(self._cartridge_name_changed)

    def _ts_changed(self, value):
        self._cur_profile.ts = value

    def _cartridge_name_changed(self, text):
        self._cur_profile.cartridgeName.setText(text)

    def _temp_changed(self, value):
        self._cur_profile._temp = appSettings.value('unit/temperature')(value)

    def _validate_mv(self, value):
        if self.mv.value() == 0:
            self.mv.setFocus()
        else:
            self._cur_profile.mv = appSettings.value('unit/velocity')(value)

    def setUnits(self):
        self.disconnect()
        if self._cur_profile:
            _translate = QtCore.QCoreApplication.translate

            vu = appSettings.value('unit/velocity')
            tu = appSettings.value('unit/temperature')

            self.mv.setValue(self._cur_profile.mv >> vu)
            self.temp.setValue(self._cur_profile.temp >> tu)
            self.mv.setSuffix(' ' + _translate("units", vu.symbol))
            self.temp.setSuffix(' ' + _translate("units", tu.symbol))

            self.cartridgeName.setText(self._cur_profile.cartridgeName.text())
            self.ts.setValue(self._cur_profile.ts)
        self.setConnects()

    def set_current(self, profile):
        """updates inner widgets data with selected profile data"""
        self._cur_profile = profile
        self.setUnits()
