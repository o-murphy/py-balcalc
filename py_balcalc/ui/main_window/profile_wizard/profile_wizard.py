from PySide6 import QtWidgets
from py_ballisticcalc import Unit

from py_balcalc.signals_manager import appSignalMgr
from ..profile_tab.profile_weapon import ProfileWeapon
from ..profile_tab.profile_cartridge import ProfileCartridge
from ..profile_tab.profile_bullet import ProfileBullet
import a7p


class ProfileWizard(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

        self._profile = a7p.Profile()

        self.next_btn.clicked.connect(self.next_screen)
        self.back_btn.clicked.connect(self.prev_screen)
        self.cancel_btn.clicked.connect(self.reject)

        self.__post_init__()

    def setupUi(self):
        self.setObjectName("ProfileWizard")
        self.setWindowTitle("Profile Wizard")
        self.layout = QtWidgets.QVBoxLayout(self)

        self.stacked = QtWidgets.QStackedWidget(self)
        self.next_btn = QtWidgets.QPushButton("Next", self)
        self.back_btn = QtWidgets.QPushButton("Back", self)
        self.cancel_btn = QtWidgets.QPushButton("Cancel", self)

        self.layout.addWidget(self.stacked)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.buttons_layout)

        self.buttons_layout.addWidget(self.back_btn)
        self.buttons_layout.addWidget(self.next_btn)
        self.buttons_layout.addWidget(self.cancel_btn)

        self.weapon = ProfileWeapon(self)
        self.cartridge = ProfileCartridge(self)
        self.bullet = ProfileBullet(self)

        self.stacked.insertWidget(0, self.weapon)
        self.stacked.insertWidget(1, self.cartridge)
        self.stacked.insertWidget(2, self.bullet)

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

    def export_a7p(self):
        # TODO: store data to new a7p payload
        self._profile.profile_name = self.weapon.rifleName.text()
        self._profile.cartridge_name = self.weapon.caliberName.text()
        self._profile.short_name_top = self.weapon.caliberShort.text()
        self._profile.r_twist = int(self.weapon.twist.raw_value() >> Unit.INCH) * 100
        self._profile.sc_height = int(self.weapon.sh.raw_value() >> Unit.MILLIMETER)
        self._profile.twist_dir = 1 if self.weapon.rightTwist.isChecked() else 0
        return a7p.Payload(profile=self._profile)

    def _update_values(self):
        self.weapon.sh.set_raw_value(Unit.MILLIMETER(self._profile.sc_height))
        self.weapon.twist.set_raw_value(Unit.INCH(self._profile.r_twist / 100))

        self.cartridge.mv.set_raw_value(Unit.MPS(self._profile.c_muzzle_velocity / 10))
        self.cartridge.temp.set_raw_value(Unit.CELSIUS(self._profile.c_zero_temperature))
        self.cartridge.ts.setValue(self._profile.c_t_coeff / 1000)

        self.bullet.weight.set_raw_value(Unit.GRAIN(self._profile.b_weight / 10))
        self.bullet.length.set_raw_value(Unit.INCH(self._profile.b_length / 1000))
        self.bullet.diameter.set_raw_value(Unit.INCH(self._profile.b_diameter / 1000))

    def next_screen(self):
        index = self.stacked.currentIndex()
        if index == 1:
            self.next_btn.setText("Accept")
        if index < self.stacked.count():
            self.stacked.setCurrentIndex(index + 1)
        if index == 2:
            self.accept()

    def prev_screen(self):
        index = self.stacked.currentIndex()
        if index > 0:
            self.stacked.setCurrentIndex(index - 1)
            self.next_btn.setText("Next")
