import os.path
import sys

from PySide6.QtCore import QSettings
from py_ballisticcalc import Unit
from py_ballisticcalc import Settings as CalcSettings


CalcSettings.Units.sight_height = Unit.MILLIMETER
CalcSettings.Units.velocity = Unit.MPS
CalcSettings.Units.distance = Unit.METER


DEFAULT_SETTINGS = {
    "locale": "us",
    "env/user_dir": os.path.join(os.path.expanduser("~"), 'archer_bc2_profiles'),
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


DEF_UNITS_LIMITS = {
    "unit/sight_height": {'max': Unit.CENTIMETER(30), 'min': Unit.CENTIMETER(0.1)},
    "unit/twist": {'max': Unit.INCH(30), 'min': Unit.INCH(0)},
    "unit/velocity": {'max': Unit.MPS(3000), 'min': Unit.MPS(0)},
    "unit/distance": {'max': Unit.METER(5000), 'min': Unit.METER(10)},
    "unit/diameter": {'max': Unit.INCH(65.535), 'min': Unit.INCH(0.001)},
    "unit/length": {'max': Unit.INCH(10), 'min': Unit.INCH(0.1)},
    "unit/temperature": {'max': Unit.CELSIUS(100), 'min': Unit.CELSIUS(-100)},
    "unit/pressure": {'max': Unit.HP(1050), 'min': Unit.HP(875)},
    # "unit/pressure": {'max': Unit.MM_HG(770), 'min': Unit.MM_HG(640)},
    "unit/weight": {'max': Unit.GRAIN(6553.5), 'min': Unit.GRAIN(1)},
    "unit/energy": {'max': None, 'min': Unit.POUND(0)},
    "unit/drop": {'max': None, 'min': Unit.CM_PER_100M(0)},
    "unit/adjustment": {'max': Unit.DEGREE(359), 'min': Unit.DEGREE(0)},
    "unit/angular": {'max': Unit.DEGREE(359), 'min': Unit.DEGREE(0)},
    "unit/target_height": {'max': Unit.METER(5), 'min': Unit.INCH(5)},
    "unit/ogw": {'max': None, 'min': Unit.KILOGRAM(0)},
}


DEF_STRINGS_LIMITS = {
    "profile_name": 50,
    "cartridge_name": 50,
    "bullet_name": 50,
    "short_name_top": 8,
    "short_name_bot": 8,
    "user_note": 250,
    "caliber": 50,
    "device_uuid": 50,
}

DEF_DISTANCES_LIST_SIZE = 200
DEF_COEFFICIENTS_LIST_SIZE = 200
DEF_SWITCH_LIST_SIZE = 4

DEF_FLOAT_LIMITS = {
    "zero_x": {"min": -600, "max": 600},  # TODO: not implemented yet
    "zero_y": {"min": -600, "max": 600},  # TODO: not implemented yet
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


app_settings = AppSettingsStorage('PyBalCalc', 'Settings')
load_default_settings(app_settings)
