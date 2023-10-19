from PySide6 import QtWidgets, QtCore
from .ui import Ui_cartridge


# shows selected profile cartridge property
class ProfileCartridge(QtWidgets.QWidget, Ui_cartridge):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.cartridgeGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)

        self._cur_profile = None
        self._cur_units = None

        # self.mv.valueChanged.connect(self._validate_mv)
        # self.temp.valueChanged.connect(self._temp_changed)
        # self.ts.valueChanged.connect(self._ts_changed)
        # self.cartridgeName.textChanged.connect(self._cartridge_name_changed)

    # def _ts_changed(self, value):
    #     self._cur_profile.ts = value
    #
    # def _cartridge_name_changed(self, text):
    #     self._cur_profile.cartridgeName.setText(text)

    # def _temp_changed(self, value):
    #     self._cur_profile._temp = Temperature(value, self._cur_units.tempUnits.currentData())
    #
    # def _validate_mv(self, value):
    #     if self.mv.value() == 0:
    #         self.mv.setFocus()
    #     else:
    #         self._cur_profile.mv = Velocity(value, self._cur_units.vUnits.currentData())

    # def setUnits(self):
    #     self._cur_units = self.window().app_settings
    #
    #     if self._cur_profile:
    #         self.mv.setValue(int(self._cur_profile.mv.get_in(self._cur_units.vUnits.currentData())))
    #         self.temp.setValue(int(self._cur_profile.temp.get_in(self._cur_units.tempUnits.currentData())))
    #         self.mv.setSuffix(self._cur_units.vUnits.currentText())
    #         self.temp.setSuffix(self._cur_units.tempUnits.currentText())
    #
    #         self.cartridgeName.setText(self._cur_profile.cartridgeName.text())
    #         self.ts.setValue(self._cur_profile.ts)
    #
    # def set_current(self, profile):
    #     """updates inner widgets data with selected profile data"""
    #     self._cur_profile = profile
    #     self.setUnits()
