from re import search

from PySide6 import QtWidgets, QtCore, QtGui
from py_ballisticcalc import Unit

from py_balcalc.settings import DEF_STRINGS_LIMITS
from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr
from py_balcalc.ui.custom_widgets import TLabel, UnitSpinBox, RegExpLineEdit
import qtawesome as qta


class ProfileWeapon(QtWidgets.QGroupBox):
    """shows selected profile weapon property"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.auto_tile_mode = 0

        self.init_ui()
        self.__post_init__()

    def __post_init__(self):
        self.profile_name.setMaxLength(DEF_STRINGS_LIMITS['profile_name'])
        self.tileTop.setMaxLength(DEF_STRINGS_LIMITS['short_name_top'])
        self.caliber.setMaxLength(DEF_STRINGS_LIMITS['caliber'])

        self.auto_tile_act.triggered.connect(self.auto_tile)
        self.tile_help.triggered.connect(self.show_tile_help)

    def show_tile_help(self):
        # TODO:
        ...

    def auto_tile(self):
        """changes current auto tile creation mode"""
        if self.auto_tile_mode == 1:
            self.tileTop.setText(self.caliber.text().replace(' ', '').strip()[:7])
            self.auto_tile_mode = 0
        else:
            reg = search(r'\.+\d+', self.caliber.text())
            cal = reg.group() if reg else ''
            tile = ''.join((list(filter(lambda char: char.isupper(), self.caliber.text()))))
            # self.caliberShort.setText(f'{cal + tile}'[:7])
            self.tileTop.setText(f'{cal + tile}'[:7])
            self.auto_tile_mode = 1

    def init_ui(self):
        self.setObjectName("ProfileWeapon")
        self.setCheckable(True)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.gridLayout.addWidget(TLabel('Name:'), 0, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Caliber:'), 1, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Tile top:'), 2, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Sight height:'), 3, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Twist:'), 4, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Zeroing distance:'), 5, 0, 1, 1)

        self.twist = UnitSpinBox(self, Unit.INCH(10), 'unit/twist')
        self.sh = UnitSpinBox(self, Unit.MILLIMETER(90), 'unit/sight_height')
        self.zero_dist = UnitSpinBox(self, Unit.METER(100), 'unit/distance')

        self.twist.setObjectName("twist")
        self.sh.setObjectName("sight_height")
        self.sh.setObjectName("zero_dist")

        self.rightTwist = QtWidgets.QRadioButton(self)
        self.caliber = QtWidgets.QLineEdit(self)
        self.tileTop = RegExpLineEdit(self, valid_regex=r'.+')

        self.rightTwist.setEnabled(True)
        self.rightTwist.setChecked(True)
        self.rightTwist.setObjectName("rightTwist")
        self.leftTwist = QtWidgets.QRadioButton(self)
        self.leftTwist.setObjectName("leftTwist")
        # self.caliber.setMaxLength(20)
        self.caliber.setObjectName("caliber")
        self.tileTop.setMinimumSize(QtCore.QSize(0, 0))
        self.tileTop.setMaxLength(8)
        self.tileTop.setObjectName("caliberShort")

        self.profile_name = RegExpLineEdit(self, valid_regex=r'.+')
        self.profile_name.setObjectName("profile_name")

        self.gridLayout.addWidget(self.profile_name, 0, 1, 1, 4)
        self.gridLayout.addWidget(self.caliber, 1, 1, 1, 3)
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

        self.tr_ui()
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        self.setTitle(tr("weapon", "Weapon"))
        self.rightTwist.setText(tr("weapon", "Right"))
        self.leftTwist.setText(tr("weapon", "Left"))

        self.tileTop.setPlaceholderText(tr("weapon", 'Tile text:'))

        self.profile_name.setPlaceholderText(tr("root", "Field can't be empty"))
        self.tileTop.setPlaceholderText(tr("root", "Field can't be empty"))
