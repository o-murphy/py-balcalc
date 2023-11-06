from PySide6 import QtWidgets
from py_ballisticcalc import AbstractUnit, Unit
from py_balcalc.settings import DEF_UNITS_LIMITS, app_settings
from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr


class UnitSpinBox(QtWidgets.QDoubleSpinBox):

    def __init__(self, parent, default: AbstractUnit, unit_settings_key: str):
        super().__init__(parent)

        self._unit_settings_key = unit_settings_key
        self.set_display_unit(app_settings.value(self._unit_settings_key))
        self._raw_value = None
        self.set_raw_value(default)

        self.__post_init__()

    def __post_init__(self):
        self.valueChanged.connect(self.update_raw_value)
        appSignalMgr.translator_updated.connect(self.tr_ui)
        appSignalMgr.settings_units_updated.connect(self.update_display_unit)
        appSignalMgr.settings_locale_updated.connect(self.tr_ui)
        self.update_display_unit()
        self.tr_ui()

    def wheelEvent(self, event) -> None:
        pass

    def validate(self, text: str, pos: int) -> object:
        # text = text.split(' ')[0].replace(".", ",")
        text = text.replace(".", ",")
        return QtWidgets.QDoubleSpinBox.validate(self, text, pos)

    def valueFromText(self, text: str) -> float:
        text = text.split(' ')[0].replace(",", ".")
        return float(text)

    def set_display_unit(self, unit: Unit):
        self.setDecimals(unit.accuracy)
        min_, max_ = DEF_UNITS_LIMITS[self._unit_settings_key].values()
        self.setRange(min_ >> unit, max_ >> unit)
        self.setSingleStep(10**(-self.decimals()))
        self.tr_ui()

    def update_display_unit(self):
        unit = app_settings.value(self._unit_settings_key)
        self.set_display_unit(unit)
        self.setValue(self._raw_value >> unit)

    def update_raw_value(self, value):
        self._raw_value = app_settings.value(self._unit_settings_key)(value)
        self.validate_value()

    def raw_value(self):
        return self._raw_value

    def set_raw_value(self, value: AbstractUnit):
        self._raw_value = value
        self.set_display_unit(app_settings.value(self._unit_settings_key))
        self.setValue(self._raw_value >> app_settings.value(self._unit_settings_key))

    def valid(self):
        return not self.property("invalid")

    def set_valid(self, valid: bool = True):
        self.setProperty("invalid", not valid)

    def validate_value(self, min_=None, max_=None):
        if not min_:
            min_ = app_settings.value(self._unit_settings_key)(self.minimum())
        if not max_:
            max_ = app_settings.value(self._unit_settings_key)(self.maximum())
        if min_ <= self._raw_value <= max_:
            self.set_valid()
        else:
            self.set_valid(False)

    def tr_ui(self):
        try:
            self.setSuffix(
                ' ' + tr(
                    "units",
                    app_settings.value(self._unit_settings_key).symbol)
            )
        except Exception:
            print(self.objectName(), app_settings.value(self._unit_settings_key))
