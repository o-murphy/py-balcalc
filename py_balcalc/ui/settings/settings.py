# -*u.- coding: utf-8 -*u.-

from configparser import ConfigParser
import os
from pathlib import Path

from PySide6 import QtCore, QtWidgets, QtGui
from py_ballisticcalc.unit import *
from py_ballisticcalc import Settings as CalcSettings

from .ui import Ui_AppSettings


DistanceUnits = [value for key, value in Distance.__dict__.items() if isinstance(value, Unit)]
VelocityUnits = [value for key, value in Velocity.__dict__.items() if isinstance(value, Unit)]
TemperatureUnits = [value for key, value in Temperature.__dict__.items() if isinstance(value, Unit)]
PressureUnits = [value for key, value in Pressure.__dict__.items() if isinstance(value, Unit)]
EnergyUnits = [value for key, value in Energy.__dict__.items() if isinstance(value, Unit)]
AngularUnits = [value for key, value in Angular.__dict__.items() if isinstance(value, Unit)]
WeightUnits = [value for key, value in Weight.__dict__.items() if isinstance(value, Unit)]


# loads, writes and sets app preferences from settings.ini file
class AppSettings(QtWidgets.QDialog, Ui_AppSettings):
    def __init__(self):
        super(AppSettings, self).__init__()
        self.setupUi(self)

        self.config = ConfigParser()
        # self.config.read(CONFIG_PATH)

        # recreate settings.ini if it's format wrong
        try:
            self.update_config()
        except Exception:
            # os.remove(CONFIG_PATH)
            self.update_config()

    def update_config(self):
        """loads all settings to current widget"""
        self.init_general_tab()
        self.init_units_tab()

        self.load_general_settings()
        self.load_unit_settings()

        self.init_extension_tab()
        self.load_extension_settings()

        self.tabSettings.setCurrentIndex(1)

        self.save_cfg()

    def save_cfg(self):
        # with open(CONFIG_PATH, 'w') as fp:
        #     self.config.write(fp)
        ...

    def init_general_tab(self):
        """creates general settings tab, loads settings or sets it to default values"""
        self.languages = ['en', 'ua', 'ru']
        for i, lang in enumerate(self.languages):
            self.Language.setItemData(i, lang)

        if 'General' not in self.config:
            self.config.add_section('General')
            self.config.set('General', 'exp_dfed', '0')
        self.xdfed.setChecked(self.config.getboolean('General', 'exp_dfed'))


    def init_extension_tab(self):
        """creates extension settings tab, loads settings or sets it to default values"""

        root = Path(__file__).parent.parent
        edir = Path(root, 'extensions')
        if not os.path.exists(edir):
            return

        if 'Extensions' not in self.config:
            self.config.add_section('Extensions')

        for each in edir.iterdir():
            if each.is_dir() and not str(each.name).startswith('__'):
                ext_name = f'extensions.{each.name}'
                if ext_name not in self.config['Extensions']:
                    self.config.set('Extensions', ext_name, str(True))

    def load_extension_settings(self):
        """loads which extensions are enabled"""
        root = Path(__file__).parent.parent
        edir = Path(root, 'extensions')
        if not os.path.exists(edir):
            return

        layout = self.tabExtensions.layout()
        layout.setAlignment(QtCore.Qt.AlignTop)

        for i, (k, v) in enumerate(self.config['Extensions'].items()):
            text = k.replace('extensions.', '').replace('_', ' ').capitalize()
            cb = QtWidgets.QCheckBox()
            cb.setText(text)
            cb.setObjectName(k)
            is_checked = self.config['Extensions'].getboolean(k)
            cb.setChecked(is_checked)
            layout.addWidget(cb, i, 0, 1, 1)

    def init_units_tab(self):
        """
        creates extension _cur_units tab, loads settings or sets it to default values
        that will be used globally in the app and a ballistics calculations
        """

        [self.shUnits.addItem(i.key, userData=i) for i in DistanceUnits]
        [self.twistUnits.addItem(i.key, userData=i) for i in DistanceUnits]
        [self.vUnits.addItem(i.key, userData=i) for i in VelocityUnits]
        [self.distUnits.addItem(i.key, userData=i) for i in DistanceUnits]
        [self.dUnits.addItem(i.key, userData=i) for i in DistanceUnits]
        [self.lnUnits.addItem(i.key, userData=i) for i in DistanceUnits]
        [self.tempUnits.addItem(i.key, userData=i) for i in TemperatureUnits]
        [self.wUnits.addItem(i.key, userData=i) for i in WeightUnits]
        [self.eUnits.addItem(i.key, userData=i) for i in EnergyUnits]
        [self.dropUnits.addItem(i.key, userData=i) for i in DistanceUnits]
        [self.pathUnits.addItem(i.key, userData=i) for i in AngularUnits]
        [self.angleUnits.addItem(i.key, userData=i) for i in AngularUnits]
        [self.pUnits.addItem(i.key, userData=i) for i in PressureUnits]
        [self.thUnits.addItem(i.key, userData=i) for i in DistanceUnits]
        [self.ogwUnits.addItem(i.key, userData=i) for i in WeightUnits]

        self.shUnits.setCurrentIndex(self.shUnits.findData(CalcSettings.Units.sight_height))
        self.twistUnits.setCurrentIndex(self.twistUnits.findData(CalcSettings.Units.twist))
        self.vUnits.setCurrentIndex(self.vUnits.findData(CalcSettings.Units.velocity))
        self.distUnits.setCurrentIndex(self.distUnits.findData(CalcSettings.Units.distance))
        self.dUnits.setCurrentIndex(self.dUnits.findData(CalcSettings.Units.diameter))
        self.lnUnits.setCurrentIndex(self.lnUnits.findData(CalcSettings.Units.length))
        self.tempUnits.setCurrentIndex(self.tempUnits.findData(CalcSettings.Units.temperature))
        self.wUnits.setCurrentIndex(self.wUnits.findData(CalcSettings.Units.weight))
        self.eUnits.setCurrentIndex(self.eUnits.findData(CalcSettings.Units.energy))
        self.dropUnits.setCurrentIndex(self.dropUnits.findData(CalcSettings.Units.drop))
        self.pathUnits.setCurrentIndex(self.pathUnits.findData(CalcSettings.Units.adjustment))
        self.angleUnits.setCurrentIndex(self.angleUnits.findData(CalcSettings.Units.angular))
        self.pUnits.setCurrentIndex(self.pUnits.findData(CalcSettings.Units.pressure))
        self.thUnits.setCurrentIndex(self.thUnits.findData(CalcSettings.Units.target_height))
        self.ogwUnits.setCurrentIndex(self.ogwUnits.findData(CalcSettings.Units.ogw))

    def load_general_settings(self):
        """loads last general settings from settings.ini"""

        if 'Locale' in self.config:
            locale = self.config['Locale']['current']
            self.Language.setCurrentIndex(self.languages.index(locale))
        else:
            self.save_language_settings()

        if 'General' in self.config:
            exp_dfed = self.config.getboolean('General', 'exp_dfed')
            self.xdfed.setChecked(exp_dfed)
        else:
            self.save_exp_dfed()

    def load_unit_settings(self):
        """loads last unit settings from settings.ini"""

        widgets = self.tabUnits.findChildren(QtWidgets.QComboBox)
        if 'Units' in self.config:
            for i in self.config['Units']:
                for w in widgets:
                    if i == w.objectName().lower():
                        w.setCurrentIndex(w.findData(self.config['Units'][i]))
        else:
            self.save_units_settings()

    def save_exp_dfed(self):
        """
        saves to settings.ini if it's enabled experimental
        drag function editor ballistics calculation API here
        """

        exp_dfed = self.xdfed.isChecked()
        if not 'General' in self.config:
            self.config.add_section('General')
        self.config.set('General', 'exp_dfed', str(exp_dfed))

    def save_language_settings(self):
        """saves language settings to settings.ini"""

        locale = self.Language.currentData()
        # config = configparser.ConfigParser()
        # config.read(CONFIG_PATH)

        if 'Locale' not in self.config:
            self.config.add_section('Locale')

        self.config.set('Locale', 'system', QtCore.QLocale.system().name().split('_')[1].lower())
        if locale != 'en':
            if os.path.isfile(f'translate/eng-{locale}.qm'):
                self.config.set('Locale', 'current', locale)
            else:
                locale = self.config['Locale']['system']
                self.config.set('Locale', 'current', locale)
        else:
            self.config.set('Locale', 'current', locale)

    def save_units_settings(self):
        """saves _cur_units settings to settings.ini"""

        # config = configparser.ConfigParser()
        # config.read(CONFIG_PATH)
        # if 'Units' not in self.config:
        #     self.config.add_section('Units')
        # for w in self.tabUnits.findChildren(QtWidgets.QComboBox):
        #     self.config.set('Units', w.objectName(), str(w.currentData()))

    def save_extensions_settings(self):
        """saves which extensions are enabled to settings.ini"""

        # config = configparser.ConfigParser()
        # config.read(CONFIG_PATH)
        children = self.tabExtensions.findChildren(QtWidgets.QCheckBox)
        for ch in children:
            self.config.set('Extensions', ch.objectName(), str(ch.isChecked()))

    def accept(self) -> None:
        self.save_language_settings()
        self.save_exp_dfed()
        self.save_units_settings()
        self.save_extensions_settings()
        self.save_cfg()
        super().accept()

    def retranslateUi(self, AppSettings):
        super().retranslateUi(AppSettings)
        _translate = QtCore.QCoreApplication.translate
