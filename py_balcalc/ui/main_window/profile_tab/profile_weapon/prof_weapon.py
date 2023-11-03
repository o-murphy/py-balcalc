from re import search

from PySide6 import QtWidgets, QtCore, QtGui
from py_ballisticcalc import Unit

from py_balcalc.settings import DEF_STRINGS_LIMITS
from py_balcalc.ui.custom_widgets import TLabel, UnitSpinBox
import qtawesome as qta


class ProfileWeapon(QtWidgets.QGroupBox):
    """shows selected profile weapon property"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.auto_tile_mode = 0

        self.setup_ui(self)
        self.__post_init__()
        
    def __post_init__(self):
        self.rifleName.setMaxLength(DEF_STRINGS_LIMITS['profile_name'])
        self.tileTop.setMaxLength(DEF_STRINGS_LIMITS['short_name_top'])
        self.caliberName.setMaxLength(DEF_STRINGS_LIMITS['caliber'])

        self.auto_tile_act.triggered.connect(self.auto_tile)
        self.tile_help.triggered.connect(self.show_tile_help)

    def retranslate_ui(self, weapon):
        _translate = QtCore.QCoreApplication.translate
        self.tileTop.setPlaceholderText(_translate("weapon", 'Tile text:'))

    def show_tile_help(self):
        # TODO:
        ...

    def auto_tile(self):
        """changes current auto tile creation mode"""
        if self.auto_tile_mode == 1:
            self.tileTop.setText(self.caliberName.text().replace(' ', '').strip()[:7])
            self.auto_tile_mode = 0
        else:
            reg = search(r'\.+\d+', self.caliberName.text())
            cal = reg.group() if reg else ''
            tile = ''.join((list(filter(lambda char: char.isupper(), self.caliberName.text()))))
            # self.caliberShort.setText(f'{cal + tile}'[:7])
            self.tileTop.setText(f'{cal + tile}'[:7])
            self.auto_tile_mode = 1

    def setup_ui(self, weapon):
        weapon.setObjectName("ProfileWeapon")
        weapon.setCheckable(True)

        self.gridLayout = QtWidgets.QGridLayout(weapon)
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.gridLayout.addWidget(TLabel('Name:'), 0, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Caliber:'), 1, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Tile top:'), 2, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Sight height:'), 3, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Twist:'), 4, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Zeroing distance:'), 5, 0, 1, 1)


        self.twist = UnitSpinBox(weapon, Unit.INCH(10), 'unit/twist')
        self.sh = UnitSpinBox(weapon, Unit.MILLIMETER(90), 'unit/sight_height')
        self.zero_dist = UnitSpinBox(weapon, Unit.METER(100), 'unit/distance')
        self.zero_dist.setMaximum(1500)

        self.twist.setObjectName("twist")
        self.sh.setObjectName("sight_height")
        self.sh.setObjectName("zero_dist")

        self.rightTwist = QtWidgets.QRadioButton(weapon)
        self.caliberName = QtWidgets.QLineEdit(weapon)
        self.tileTop = QtWidgets.QLineEdit(weapon)

        self.rightTwist.setEnabled(True)
        self.rightTwist.setChecked(True)
        self.rightTwist.setObjectName("rightTwist")
        self.leftTwist = QtWidgets.QRadioButton(weapon)
        self.leftTwist.setObjectName("leftTwist")
        # self.caliberName.setMaxLength(20)
        self.caliberName.setObjectName("caliberName")
        self.tileTop.setMinimumSize(QtCore.QSize(0, 0))
        self.tileTop.setMaxLength(8)
        self.tileTop.setObjectName("caliberShort")

        self.rifleName = QtWidgets.QLineEdit(weapon)
        # self.rifleName.setMaxLength(20)
        self.rifleName.setFrame(True)
        self.rifleName.setObjectName("rifleName")

        self.gridLayout.addWidget(self.rifleName, 0, 1, 1, 4)
        self.gridLayout.addWidget(self.caliberName, 1, 1, 1, 3)
        self.gridLayout.addWidget(self.tileTop, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.sh, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.twist, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.zero_dist, 5, 1, 1, 1)


        self.gridLayout.addWidget(self.rightTwist, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.leftTwist, 4, 3, 1, 1)

        self.auto_tile_act = QtGui.QAction(
            qta.icon(
                'mdi6.autorenew', color='white', color_active='orange', color_disabled='grey'
            ), 'Auto')
        self.tile_help = QtGui.QAction(
            qta.icon(
                'mdi6.help', color='white', color_active='orange', color_disabled='grey'
            ), 'Help')
        self.tileTop.addAction(self.tile_help, QtWidgets.QLineEdit.TrailingPosition)
        self.tileTop.addAction(self.auto_tile_act, QtWidgets.QLineEdit.TrailingPosition)

        self.retranslate_ui(weapon)

    def retranslate_ui(self, weapon):
        _translate = QtCore.QCoreApplication.translate
        weapon.setTitle(_translate("weapon", "Weapon"))
        self.rightTwist.setText(_translate("weapon", "Right"))
        self.leftTwist.setText(_translate("weapon", "Left"))
