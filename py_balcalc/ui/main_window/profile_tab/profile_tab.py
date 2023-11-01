from PySide6 import QtCore, QtWidgets

from py_ballisticcalc import Unit

from py_balcalc.signals_manager import appSignalMgr
from .ui import Ui_profileCurrent
from .profile_weapon import ProfileWeapon
from .profile_cartridge import ProfileCartridge
from .profile_bullet import ProfileBullet
from .profile_conditions import ProfileConditions


class ProfileTab(QtWidgets.QWidget, Ui_profileCurrent):
    def __init__(self, parent=None, payload=None):
        super().__init__(parent)
        self.weapon = ProfileWeapon(self)
        self.cartridge = ProfileCartridge(self)
        self.bullet = ProfileBullet(self)
        self.conditions = ProfileConditions(self)
        self.setupUi(self)

        self._profile = payload.profile
        self.__post_init__()

    def setupUi(self, profileCurrent):
        super(ProfileTab, self).setupUi(profileCurrent)
        self.bullet.layout().setAlignment(QtCore.Qt.AlignTop)
        self.munition_tab.layout().setAlignment(QtCore.Qt.AlignTop)
        self.conditions_tab.layout().setAlignment(QtCore.Qt.AlignTop)
        self.munition_tab.layout().addWidget(self.weapon, 0, 0, 1, 1)
        self.munition_tab.layout().addWidget(self.cartridge, 1, 0, 1, 1)
        self.munition_tab.layout().addWidget(self.bullet, 0, 1, 2, 1)
        self.conditions_tab.layout().addWidget(self.conditions, 0, 0, 1, 1)

    def __post_init__(self):
        """
        updates inner widgets data with selected profile data
        enables/disables inner tabs if profile type is correct
        """

        self.weapon.rifleName.setText(self._profile.profile_name)
        self.weapon.caliberName.setText(self._profile.caliber)
        self.weapon.caliberShort.setText(self._profile.short_name_top)
        self.weapon.rightTwist.setChecked(self._profile.twist_dir == 0)
        self.cartridge.cartridgeName.setText(self._profile.cartridge_name)
        self.bullet.bulletName.setText(self._profile.bullet_name)

        if not self._profile.short_name_top:
            self.weapon.auto_tile()

        self._update_values()
        appSignalMgr.appSettingsUpdated.connect(self._update_values)

    def _update_values(self):
        self.weapon.sh.set_raw_value(Unit.MILLIMETER(self._profile.sc_height))
        self.weapon.twist.set_raw_value(Unit.INCH(self._profile.r_twist / 100))

        self.cartridge.mv.set_raw_value(Unit.MPS(self._profile.c_muzzle_velocity / 10))
        self.cartridge.temp.set_raw_value(Unit.CELSIUS(self._profile.c_zero_temperature))
        self.cartridge.ts.setValue(self._profile.c_t_coeff / 1000)

        self.bullet.weight.set_raw_value(Unit.GRAIN(self._profile.b_weight / 10))
        self.bullet.length.set_raw_value(Unit.INCH(self._profile.b_length / 1000))
        self.bullet.diameter.set_raw_value(Unit.INCH(self._profile.b_diameter / 1000))

        self.conditions.z_pressure.set_raw_value(Unit.HP(self._profile.c_zero_air_pressure / 10))
        self.conditions.z_temp.set_raw_value(Unit.CELSIUS(self._profile.c_zero_temperature))
        self.conditions.z_powder_temp.set_raw_value(Unit.CELSIUS(self._profile.c_zero_p_temperature))
        self.conditions.z_angle.set_raw_value(Unit.DEGREE(self._profile.c_zero_w_pitch))
        self.conditions.z_humidity.setValue(self._profile.c_zero_air_humidity)

        # self.z_azimuth.set_raw_value(Unit.DEGREE(data['z_azimuth']))
        # self.z_latitude.set_raw_value(Angular(data['z_latitude'], AngularDegree))
