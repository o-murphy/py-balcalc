from PySide6 import QtCore, QtWidgets, QtGui
from py_ballisticcalc.unit import *

from py_balcalc.settings import app_settings
from py_balcalc.signals_manager import appSignalMgr
from .units_tab import UnitsTab
from .general_tab import GeneralTab


DistanceUnits = [value for key, value in Distance.__dict__.items() if isinstance(value, Unit)]
VelocityUnits = [value for key, value in Velocity.__dict__.items() if isinstance(value, Unit)]
TemperatureUnits = [value for key, value in Temperature.__dict__.items() if isinstance(value, Unit)]
PressureUnits = [value for key, value in Pressure.__dict__.items() if isinstance(value, Unit)]
EnergyUnits = [value for key, value in Energy.__dict__.items() if isinstance(value, Unit)]
AngularUnits = [value for key, value in Angular.__dict__.items() if isinstance(value, Unit)]
WeightUnits = [value for key, value in Weight.__dict__.items() if isinstance(value, Unit)]


class AppSettings(QtWidgets.QDialog):
    """loads, writes and sets app preferences from settings.ini file"""

    def __init__(self):
        super(AppSettings, self).__init__()
        self.setup_ui(self)

        self.init_general_tab()
        self.init_units_tab()
        self.tabsSettings.setCurrentIndex(0)

    def init_general_tab(self):
        # Todo load list of languages

        for lang in ['us', 'ua']:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(f":/flags/{lang}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

            [combo_box.addItem(i.key, userData=i) for i in items]
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

    def accept(self) -> None:
        super().accept()

    def setup_ui(self, AppSettings):
        AppSettings.setObjectName("AppSettings")
        AppSettings.resize(328, 424)

        self.gridLayout = QtWidgets.QGridLayout(AppSettings)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(AppSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1, QtCore.Qt.AlignBottom)

        self.tabsSettings = QtWidgets.QTabWidget(AppSettings)
        self.tabsSettings.setObjectName("tabsSettings")

        self.general_tab = GeneralTab(self)
        self.tabsSettings.addTab(self.general_tab, "")

        self.units_tab = UnitsTab(self)
        self.tabsSettings.addTab(self.units_tab, "")

        self.gridLayout.addWidget(self.tabsSettings, 0, 0, 1, 1, QtCore.Qt.AlignTop)

        self.buttonBox.accepted.connect(AppSettings.accept)  # type: ignore
        self.buttonBox.rejected.connect(AppSettings.reject)  # type: ignore

        self.retranslate_ui()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AppSettings", "Settings"))
        self.tabsSettings.setTabText(self.tabsSettings.indexOf(self.general_tab),
                                     _translate("AppSettings", "General settings"))
        self.tabsSettings.setTabText(self.tabsSettings.indexOf(self.units_tab), _translate("AppSettings", "Units"))

        self.general_tab.locale.setItemText(0, _translate("AppSettings", "English"))
        self.general_tab.locale.setItemText(1, _translate("AppSettings", "Українська"))
