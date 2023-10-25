from re import search

import a7p
from PySide6 import QtCore

from py_ballisticcalc import Unit
from py_balcalc.settings import appSettings


# creates, show and store ballistic profile
class Profile(QtCore.QObject):
    def __init__(self, parent=None):
        super(Profile, self).__init__(parent)

        self._payload = a7p.Payload()

        self.rifleName = ''
        self.caliberName = ''
        self.cartridgeName = ''
        self.bulletName = ''
        self.weightTile = ''
        self.caliberShort = ''

        self._z_d = Unit.METER(100)  # zeroing distUnits

        self.auto_tile_mode = 0

        self.sh = Unit.MILLIMETER(0)  # sight height
        self.twist = Unit.INCH(0)  # barrel twistUnits
        self.caliberName = ''
        self.rightTwist = True

        # current atmo conditions
        self.z_pressure = Unit.MM_HG(0)
        self.z_temp = Unit.CELSIUS(0)
        self.z_powder_temp = Unit.CELSIUS(0)
        self.z_angle = Unit.DEGREE(0)
        self.z_azimuth = Unit.DEGREE(0)
        self.z_latitude = Unit.DEGREE(0)
        self.z_humidity = 0

        self.z_wind_angle = Unit.DEGREE(0)
        self.z_wind_speed = Unit.MPS(0)

        # cartridge properties
        self.mv = Unit.MPS(0)
        self.temp = Unit.CELSIUS(0)
        self.ts = 1

        # bullet params
        self.bulletName = ''
        self.weight = Unit.GRAIN(0)
        self.length = Unit.INCH(0)
        self.diameter = Unit.INCH(0)

        # self.drag_idx = 0
        # self.drags = []

        self.setConnects()

    def setConnects(self):
        # self.z_d.valueChanged.connect(self.z_d_changed)
        ...

    def disconnect(self):
        # self.z_d.valueChanged.disconnect(self.z_d_changed)
        ...

    def z_d_changed(self, value):
        self._z_d = appSettings.value('unit/distance')(value)


    def auto_tile(self):
        """changes current auto tile creation mode"""
        if self.auto_tile_mode == 1:
            self.auto_tile_1()
        else:
            self.auto_tile_0()

    def auto_tile_1(self):
        """ auto update caliberShort text with mode 1"""
        self.caliberShort = self.caliberName.replace(' ', '').strip()[:7]
        self.auto_tile_mode = 0

    def auto_tile_0(self):
        """ auto update caliberShort text with mode 0"""
        reg = search(r'\.+\d+', self.caliberName)
        cal = reg.group() if reg else ''
        tile = ''.join((list(filter(lambda char: char.isupper(), self.caliberName))))
        # self.caliberShort.setText(f'{cal + tile}'[:7])
        self.caliberShort = f'{cal + tile}'[:7]
        self.auto_tile_mode = 1

    def get(self) -> a7p.Payload:
        prof = self._payload.profile
        # prof.c_zero_distance_idx = int(self._z_d >> Unit.METER) * 100
        return self._payload

    def set(self, payload: a7p.Payload):
        """set input data to ballistic profile instance"""

        self._payload = payload
        prof = self._payload.profile
        self._z_d = Unit.METER(
            prof.distances[prof.c_zero_distance_idx] / 100
        )

        # self.z_x.setValue(prof.zero_x)
        # self.z_y.setValue(prof.zero_y)

        self.sh = Unit.MILLIMETER(prof.sc_height)
        self.twist = Unit.INCH(prof.r_twist / 100)
        self.caliberName = prof.caliber
        self.rightTwist = prof.twist_dir == 0
        self.caliberShort = prof.short_name_top

        self.rifleName = prof.profile_name
        self.cartridgeName = prof.cartridge_name

        self.z_pressure = Unit.HP(prof.c_zero_air_pressure / 10)
        self.z_temp = Unit.CELSIUS(prof.c_zero_temperature)
        self.z_powder_temp = Unit.CELSIUS(prof.c_zero_p_temperature)
        self.z_angle = Unit.DEGREE(prof.c_zero_w_pitch)
        # self.z_azimuth = Unit.DEGREE(data['z_azimuth'])
        # self.z_latitude = Angular(data['z_latitude'], AngularDegree)
        self.z_humidity = prof.c_zero_air_humidity

        # if 'z_wind_angle' in data:
        #     self.z_wind_angle = Unit.DEGREE(data['z_wind_angle'], AngularDegree)
        # if 'z_wind_speed' in data:
        #     self.z_wind_speed = Velocity(data['z_wind_speed'], VelocityMPS)

        self.mv = Unit.MPS(prof.c_muzzle_velocity / 10)
        self.temp = Unit.CELSIUS(prof.c_zero_temperature)
        self.ts = prof.c_t_coeff / 1000

        self.weight = Unit.GRAIN(prof.b_weight / 10)
        self.length = Unit.INCH(prof.b_length / 1000)
        self.diameter = Unit.INCH(prof.b_diameter / 1000)

        self.bulletName = prof.bullet_name

        # self.drag_idx = data['drag_idx']

        if not self.caliberShort:
            self.auto_tile_0()
