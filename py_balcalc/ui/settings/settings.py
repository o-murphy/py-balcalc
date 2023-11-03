from PySide6 import QtCore, QtWidgets, QtGui
from py_ballisticcalc.unit import *

from py_balcalc.settings import app_settings
from py_balcalc.signals_manager import appSignalMgr
from .units_tab import UnitsTab
from .general_tab import GeneralTab
from py_balcalc.translator import translator, tr


def get_units_list(unit):
    return [value for key, value in unit.__dict__.items() if isinstance(value, Unit)]


DistanceUnits = get_units_list(Distance)
VelocityUnits = get_units_list(Velocity)
TemperatureUnits = get_units_list(Temperature)
PressureUnits = get_units_list(Pressure)
EnergyUnits = get_units_list(Energy)
AngularUnits = get_units_list(Angular)
WeightUnits = get_units_list(Weight)


class AppSettings(QtWidgets.QDialog):
    """loads, writes and sets app preferences from settings.ini file"""

    def __init__(self):
        super(AppSettings, self).__init__()
        self.init_ui()

        self.init_general_tab()
        self.init_units_tab()
        self.tabsSettings.setCurrentIndex(0)
        self.__post_init__()

    def __post_init__(self):
        appSignalMgr.translator_updated.connect(self.tr_ui)
        # appSignalMgr.translator_updated.connect(self.tr_units)  # TODO:

    def init_general_tab(self):
        # Todo load list of languages

        for lang in translator.translations:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(f":/lang/{lang}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.general_tab.locale.addItem(icon, lang, lang)

        def on_change(key, value):
            app_settings.setValue(key, value)
            appSignalMgr.settings_locale_updated.emit()

        self.general_tab.locale.setCurrentIndex(
            self.general_tab.locale.findData(app_settings.value("locale"))
        )
        self.general_tab.locale.currentIndexChanged.connect(
            lambda: on_change("locale", self.general_tab.locale.currentData())
        )

    def init_units_tab(self):
        """
        creates extension _cur_units tab, loads settings or sets it to default values
        that will be used globally in the app and a ballistics calculations
        """

        def init_one_combo(combo_box: QtWidgets.QComboBox, items: list, default: str):

            def on_change():
                app_settings.setValue(default, combo_box.currentData())
                appSignalMgr.settings_units_updated.emit()

            [combo_box.addItem(tr('settings', i.key), userData=i) for i in items]
            combo_box.setCurrentIndex(combo_box.findData(app_settings.value(default)))
            combo_box.currentIndexChanged.connect(on_change)

        init_one_combo(self.units_tab.shUnits, DistanceUnits, 'unit/sight_height')
        init_one_combo(self.units_tab.twistUnits, DistanceUnits, 'unit/twist')
        init_one_combo(self.units_tab.distUnits, DistanceUnits, 'unit/distance')
        init_one_combo(self.units_tab.dUnits, DistanceUnits, 'unit/diameter')
        init_one_combo(self.units_tab.lnUnits, DistanceUnits, 'unit/length')
        init_one_combo(self.units_tab.dropUnits, DistanceUnits, 'unit/drop')
        init_one_combo(self.units_tab.thUnits, DistanceUnits, 'unit/target_height')

        init_one_combo(self.units_tab.vUnits, VelocityUnits, 'unit/velocity')
        init_one_combo(self.units_tab.tempUnits, TemperatureUnits, 'unit/temperature')
        init_one_combo(self.units_tab.pUnits, PressureUnits, 'unit/pressure')
        init_one_combo(self.units_tab.wUnits, WeightUnits, 'unit/weight')
        init_one_combo(self.units_tab.ogwUnits, WeightUnits, 'unit/ogw')
        init_one_combo(self.units_tab.eUnits, EnergyUnits, 'unit/energy')

        init_one_combo(self.units_tab.pathUnits, AngularUnits, 'unit/adjustment')
        init_one_combo(self.units_tab.angleUnits, AngularUnits, 'unit/angular')

    def tr_units(self):

        def tr_one(combo_box: QtWidgets.QComboBox):
            for i in range(combo_box.count()):
                data = combo_box.currentData(i)
                combo_box.setItemText(i, tr('settings', data.key))
                combo_box.setItemData(data)

        for ch in self.units_tab.findChildren(QtWidgets.QComboBox):
            tr_one(ch)


    def init_ui(self):
        self.setObjectName("AppSettings")
        self.resize(328, 424)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1, QtCore.Qt.AlignBottom)

        self.tabsSettings = QtWidgets.QTabWidget(self)
        self.tabsSettings.setObjectName("tabsSettings")

        self.general_tab = GeneralTab(self)
        self.tabsSettings.addTab(self.general_tab, "")

        self.units_tab = UnitsTab(self)
        self.tabsSettings.addTab(self.units_tab, "")

        self.gridLayout.addWidget(self.tabsSettings, 0, 0, 1, 1, QtCore.Qt.AlignTop)

        self.buttonBox.accepted.connect(self.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.reject)  # type: ignore

        self.tr_ui()

    def tr_ui(self):
        self.setWindowTitle(tr("AppSettings", "Settings"))
        self.tabsSettings.setTabText(self.tabsSettings.indexOf(self.general_tab),
                                     tr("AppSettings", "General settings"))
        self.tabsSettings.setTabText(self.tabsSettings.indexOf(self.units_tab), tr("AppSettings", "Units"))

        self.general_tab.locale.setItemText(0, tr("AppSettings", "English"))
        self.general_tab.locale.setItemText(1, tr("AppSettings", "Українська"))
