from PySide6 import QtWidgets, QtCore
from py_ballisticcalc import Unit

from py_balcalc.ui.custom_widgets import TLabel, UnitSpinBox


class ProfileCartridge(QtWidgets.QGroupBox):
    """shows selected profile cartridge property"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui(self)

    def setup_ui(self, cartridge):
        cartridge.setObjectName("cartridge")
        cartridge.setCheckable(False)

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

        self.retranslate_ui(cartridge)

    def retranslate_ui(self, cartridge):
        _translate = QtCore.QCoreApplication.translate
        cartridge.setTitle(_translate("cartridge", "Cartridge"))
        self.ts.setSuffix(_translate("cartridge", " %"))
