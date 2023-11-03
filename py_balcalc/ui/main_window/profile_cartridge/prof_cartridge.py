from PySide6 import QtWidgets, QtCore
from py_ballisticcalc import Unit

from py_balcalc.settings import DEF_STRINGS_LIMITS, DEF_FLOAT_LIMITS
from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr
from py_balcalc.ui.custom_widgets import TLabel, UnitSpinBox


class ProfileCartridge(QtWidgets.QGroupBox):
    """shows selected profile cartridge property"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui(self)

    def __post_init__(self):
        self.cartridgeName.setMaxLength(DEF_STRINGS_LIMITS['cartridge_name'])
        self.ts.setMaximum(DEF_FLOAT_LIMITS['c_t_coeff']['max'])
        self.ts.setMinimum(DEF_FLOAT_LIMITS['c_t_coeff']['min'])

    def init_ui(self, cartridge):
        cartridge.setObjectName("ProfileCartridge")
        cartridge.setCheckable(True)

        self.gridLayout = QtWidgets.QGridLayout(cartridge)
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.gridLayout.addWidget(TLabel('Name:'), 0, 0)
        self.gridLayout.addWidget(TLabel('Muzzle Velocity:'), 1, 0)
        self.gridLayout.addWidget(TLabel('Temperature:'), 2, 0)
        self.gridLayout.addWidget(TLabel('Temperature sensitivity:'), 3, 0)

        self.cartridgeName = QtWidgets.QLineEdit(cartridge)
        self.ts = QtWidgets.QDoubleSpinBox(cartridge)
        self.temp = UnitSpinBox(cartridge, Unit.CELSIUS(15), 'unit/temperature')
        self.mv = UnitSpinBox(cartridge, Unit.MPS(800), 'unit/velocity')

        self.ts.setObjectName("ts")
        self.temp.setObjectName("temp")
        self.mv.setObjectName("muzzle_velocity")

        self.gridLayout.addWidget(self.cartridgeName, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.mv, 1, 1)
        self.gridLayout.addWidget(self.temp, 2, 1)
        self.gridLayout.addWidget(self.ts, 3, 1)

        self.mv.setMaximum(5000)
        self.ts.setMaximum(100.0)
        self.ts.setDecimals(3)

        self.tr_ui()
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        self.setTitle(tr("cartridge", "Cartridge"))
        self.ts.setSuffix(tr("cartridge", " %"))
