from PySide6 import QtCore, QtGui, QtWidgets

# from modules import BConverter
# from .add_btn import AddBtn
# from .profile_item_contents import Bullet, Rifle, Cartridge, Conditions
from .ui import Ui_profileCurrent
# from ..bc_table import BCTable


class ProfileCurrent(QtWidgets.QWidget, Ui_profileCurrent):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # self.convert = BConverter()
        # self.bc_table = BCTable()
        #
        # self.rifle = Rifle(self)
        # self.cartridge = Cartridge(self)
        # self.bullet = Bullet(self)
        # self.conditions = Conditions(self)

        self.tab_6.layout().setAlignment(QtCore.Qt.AlignTop)
        self.tab_7.layout().setAlignment(QtCore.Qt.AlignTop)

        # self.tab_6.layout().addWidget(self.rifle, 0, 0, 1, 1)
        # self.tab_6.layout().addWidget(self.cartridge, 1, 0, 1, 1)
        # self.tab_6.layout().addWidget(self.bullet, 2, 0, 1, 1)
        # self.tab_7.layout().addWidget(self.conditions, 0, 0, 1, 1)

    def set_current(self, profile):
        """
        updates inner widgets data with selected profile data
        enables/disables inner tabs if profile type is correct
        """
        # if isinstance(profile, AddBtn):
        #     self.tab_6.setDisabled(True)
        #     self.tab_7.setDisabled(True)
        #     return
        #
        # if not profile:
        #     self.tab_6.setDisabled(True)
        #     self.tab_7.setDisabled(True)
        #     return
        #
        # self.tab_6.setEnabled(True)
        # self.tab_7.setEnabled(True)
        #
        # self.rifle.set_current(profile)
        # self.cartridge.set_current(profile)
        # self.bullet.set_current(profile)
        # self.conditions.set_current(profile)
        ...
