from PySide6 import QtCore, QtGui, QtWidgets

# from modules import BConverter

from .ui import Ui_profileCurrent
from .profile_weapon import ProfileWeapon
from .profile_cartridge import ProfileCartridge
from .profile_bullet import ProfileBullet
from .profile_conditions import ProfileConditions
# from ..bc_table import BCTable
# from ..add_button import AddButton
from py_balcalc.profile import Profile


class ProfileCurrent(QtWidgets.QWidget, Ui_profileCurrent):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._profile = None
        # self.convert = BConverter()
        # self.bc_table = BCTable()
        #
        self.weapon = ProfileWeapon(self)
        self.cartridge = ProfileCartridge(self)
        self.bullet = ProfileBullet(self)
        self.conditions = ProfileConditions(self)

        self.bullet.layout().setAlignment(QtCore.Qt.AlignTop)

        self.munition_tab.layout().setAlignment(QtCore.Qt.AlignTop)
        self.conditions_tab.layout().setAlignment(QtCore.Qt.AlignTop)

        self.munition_tab.layout().addWidget(self.weapon, 0, 0, 1, 1)
        self.munition_tab.layout().addWidget(self.cartridge, 1, 0, 1, 1)
        self.munition_tab.layout().addWidget(self.bullet, 0, 1, 2, 1)
        self.conditions_tab.layout().addWidget(self.conditions, 0, 0, 1, 1)

    def set_current(self, payload):
        """
        updates inner widgets data with selected profile data
        enables/disables inner tabs if profile type is correct
        """

        self._profile = Profile(self)
        self._profile.set(payload)

        self.weapon.set_current(self._profile)
        self.cartridge.set_current(self._profile)
        self.bullet.set_current(self._profile)
        self.conditions.set_current(self._profile)
