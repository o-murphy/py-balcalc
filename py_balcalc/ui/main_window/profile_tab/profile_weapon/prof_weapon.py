from re import search

from PySide6 import QtWidgets, QtCore, QtGui
from py_ballisticcalc import Unit

from py_balcalc.ui.custom_widgets import TLabel, UnitSpinBox
import qtawesome as qta


class ProfileWeapon(QtWidgets.QGroupBox):
    """shows selected profile weapon property"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.auto_tile_mode = 0

        self.setupUi(self)
        self.auto_tile_act.triggered.connect(self.auto_tile)

    def retranslateUi(self, weapon):
        _translate = QtCore.QCoreApplication.translate
        self.caliberShort.setPlaceholderText(_translate("weapon", 'Tile text:'))
        super().retranslateUi(weapon)

    def auto_tile(self):
        """changes current auto tile creation mode"""
        if self.auto_tile_mode == 1:
            self.caliberShort.setText(self.caliberName.text().replace(' ', '').strip()[:7])
            self.auto_tile_mode = 0
        else:
            reg = search(r'\.+\d+', self.caliberName.text())
            cal = reg.group() if reg else ''
            tile = ''.join((list(filter(lambda char: char.isupper(), self.caliberName.text()))))
            # self.caliberShort.setText(f'{cal + tile}'[:7])
            self.caliberShort.setText(f'{cal + tile}'[:7])
            self.auto_tile_mode = 1

    def setupUi(self, weapon):
        weapon.setObjectName("weapon")
        weapon.setCheckable(False)

        self.gridLayout = QtWidgets.QGridLayout(weapon)
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.gridLayout.addWidget(TLabel('Name:'), 0, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Caliber:'), 1, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Sight height:'), 2, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Twist:'), 3, 0, 1, 1)

        self.twist = UnitSpinBox(weapon, Unit.INCH(10), 'unit/twist')
        self.sh = UnitSpinBox(weapon, Unit.CENTIMETER(9), 'unit/sight_height')

        self.twist.setObjectName("twist")
        self.sh.setObjectName("sight_height")

        self.rightTwist = QtWidgets.QRadioButton(weapon)
        self.rightTwist.setEnabled(True)
        self.rightTwist.setChecked(True)
        self.rightTwist.setObjectName("rightTwist")
        self.leftTwist = QtWidgets.QRadioButton(weapon)
        self.leftTwist.setObjectName("leftTwist")
        self.caliberName = QtWidgets.QLineEdit(weapon)
        self.caliberName.setMaxLength(20)
        self.caliberName.setObjectName("caliberName")
        self.caliberShort = QtWidgets.QLineEdit(weapon)
        self.caliberShort.setMinimumSize(QtCore.QSize(0, 0))
        self.caliberShort.setMaxLength(8)
        self.caliberShort.setObjectName("caliberShort")
        self.rifleName = QtWidgets.QLineEdit(weapon)
        self.rifleName.setMaxLength(20)
        self.rifleName.setFrame(True)
        self.rifleName.setObjectName("rifleName")

        self.gridLayout.addWidget(self.rifleName, 0, 1, 1, 4)
        self.gridLayout.addWidget(self.caliberName, 1, 1, 1, 3)
        self.gridLayout.addWidget(self.sh, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.twist, 3, 1, 1, 1)

        self.gridLayout.addWidget(self.caliberShort, 1, 4, 1, 1)

        self.gridLayout.addWidget(self.rightTwist, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.leftTwist, 3, 3, 1, 1)

        self.auto_tile_act = QtGui.QAction(
            qta.icon(
                'mdi6.autorenew', color='white', color_active='orange', color_disabled='grey'
            ), 'Auto')
        self.caliberShort.addAction(self.auto_tile_act, QtWidgets.QLineEdit.TrailingPosition)

        self.retranslateUi(weapon)

    def retranslateUi(self, weapon):
        _translate = QtCore.QCoreApplication.translate
        weapon.setTitle(_translate("weapon", "Weapon"))
        self.rightTwist.setText(_translate("weapon", "Right"))
        self.leftTwist.setText(_translate("weapon", "Left"))
