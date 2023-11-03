from PySide6.QtCore import QSettings
from py_ballisticcalc import Unit
from py_ballisticcalc import Settings as CalcSettings


CalcSettings.Units.sight_height = Unit.MILLIMETER
CalcSettings.Units.velocity = Unit.MPS
CalcSettings.Units.distance = Unit.METER


DEFAULT_SETTINGS = {
    "locale": "us",
    "unit/sight_height": CalcSettings.Units.sight_height,
    "unit/twist": CalcSettings.Units.twist,
    "unit/velocity": CalcSettings.Units.velocity,
    "unit/distance": CalcSettings.Units.distance,
    "unit/diameter": CalcSettings.Units.diameter,
    "unit/length": CalcSettings.Units.length,
    "unit/temperature": CalcSettings.Units.temperature,
    "unit/pressure": CalcSettings.Units.pressure,
    "unit/weight": CalcSettings.Units.weight,
    "unit/energy": CalcSettings.Units.energy,
    "unit/drop": CalcSettings.Units.drop,
    "unit/adjustment": CalcSettings.Units.adjustment,
    "unit/angular": CalcSettings.Units.angular,
    "unit/target_height": CalcSettings.Units.target_height,
    "unit/ogw": CalcSettings.Units.ogw,
}


DEF_FIELDS_LIMITS = {
    "unit/sight_height": {'max': Unit.CENTIMETER(30), 'min': Unit.CENTIMETER(0.1)},
    "unit/twist": {'max': Unit.INCH(30), 'min': Unit.INCH(0)},
    "unit/velocity": {'max': Unit.MPS(2000), 'min': Unit.MPS(0)},
    "unit/distance": {'max': Unit.METER(5000), 'min': Unit.METER(10)},
    "unit/diameter": {'max': Unit.INCH(10), 'min': Unit.INCH(0.1)},
    "unit/length": {'max': Unit.INCH(30), 'min': Unit.INCH(0.1)},
    "unit/temperature": {'max': Unit.CELSIUS(50), 'min': Unit.CELSIUS(-50)},
    "unit/pressure": {'max': Unit.HP(1050), 'min': Unit.HP(875)},
    # "unit/pressure": {'max': Unit.MM_HG(770), 'min': Unit.MM_HG(640)},
    "unit/weight": {'max': Unit.KILOGRAM(60), 'min': Unit.GRAIN(1)},
    "unit/energy": {'max': None, 'min': Unit.POUND(0)},
    "unit/drop": {'max': None, 'min': Unit.CM_PER_100M(0)},
    "unit/adjustment": {'max': Unit.DEGREE(359), 'min': Unit.DEGREE(0)},
    "unit/angular": {'max': Unit.DEGREE(359), 'min': Unit.DEGREE(0)},
    "unit/target_height": {'max': Unit.METER(5), 'min': Unit.INCH(5)},
    "unit/ogw": {'max': None, 'min': Unit.KILOGRAM(0)},
}


class AppSettingsStorage(QSettings):

    def value(self, key: str, **kwargs) -> object:
        if not self.contains(key):
            self.setValue(key, DEFAULT_SETTINGS.get(key, None))
        return super().value(key, **kwargs)


def load_default_settings(settings: QSettings):
    for key, value in DEFAULT_SETTINGS.items():
        if not settings.contains(key):
            settings.setValue(key, value)


app_settings = AppSettingsStorage('PyBalCalc', 'Settings')
load_default_settings(app_settings)
