import os.path

from PySide6.QtCore import QSettings
from py_ballisticcalc import Unit, UnitPropsDict
from py_ballisticcalc import Settings as CalcSettings
from py_ballisticcalc.unit import UnitProps


CalcSettings.Units.sight_height = Unit.MILLIMETER
CalcSettings.Units.velocity = Unit.MPS
CalcSettings.Units.distance = Unit.METER

# Fix of Unit.INCH accuracy
UnitPropsDict[Unit.INCH] = UnitProps("inch", 3, "inch")
UnitPropsDict[Unit.IN_HG] = UnitProps('inhg', 6, 'inhg')
UnitPropsDict[Unit.GRAIN] = UnitProps('grain', 1, 'gr')

DEFAULT_USER_DIR = os.path.join(os.path.expanduser("~"), 'archer_bc2_profiles')


DEFAULT_SETTINGS = {
    "locale": "English",
    "env/user_dir": DEFAULT_USER_DIR,
    "unit/sight_height": CalcSettings.Units.sight_height,
    "unit/twist": CalcSettings.Units.twist,
    "unit/velocity": CalcSettings.Units.velocity,
    "unit/distance": CalcSettings.Units.distance,
    "unit/b_diameter": CalcSettings.Units.diameter,
    "unit/b_length": CalcSettings.Units.length,
    "unit/temperature": CalcSettings.Units.temperature,
    "unit/pressure": CalcSettings.Units.pressure,
    "unit/b_weight": CalcSettings.Units.weight,
    "unit/energy": CalcSettings.Units.energy,
    "unit/drop": CalcSettings.Units.drop,
    "unit/adjustment": CalcSettings.Units.adjustment,
    "unit/angular": CalcSettings.Units.angular,
    "unit/target_height": CalcSettings.Units.target_height,
    "unit/ogw": CalcSettings.Units.ogw,
}

INF = 99999
DEF_UNITS_LIMITS = {
    "unit/distance": {'min': Unit.METER(1), 'max': Unit.METER(3000)},
    "unit/sight_height": {'min': Unit.MILLIMETER(-5000), 'max': Unit.MILLIMETER(5000)},
    "unit/twist": {'min': Unit.INCH(0), 'max': Unit.INCH(100)},
    "unit/velocity": {'min': Unit.MPS(0), 'max': Unit.MPS(3000)},
    "unit/temperature": {'min': Unit.CELSIUS(-100), 'max': Unit.CELSIUS(100)},
    "unit/pressure": {'min': Unit.HP(300), 'max': Unit.HP(1500)},
    "unit/b_diameter": {'min': Unit.INCH(0.001), 'max': Unit.INCH(65.535)},
    "unit/b_length": {'min': Unit.INCH(0.01), 'max': Unit.INCH(200)},
    "unit/b_weight": {'min': Unit.GRAIN(10), 'max': Unit.GRAIN(6553.5)},
    "unit/energy": {'min': Unit.POUND(0), 'max': Unit.POUND(INF)},
    "unit/drop": {'min': Unit.CM_PER_100M(0), 'max': Unit.CM_PER_100M(INF)},
    "unit/adjustment": {'min': Unit.DEGREE(0), 'max': Unit.DEGREE(359)},
    "unit/angular": {'min': Unit.DEGREE(0), 'max': Unit.DEGREE(359)},
    "unit/target_height": {'min': Unit.INCH(5), 'max': Unit.METER(5)},
    "unit/ogw": {'min': Unit.KILOGRAM(0), 'max': Unit.KILOGRAM(INF)},
}


DEF_STRINGS_LIMITS = {
    "profile_name": 50,
    "cartridge_name": 50,
    "bullet_name": 50,
    "short_name_top": 8,
    "short_name_bot": 8,
    "user_note": 1024,
    "caliber": 50,
    "device_uuid": 50,
}

DEF_DISTANCES_LIST_SIZE = 200
DEF_COEFFICIENTS_LIST_SIZE = 200
DEF_SWITCH_LIST_SIZE = 4

DEF_FLOAT_LIMITS = {
    "zero_x": {"min": -200, "max": 200},
    "zero_y": {"min": -200, "max": 200},
    "c_t_coeff": {"min": 0.002, "max": 3},
    "c_zero_air_humidity": {"min": 0, "max": 100},

    "c_zero_w_pitch": {"min": -90, "max": 90},  # TODO: not implemented yet
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


def get_default_user_dir():
    os.makedirs(DEFAULT_USER_DIR, exist_ok=True)
    return DEFAULT_USER_DIR


def get_user_dir():
    last_user_dir = app_settings.value("env/user_dir")
    if not os.path.exists(last_user_dir):
        app_settings.setValue("env/user_dir", DEFAULT_USER_DIR)
        return get_default_user_dir()
    return app_settings.value("env/user_dir")


get_default_user_dir()
app_settings = AppSettingsStorage('PyBalCalc', 'Settings')
print(app_settings.fileName())
load_default_settings(app_settings)
