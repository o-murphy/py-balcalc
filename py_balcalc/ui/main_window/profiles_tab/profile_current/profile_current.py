from PySide6 import QtCore, QtGui, QtWidgets

# from modules import BConverter
# from .add_btn import AddBtn
# from .profile_item_contents import Bullet, Rifle, Cartridge, Conditions
from .ui import Ui_profileCurrent
from .profile_weapon import ProfileWeapon
from .profile_cartridge import ProfileCartridge
from .profile_bullet import ProfileBullet
from .profile_conditions import ProfileConditions
# from ..bc_table import BCTable
from ..add_button import AddButton


class ProfileCurrent(QtWidgets.QWidget, Ui_profileCurrent):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # self.convert = BConverter()
        # self.bc_table = BCTable()
        #
        self.weapon = ProfileWeapon(self)
        self.cartridge = ProfileCartridge(self)
        self.bullet = ProfileBullet(self)
        self.conditions = ProfileConditions(self)

        self.munition_tab.layout().setAlignment(QtCore.Qt.AlignTop)
        self.conditions_tab.layout().setAlignment(QtCore.Qt.AlignTop)

        self.munition_tab.layout().addWidget(self.weapon, 0, 0, 1, 1)
        self.munition_tab.layout().addWidget(self.cartridge, 1, 0, 1, 1)
        self.munition_tab.layout().addWidget(self.bullet, 2, 0, 1, 1)
        self.conditions_tab.layout().addWidget(self.conditions, 0, 0, 1, 1)

    def set_current(self, profile):
        """
        updates inner widgets data with selected profile data
        enables/disables inner tabs if profile type is correct
        """
        print(profile)
        if isinstance(profile, AddButton):
            self.munition_tab.setDisabled(True)
            self.conditions_tab.setDisabled(True)
            return

        if not profile:
            self.munition_tab.setDisabled(True)
            self.conditions_tab.setDisabled(True)
            return

        self.munition_tab.setEnabled(True)
        self.conditions_tab.setEnabled(True)

        self.weapon.set_current(profile)
        self.cartridge.set_current(profile)
        self.bullet.set_current(profile)
        self.conditions.set_current(profile)
