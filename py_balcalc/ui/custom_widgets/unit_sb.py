from PySide6 import QtWidgets
from py_ballisticcalc import AbstractUnit, Unit
from qtpy import QtCore
from py_balcalc.settings import appSettings
from py_balcalc.signals_manager import appSignalMgr


class UnitSpinBox(QtWidgets.QDoubleSpinBox):

    def __init__(self, parent, default: AbstractUnit, unit_settings_key: str):
        super().__init__(parent)

        self._unit_settings_key = unit_settings_key
        self._display_unit = None
        self._raw_value = default

        self.update_display_unit()

        self.valueChanged.connect(self.update_raw_value)
        appSignalMgr.appSettingsUpdated.connect(self.update_display_unit)

    def wheelEvent(self, event) -> None:
        pass

    def valueFromText(self, text: str) -> float:
        print(text)
        text = text.split(' ')[0].replace(",", ".")
        return float(text)

    def set_display_unit(self, unit: Unit):
        self._display_unit = unit
        self.setDecimals(unit.accuracy)
        self.setSingleStep(10**(-self.decimals()))
        _translate = QtCore.QCoreApplication.translate
        self.setSuffix(' ' + _translate("units", unit.symbol))

        print(self._display_unit)
        # self.setValue(self._raw_value >> unit)

    def update_display_unit(self):
        self.set_display_unit(appSettings.value(self._unit_settings_key))
        self.setValue(self._raw_value >> self._display_unit)

    # def _from_raw(self, value) -> float:
    #     return self._raw_unit(value) >> self._unit
    #
    # def _to_raw(self, value) -> float:
    #     return self._unit(value) >> self._raw_unit
    #

    def update_raw_value(self, value):
        self._raw_value = self._display_unit(value)
        print('upd', value, self._display_unit(value))

    def set_raw_value(self, value: AbstractUnit):
        self._raw_value = value
        self.setValue(self._raw_value >> self._display_unit)
    #
    # def rawValue(self):
    #     return self._to_raw(self.value())
