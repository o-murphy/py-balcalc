from PySide6 import QtWidgets
from py_ballisticcalc import AbstractUnit, Unit, UnitPropsDict
from py_ballisticcalc.unit import UnitProps
from qtpy import QtCore
from py_balcalc.settings import DEF_FIELDS_LIMITS, app_settings
from py_balcalc.signals_manager import appSignalMgr


# Fix of Unit.INCH accuracy
UnitPropsDict[Unit.INCH] = UnitProps("inch", 3, "inch")


class UnitSpinBox(QtWidgets.QDoubleSpinBox):

    def __init__(self, parent, default: AbstractUnit, unit_settings_key: str):
        super().__init__(parent)

        self._unit_settings_key = unit_settings_key
        self._raw_value = default

        self.update_display_unit()

        self.valueChanged.connect(self.update_raw_value)
        appSignalMgr.settings_units_updated.connect(self.update_display_unit)
        appSignalMgr.settings_locale_updated.connect(self.tr)

    def wheelEvent(self, event) -> None:
        pass

    def validate(self, text: str, pos: int) -> object:
        # text = text.split(' ')[0].replace(".", ",")
        text = text.split(' ')[0].replace(",", ".")
        return QtWidgets.QDoubleSpinBox.validate(self, text, pos)

    def valueFromText(self, text: str) -> float:
        text = text.split(' ')[0].replace(",", ".")
        return float(text)

    def set_display_unit(self, unit: Unit):
        self.setDecimals(unit.accuracy)
        self.setMaximum(DEF_FIELDS_LIMITS[self._unit_settings_key]['max'])
        self.setMinimum(DEF_FIELDS_LIMITS[self._unit_settings_key]['min'])
        self.setSingleStep(10**(-self.decimals()))
        self.tr()

    def update_display_unit(self):
        self.set_display_unit(app_settings.value(self._unit_settings_key))
        self.setValue(self._raw_value >> app_settings.value(self._unit_settings_key))

    def update_raw_value(self, value):
        self._raw_value = app_settings.value(self._unit_settings_key)(value)

    def raw_value(self):
        return self._raw_value

    def set_raw_value(self, value: AbstractUnit):
        self._raw_value = value
        self.setValue(self._raw_value >> app_settings.value(self._unit_settings_key))
        self.set_display_unit(app_settings.value(self._unit_settings_key))

    def tr(self):
        _translate = QtCore.QCoreApplication.translate
        self.setSuffix(
            ' ' + _translate(
                "units",
                app_settings.value(self._unit_settings_key).symbol)
        )
