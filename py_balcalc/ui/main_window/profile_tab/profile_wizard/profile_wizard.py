from PySide6 import QtWidgets

from ..profile_current.profile_weapon import ProfileWeapon
from ..profile_current.profile_cartridge import ProfileCartridge
from ..profile_current.profile_bullet import ProfileBullet


class ProfileWizard(QtWidgets.QDialog):
    def __init__(self, parent=None, profile=None):
        super().__init__(parent)
        self.setupUi()

        self.profile = profile

        self.rifle.set_current(self.profile)
        self.cartridge.set_current(self.profile)
        self.bullet.set_current(self.profile)

        self.next_btn.clicked.connect(self.next_screen)
        self.back_btn.clicked.connect(self.prev_screen)
        self.cancel_btn.clicked.connect(self.reject)

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

        self.rifle = ProfileWeapon(self)
        self.cartridge = ProfileCartridge(self)
        self.bullet = ProfileBullet(self)

        self.stacked.insertWidget(0, self.rifle)
        self.stacked.insertWidget(1, self.cartridge)
        self.stacked.insertWidget(2, self.bullet)

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
