from PySide6 import QtWidgets, QtCore

from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr
from .conditions import CalcConditions
from py_balcalc.ui.main_window.profile_tab import ProfileTab
from py_ballisticcalc import *
import pyqtgraph as pg

from py_balcalc.settings import app_settings
from .table import TrajectoryTable


class CalculatorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, tab: ProfileTab = None):
        super(CalculatorDialog, self).__init__(parent)
        self.init_ui()
        self.tab = tab

        self.weapon = None
        self.drag_model = None
        self.ammo = None
        self.zero_atmo = None
        self.calc = None

        self.drop_plot = None
        self.drag_plot = None

        self.init_calculator()

        self.calculate()

        self.__post_init__()

    def __post_init__(self):
        self.fire_button.clicked.connect(self.calculate)

    def init_calculator(self):
        self.weapon = Weapon(
            self.tab.weapon.sc_height.raw_value(),
            self.tab.weapon.zero_dist.raw_value(),
            self.tab.weapon.twist.raw_value(),  # Todo: direction
            # TODO: zero_look_angle
        )
        _drag_model = self.tab.bullet.drag_model.model()
        print(_drag_model)
        if _drag_model in [TableG1, TableG7]:
            mbc = MultiBC(
                _drag_model,
                self.tab.bullet.b_diameter.raw_value(),
                self.tab.bullet.b_weight.raw_value(),
                self.tab.bullet.drag_model.data()
            )
            print(self.tab.bullet.drag_model.data())
            self.dm = DragModel.from_mbc(mbc)
        else:
            self.dm = DragModel(
                1,
                self.tab.bullet.drag_model.data(),
                self.tab.bullet.b_weight.raw_value(),
                self.tab.bullet.b_diameter.raw_value(),
            )
        self.ammo = Ammo(
            self.dm,
            self.tab.bullet.b_length.raw_value(),
            self.tab.cartridge.c_muzzle_velocity.raw_value(),
            self.tab.cartridge.c_t_coeff.value(),
            self.tab.cartridge.temp.raw_value(),
        )
        self.zero_atmo = Atmo(
            0,  # TODO: altitude
            self.tab.conditions.c_zero_air_pressure.raw_value(),
            self.tab.conditions.c_zero_temperature.raw_value(),
            self.tab.conditions.c_zero_air_humidity.value(),
        )
        self.calc = Calculator(self.weapon, self.ammo, self.zero_atmo)

    def calculate(self):
        if self.drop_plot:
            self.drop_plot.clear()
        if self.drag_plot:
            self.drag_plot.clear()

        shot_atmo = Atmo(
            0,
            self.conditions.c_zero_air_pressure.raw_value(),
            self.conditions.c_zero_temperature.raw_value(),
            self.conditions.c_zero_air_humidity.value()
        )
        shot = Shot(
            Unit.METER(3000),
            self.conditions.z_angle.raw_value(),
            atmo=shot_atmo,
            # TODO: winds
        )
        trajectory_step = Unit.METER(10)  # Todo: add to settings
        hit = self.calc.fire(shot, trajectory_step)

        distances = [p.distance >> app_settings.value('unit/distance') for p in hit.trajectory]
        drop = [p.drop >> app_settings.value('unit/drop') for p in hit.trajectory]

        cdm = self.calc.cdm
        cd_list = [item['CD'] for item in cdm]
        mach_list = [item['Mach'] for item in cdm]

        self.drop_plot = self.drop_plot_widget.plot(distances, drop, pen=pg.mkPen('orange', width=1))
        self.drag_plot = self.drag_plot_widget.plot(mach_list, cd_list, pen=pg.mkPen('orange', width=1))

        self.trajectory_table.load_data(hit)

    def init_ui(self):
        self.setObjectName("CalculatorDialog")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        self.setMinimumSize(QtCore.QSize(720, 480))

        self.layout_ = QtWidgets.QHBoxLayout(self)

        self.view_tabs = QtWidgets.QTabWidget(self)
        self.view_tabs.setTabPosition(QtWidgets.QTabWidget.South)

        self.drop_plot_widget = pg.PlotWidget(self)
        self.drag_plot_widget = pg.PlotWidget(self)
        self.trajectory_table = TrajectoryTable(self)

        self.conditions = CalcConditions(self)
        self.fire_button = QtWidgets.QPushButton("")

        lt = QtWidgets.QVBoxLayout()
        lt.addWidget(self.conditions)
        lt.addWidget(self.fire_button)

        self.view_tabs.addTab(self.drop_plot_widget, tr("calculator", "Drop"))
        self.view_tabs.addTab(self.drag_plot_widget, tr("calculator", "Drag model"))
        self.view_tabs.addTab(self.trajectory_table, tr("calculator", "Table"))

        self.layout_.insertLayout(0, lt)
        self.layout_.addWidget(self.view_tabs)

        self.drop_plot_widget.showGrid(x=True, y=True, alpha=0.3)
        self.drop_plot_widget.setLabel('bottom', text=tr("unit", app_settings.value('unit/distance').symbol))
        self.drop_plot_widget.setLabel('left', text=tr("unit", app_settings.value('unit/drop').symbol))

        self.drag_plot_widget.showGrid(x=True, y=True, alpha=0.3)
        self.drag_plot_widget.setLabel('bottom', text=tr("unit", "Mach"))
        self.drag_plot_widget.setLabel('left', text=tr("unit", "CD"))

        self.tr_ui()
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        self.conditions.setTitle(tr("calculator", "Shot atmosphere"))
        self.fire_button.setText(tr("calculator", "Fire"))
