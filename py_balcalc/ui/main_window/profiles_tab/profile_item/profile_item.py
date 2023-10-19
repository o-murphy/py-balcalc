from re import search
from PySide6 import QtCore, QtWidgets, QtGui

# from dbworker import get_defaults
# from dbworker.models import DragFunc
# from modules.flags import DatabaseRW
from .ui import Ui_profileItem
from py_balcalc.ui.custom_widgets import NoWheelDoubleSpinBox


# creates, show and store ballistic profile
class ProfileItem(QtWidgets.QWidget, Ui_profileItem):
    def __init__(self, parent=None):
        super(ProfileItem, self).__init__(parent)
        self.setupUi(self)

        self.tile.setHidden(True)

        self.weightTile = ''
        self.caliberShort = ''
        self.tile = QtWidgets.QLabel(self.tile)

        self.z_x = NoWheelDoubleSpinBox()
        self.z_x = NoWheelDoubleSpinBox()
        self.z_x.setPrefix('X: ')
        self.z_y = NoWheelDoubleSpinBox()
        self.z_y.setPrefix('Y: ')
        self.z_d = NoWheelDoubleSpinBox()
        self.z_d.setMaximum(10000)
        self.z_x.setObjectName('z_x')
        self.z_y.setObjectName('z_y')
        self.z_d.setObjectName('z_d')
        self.z_d.resize(90, 50)
        self.z_d.setDecimals(1)

        self.gridLayout.addWidget(self.tile, 0, 0, 2, 1)
        self.gridLayout.addWidget(self.z_x, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.z_y, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.z_d, 0, 3, 2, 1)

        # self._z_d = Distance(100, DistanceMeter)  # zeroing distance
        #
        # self.auto_tile_mode = 0
        #
        # self.sh = Distance(0, DistanceMillimeter)  # sight height
        # self.twist = Distance(0, DistanceInch)  # barrel twist
        # self.caliberName = ''
        # self.rightTwist = True
        #
        # # current atmo conditions
        # self.z_pressure = Pressure(0, PressureMmHg)
        # self.z_temp = Temperature(0, TemperatureCelsius)
        # self.z_powder_temp = Temperature(0, TemperatureCelsius)
        # self.z_angle = Angular(0, AngularDegree)
        # self.z_azimuth = Angular(0, AngularDegree)
        # self.z_latitude = Angular(0, AngularDegree)
        # self.z_humidity = 0
        #
        # self.z_wind_angle = Angular(0, AngularDegree)
        # self.z_wind_speed = Velocity(0, VelocityMPS)
        #
        # # cartridge properties
        # self.mv = Velocity(0, VelocityMPS)
        # self.temp = Temperature(0, TemperatureCelsius)
        # self.ts = 1
        #
        # # bullet params
        # self.bulletName = ''
        # self.weight = Weight(0, WeightGrain)
        # self.length = Distance(0, DistanceInch)
        # self.diameter = Distance(0, DistanceInch)
        #
        # self.drag_idx = 0
        # self.drags = []
        #
        # self.app_settings = None
        # self.setUnits()
        #
        # self.z_d.valueChanged.connect(self.z_d_changed)

    # def z_d_changed(self, value):
    #     self._z_d = Distance(value, self.app_settings.distUnits.currentData())
    #
    # def setUnits(self):
    #     self.app_settings = self.window().app_settings
    #     self.z_d.setValue(self._z_d.get_in(self.app_settings.distUnits.currentData()))
    #     self.z_d.setSuffix(self.app_settings.distUnits.currentText())
    #
    # def create_tile(self):
    #     """creates tile of ballistic profile"""
    #
    #     self.weightTile = f'{int(self.weight.get_in(self.app_settings.wUnits.currentData()))}' \
    #                       f'{self.app_settings.wUnits.currentText().strip()}'
    #
    #     pixmap = QPixmap(32, 32)
    #     pixmap.fill(Qt.white)
    #     self.tile.setPixmap(pixmap)
    #
    #     tile_font = QFont('Arial Narrow')
    #     tile_font.setPixelSize(11)
    #     tile_font.setStyleStrategy(QFont.NoAntialias)
    #
    #     painter = QPainter(self.tile.pixmap())
    #     painter.setFont(tile_font)
    #
    #     row_size = 16
    #     row_count = 2
    #
    #     rows = [self.caliberShort, self.weightTile]
    #
    #     for i in range(1, row_count):
    #         painter.drawLine(0, int(row_size * i), 32, int(row_size * i))
    #         painter.drawLine(0, int(row_size * i) + 1, 32, int(row_size * i) + 1)
    #
    #     for i, r in enumerate(rows):
    #         rect = QRect(0, int(row_size * i), 32, row_size)
    #         painter.drawText(rect, Qt.AlignCenter, r)
    #
    # def auto_tile(self):
    #     """changes current auto tile creation mode"""
    #     if self.auto_tile_mode == 1:
    #         self.auto_tile_1()
    #     else:
    #         self.auto_tile_0()
    #
    # def auto_tile_1(self):
    #     """ auto update caliberShort text with mode 1"""
    #     self.caliberShort = self.caliberName.replace(' ', '').strip()[:7]
    #     self.auto_tile_mode = 0
    #
    # def auto_tile_0(self):
    #     """ auto update caliberShort text with mode 0"""
    #     reg = search(r'\.+\d+', self.caliberName)
    #     cal = reg.group() if reg else ''
    #     tile = ''.join((list(filter(lambda char: char.isupper(), self.caliberName))))
    #     # self.caliberShort.setText(f'{cal + tile}'[:7])
    #     self.caliberShort = f'{cal + tile}'[:7]
    #     self.auto_tile_mode = 1
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
    #         'twist': self.twist.get_in(DistanceInch),
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
    #         'weight': self.weight.get_in(WeightGrain),
    #         'length': self.length.get_in(DistanceInch),
    #         'diameter': self.diameter.get_in(DistanceInch),
    #
    #         'drag_idx': self.drag_idx,
    #         'drags': drags,
    #
    #     }
    #     return data
    #
    # def set(self, input_data):
    #     """set input data to ballistic profile instance"""
    #
    #     defaults = get_defaults()
    #     if input_data:
    #         defaults.update(input_data)
    #         data = defaults
    #     else:
    #         data = defaults
    #
    #     self._z_d = Distance(data['z_d'], DistanceMeter)
    #
    #     self.z_x.setValue(data['z_x'])
    #     self.z_y.setValue(data['z_y'])
    #
    #     self.sh = Distance(data['sh'], DistanceMillimeter)
    #     self.twist = Distance(data['twist'], DistanceInch)
    #     self.caliberName = data['caliberName']
    #     self.rightTwist = data['rightTwist']
    #     # self.caliberShort.setText(data['caliberShort'])
    #     self.caliberShort = data['caliberShort']
    #
    #     self.rifleName.setText(data['rifleName'])
    #     self.cartridgeName.setText(data['cartridgeName'])
    #
    #     self.z_pressure = Pressure(data['z_pressure'], PressureMmHg)
    #     self.z_temp = Temperature(data['z_temp'], TemperatureCelsius)
    #     self.z_powder_temp = Temperature(data['z_powder_temp'], TemperatureCelsius)
    #     self.z_angle = Angular(data['z_angle'], AngularDegree)
    #     self.z_azimuth = Angular(data['z_azimuth'], AngularDegree)
    #     self.z_latitude = Angular(data['z_latitude'], AngularDegree)
    #     self.z_humidity = data['z_humidity']
    #
    #     if 'z_wind_angle' in data:
    #         self.z_wind_angle = Angular(data['z_wind_angle'], AngularDegree)
    #     if 'z_wind_speed' in data:
    #         self.z_wind_speed = Velocity(data['z_wind_speed'], VelocityMPS)
    #
    #     self.mv = Velocity(data['mv'], VelocityMPS)
    #     self.temp = Temperature(data['temp'], TemperatureCelsius)
    #
    #     self.cartridgeName.setText(data['cartridgeName'])
    #     self.ts = data['ts']
    #
    #     self.weight = Weight(data['weight'], WeightGrain)
    #     self.length = Distance(data['length'], DistanceInch)
    #     self.diameter = Distance(data['diameter'], DistanceInch)
    #     self.bulletName = data['bulletName']
    #
    #     self.drag_idx = data['drag_idx']
    #
    #     for drag in data['drags']:
    #         if isinstance(drag, dict):
    #             drag = DragFunc(**drag, attrs=DatabaseRW.RW.value)
    #         self.drags.append(drag)
    #
    #     if self.caliberShort in ['', None]:
    #         self.auto_tile_0()
    #
    #     self.create_tile()
    #
    #     self.setUnits()
