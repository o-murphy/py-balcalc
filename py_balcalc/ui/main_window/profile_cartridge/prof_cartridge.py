from PySide6 import QtWidgets, QtCore
from py_ballisticcalc import Unit

from py_balcalc.settings import DEF_STRINGS_LIMITS, DEF_FLOAT_LIMITS
from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr
from py_balcalc.ui.custom_widgets import TLabel, UnitSpinBox, RegExpLineEdit


class ProfileCartridge(QtWidgets.QGroupBox):
    """shows selected profile cartridge property"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.__post_init__()

    def __post_init__(self):
        self.cartridge_name.setMaxLength(DEF_STRINGS_LIMITS['cartridge_name'])
        self.c_t_coeff.setRange(*DEF_FLOAT_LIMITS['c_t_coeff'].values())

    def init_ui(self):
        self.setObjectName("ProfileCartridge")
        self.setCheckable(True)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.gridLayout.addWidget(TLabel('Name:'), 0, 0)
        self.gridLayout.addWidget(TLabel('Muzzle Velocity:'), 1, 0)
        self.gridLayout.addWidget(TLabel('Temperature:'), 2, 0)
        self.gridLayout.addWidget(TLabel('Temperature sensitivity:'), 3, 0)

        self.cartridge_name = RegExpLineEdit(self, valid_regex=r'.+')

        self.c_t_coeff = QtWidgets.QDoubleSpinBox(self)
        self.temp = UnitSpinBox(self, Unit.CELSIUS(15), 'unit/temperature')
        self.c_muzzle_velocity = UnitSpinBox(self, Unit.MPS(800), 'unit/velocity')

        self.c_t_coeff.setObjectName("c_t_coeff")
        self.temp.setObjectName("temp")
        self.c_muzzle_velocity.setObjectName("muzzle_velocity")

        self.gridLayout.addWidget(self.cartridge_name, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.c_muzzle_velocity, 1, 1)
        self.gridLayout.addWidget(self.temp, 2, 1)
        self.gridLayout.addWidget(self.c_t_coeff, 3, 1)

        self.c_t_coeff.setMaximum(100.0)
        self.c_t_coeff.setDecimals(3)

        self.tr_ui()
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        self.setTitle(tr("cartridge", "Cartridge"))
        self.c_t_coeff.setSuffix(tr("cartridge", " %"))
        self.cartridge_name.setPlaceholderText(tr("root", "Required"))
