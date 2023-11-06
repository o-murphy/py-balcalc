from PySide6 import QtWidgets, QtCore
from py_ballisticcalc import Unit

from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr
from py_balcalc.ui.main_window.data_worker import DataWorker
from py_balcalc.ui.main_window.profile_a7p_meta import ProfileA7PMeta
from py_balcalc.ui.main_window.profile_weapon import ProfileWeapon
from py_balcalc.ui.main_window.profile_cartridge import ProfileCartridge
from py_balcalc.ui.main_window.profile_bullet import ProfileBullet
import a7p


class ProfileWizard(QtWidgets.QDialog, DataWorker):
    onAccepted = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

        self._profile = a7p.Profile()

        self.next_btn.clicked.connect(self.next_screen)
        self.back_btn.clicked.connect(self.prev_screen)
        self.cancel_btn.clicked.connect(self.reject)

        self.__post_init__()

    def __post_init__(self):
        """
        updates inner widgets data with selected profile data
        enables/disables inner tabs if profile type is correct
        """

        self.weapon.profile_name.setText(self._profile.profile_name)
        self.weapon.caliber.setText(self._profile.caliber)
        self.weapon.tileTop.setText(self._profile.short_name_top)
        self.weapon.rightTwist.setChecked(self._profile.twist_dir == 0)
        self.cartridge.cartridge_name.setText(self._profile.cartridge_name)
        self.bullet.bullet_name.setText(self._profile.bullet_name)

        if not self._profile.short_name_top:
            self.weapon.auto_tile()

        self._update_values()

        appSignalMgr.settings_units_updated.connect(self._update_values)

    def _update_values(self):
        super()._update_values()
        self.a7p_meta.distances.load_data(
            [Unit.METER(d) for d in a7p.A7PFactory.DistanceTable.MEDIUM_RANGE.value]
        )

    def next_screen(self):
        index = self.stacked.currentIndex()
        if index == self.stacked.count() - 2:
            self.next_btn.setText("Accept")
        if index < self.stacked.count():
            self.stacked.setCurrentIndex(index + 1)
        if index == self.stacked.count() - 1:
            # self.accept()
            self.onAccepted.emit()

    def prev_screen(self):
        index = self.stacked.currentIndex()
        if index > 0:
            self.stacked.setCurrentIndex(index - 1)
            self.next_btn.setText("Next")

    def init_ui(self):
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
        self.a7p_meta = ProfileA7PMeta(self)

        self.stacked.insertWidget(0, self.weapon)
        self.stacked.insertWidget(1, self.cartridge)
        self.stacked.insertWidget(2, self.bullet)
        self.stacked.insertWidget(3, self.a7p_meta)

        self.tr_ui()
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        self.next_btn.setText(tr("wizard", "Next"))
        self.back_btn.setText(tr("wizard", "Back"))
        self.cancel_btn.setText(tr("wizard", "Cancel"))
