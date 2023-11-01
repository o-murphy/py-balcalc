from re import search

from PySide6 import QtWidgets, QtCore, QtGui

from .ui import Ui_weapon
import qtawesome as qta


class ProfileWeapon(QtWidgets.QWidget, Ui_weapon):
    """shows selected profile weapon property"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.auto_tile_mode = 0
        self.setupUi(self)

    def setupUi(self, weapon):
        super().setupUi(weapon)
        self.rifleGroupBox.setCheckable(False)
        self.rifleGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)
        self.auto_tile_act = QtGui.QAction(
            qta.icon('mdi6.autorenew', color='white', color_active='orange', color_disabled='grey'),
            'Auto'
        )
        self.caliberShort.addAction(self.auto_tile_act, QtWidgets.QLineEdit.TrailingPosition)
        self.auto_tile_act.triggered.connect(self.auto_tile)

    def retranslateUi(self, weapon):
        _translate = QtCore.QCoreApplication.translate
        self.caliberShort.setPlaceholderText(_translate("weapon", 'Tile text:'))
        super().retranslateUi(weapon)

    def auto_tile(self):
        """changes current auto tile creation mode"""
        if self.auto_tile_mode == 1:
            self.auto_tile_1()
        else:
            self.auto_tile_0()

    def auto_tile_1(self):
        """ auto update caliberShort text with mode 1"""
        self.caliberShort.setText(self.caliberName.text().replace(' ', '').strip()[:7])
        self.auto_tile_mode = 0

    def auto_tile_0(self):
        """ auto update caliberShort text with mode 0"""
        reg = search(r'\.+\d+', self.caliberName.text())
        cal = reg.group() if reg else ''
        tile = ''.join((list(filter(lambda char: char.isupper(), self.caliberName.text()))))
        # self.caliberShort.setText(f'{cal + tile}'[:7])
        self.caliberShort.setText(f'{cal + tile}'[:7])
        self.auto_tile_mode = 1
