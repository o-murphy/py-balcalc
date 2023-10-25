from re import search

import a7p
from PySide6 import QtCore, QtWidgets, QtGui

# from dbworker import get_defaults
# from dbworker.models import DragFunc
# from modules.flags import DatabaseRW
from py_balcalc.signals_manager import appSignalMgr
from .ui import Ui_profileItem
from py_balcalc.ui.custom_widgets import NoWheelDoubleSpinBox
from py_ballisticcalc import Unit
from py_balcalc.settings import appSettings


# creates, show and store ballistic profile
class ProfileItem(QtCore.QObject):
    def __init__(self, parent=None):
        super(ProfileItem, self).__init__(parent)
        # self.setupUi(self)

        self._payload = a7p.Payload()

        # self.tile.setHidden(True)

        self.rifleName = ''
        self.caliberName = ''
        self.cartridgeName = ''
        self.bulletName = ''
        self.weightTile = ''
        self.caliberShort = ''
        # self.tile = QtWidgets.QLabel(self.tile)

        # self.z_x = NoWheelDoubleSpinBox()
        # self.z_x = NoWheelDoubleSpinBox()
        # self.z_x.setPrefix('X: ')
        # self.z_y = NoWheelDoubleSpinBox()
        # self.z_y.setPrefix('Y: ')
        # self.z_d = NoWheelDoubleSpinBox()
        # self.z_d.setMaximum(10000)
        # self.z_x.setObjectName('z_x')
        # self.z_y.setObjectName('z_y')
        # self.z_d.setObjectName('z_d')
        # self.z_d.resize(90, 50)
        # self.z_d.setDecimals(1)

        # self.gridLayout.addWidget(self.tile, 0, 0, 2, 1)
        # self.gridLayout.addWidget(self.z_x, 0, 2, 1, 1)
        # self.gridLayout.addWidget(self.z_y, 1, 2, 1, 1)
        # self.gridLayout.addWidget(self.z_d, 0, 3, 2, 1)

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
        self.setUnits()

        appSignalMgr.appSettingsUpdated.connect(self.setUnits)

    def setConnects(self):
        # self.z_d.valueChanged.connect(self.z_d_changed)
        ...

    def disconnect(self):
        # self.z_d.valueChanged.disconnect(self.z_d_changed)
        ...

    def z_d_changed(self, value):
        self._z_d = appSettings.value('unit/distance')(value)

    def setUnits(self):
        self.disconnect()
        du = appSettings.value('unit/distance')
        _translate = QtCore.QCoreApplication.translate
        # self.z_d.setValue(self._z_d >> du)
        # self.z_d.setSuffix(' ' + _translate("units", du.symbol))
        self.setConnects()

    def create_tile(self):
        """creates tile of ballistic profile"""
        # settings = self.window().settings
        # wu = appSettings.value('unit/weight')
        # self.weightTile = f'{self.weight >> wu}' \
        #                   f'{wu.symbol}'

        # pixmap = QtGui.QPixmap(32, 32)
        # pixmap.fill(QtCore.Qt.white)
        # self.tile.setPixmap(pixmap)

        # tile_font = QtGui.QFont('Arial Narrow')
        # tile_font.setPixelSize(11)
        # tile_font.setStyleStrategy(QtGui.QFont.NoAntialias)

        # painter = QtGui.QPainter(self.tile.pixmap())
        # painter.setFont(tile_font)
        #
        # row_size = 16
        # row_count = 2
        #
        # rows = [self.caliberShort, self.weightTile]
        #
        # for i in range(1, row_count):
        #     painter.drawLine(0, int(row_size * i), 32, int(row_size * i))
        #     painter.drawLine(0, int(row_size * i) + 1, 32, int(row_size * i) + 1)
        #
        # for i, r in enumerate(rows):
        #     rect = QtCore.QRect(0, int(row_size * i), 32, row_size)
        #     painter.drawText(rect, QtCore.Qt.AlignCenter, r)
        # del painter
        ...

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
    #
    # def get(self) -> dict:
    #     """returns dict of all ballistic profile data"""
    #
    #     drags = []
    #     for drag in self.drags:
    #         drags.append({
    #             'drag_type': drag.drag_type,
    #             'data': drag.data,
    #             'comment': drag.comment
    #         })
    #
    #     data = {
    #         'z_d': self._z_d.get_in(DistanceMeter),
    #         'z_x': self.z_x.value(),
    #         'z_y': self.z_y.value(),
    #
    #         'rifleName': self.rifleName.text(),
    #         'cartridgeName': self.cartridgeName.text(),
    #         # 'caliberShort': self.caliberShort.text(),
    #         'caliberShort': self.caliberShort,
    #
    #         # 'weightTile': self.weightTile.text(),
    #         'weightTile': self.weightTile,
    #
    #         'sh': self.sh.get_in(DistanceMillimeter),
    #         'twistUnits': self.twistUnits.get_in(DistanceInch),
    #         'caliberName': self.caliberName,
    #         'rightTwist': self.rightTwist,
    #
    #         'z_pressure': self.z_pressure.get_in(PressureMmHg),
    #         'z_temp': self.z_temp.get_in(TemperatureCelsius),
    #         'z_powder_temp': self.z_powder_temp.get_in(TemperatureCelsius),
    #         'z_angle': self.z_angle.get_in(AngularDegree),
    #         'z_azimuth': self.z_azimuth.get_in(AngularDegree),
    #         'z_latitude': self.z_latitude.get_in(AngularDegree),
    #         'z_humidity': self.z_humidity,
    #
    #         'z_wind_angle': self.z_wind_angle.get_in(AngularDegree),
    #         'z_wind_speed': self.z_wind_speed.get_in(VelocityMPS),
    #
    #         'mv': self.mv.get_in(VelocityMPS),
    #         'temp': self.temp.get_in(TemperatureCelsius),
    #         'ts': self.ts,
    #
    #         'bulletName': self.bulletName,
    #         'wUnits': self.wUnits.get_in(WeightGrain),
    #         'lnUnits': self.lnUnits.get_in(DistanceInch),
    #         'dUnits': self.dUnits.get_in(DistanceInch),
    #
    #         'drag_idx': self.drag_idx,
    #         'drags': drags,
    #
    #     }
    #     return data
    #

    def get(self) -> a7p.Payload:
        prof = self._payload.profile
        # prof.c_zero_distance_idx = int(self._z_d >> Unit.METER) * 100
        return self._payload

    def set(self, payload: a7p.Payload):
        """set input data to ballistic profile instance"""

        # defaults = get_defaults()
        # if input_data:
        #     defaults.update(input_data)
    #         data = defaults
    #     else:
    #         data = defaults
    #
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
    #
    #     for drag in data['drags']:
    #         if isinstance(drag, dict):
    #             drag = DragFunc(**drag, attrs=DatabaseRW.RW.value)
    #         self.drags.append(drag)
    #
        if not self.caliberShort:
            self.auto_tile_0()

        self.create_tile()

        self.setUnits()
