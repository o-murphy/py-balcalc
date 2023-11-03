from PySide6 import QtWidgets

from py_balcalc.ui.custom_widgets import TLabel


class UnitsTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setObjectName("tabUnits")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("conditions_tab_layout")

        self.gridLayout.addWidget(TLabel("Sight height"), 0, 0)
        self.gridLayout.addWidget(TLabel("Twist"), 1, 0)
        self.gridLayout.addWidget(TLabel("Velocity"), 2, 0)
        self.gridLayout.addWidget(TLabel("Distance"), 3, 0)
        self.gridLayout.addWidget(TLabel("Temperature"), 4, 0)
        self.gridLayout.addWidget(TLabel("Weight"), 5, 0)
        self.gridLayout.addWidget(TLabel("Length"), 6, 0)
        self.gridLayout.addWidget(TLabel("Diameter"), 7, 0)
        self.gridLayout.addWidget(TLabel("Pressure"), 8, 0)
        self.gridLayout.addWidget(TLabel("Drop"), 9, 0)
        self.gridLayout.addWidget(TLabel("Adjustment"), 10, 0)
        self.gridLayout.addWidget(TLabel("Angular"), 11, 0)
        self.gridLayout.addWidget(TLabel("Energy"), 12, 0)
        self.gridLayout.addWidget(TLabel("OGW"), 13, 0)
        self.gridLayout.addWidget(TLabel("Target height"), 14, 0)

        self.shUnits = QtWidgets.QComboBox(self)
        self.twistUnits = QtWidgets.QComboBox(self)
        self.vUnits = QtWidgets.QComboBox(self)
        self.distUnits = QtWidgets.QComboBox(self)
        self.tempUnits = QtWidgets.QComboBox(self)
        self.wUnits = QtWidgets.QComboBox(self)
        self.lnUnits = QtWidgets.QComboBox(self)
        self.dUnits = QtWidgets.QComboBox(self)
        self.pUnits = QtWidgets.QComboBox(self)
        self.dropUnits = QtWidgets.QComboBox(self)
        self.pathUnits = QtWidgets.QComboBox(self)
        self.angleUnits = QtWidgets.QComboBox(self)
        self.eUnits = QtWidgets.QComboBox(self)
        self.ogwUnits = QtWidgets.QComboBox(self)
        self.thUnits = QtWidgets.QComboBox(self)

        self.shUnits.setObjectName("shUnits")
        self.twistUnits.setObjectName("twistUnits")
        self.vUnits.setObjectName("vUnits")
        self.distUnits.setObjectName("distUnits")
        self.tempUnits.setObjectName("tempUnits")
        self.wUnits.setObjectName("wUnits")
        self.lnUnits.setObjectName("lnUnits")
        self.dUnits.setObjectName("dUnits")
        self.pUnits.setObjectName("pUnits")
        self.dropUnits.setObjectName("dropUnits")
        self.pathUnits.setObjectName("pathUnits")
        self.angleUnits.setObjectName("angleUnits")
        self.eUnits.setObjectName("eUnits")
        self.ogwUnits.setObjectName("ogwUnits")
        self.thUnits.setObjectName("thUnits")

        self.gridLayout.addWidget(self.shUnits, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.twistUnits, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.vUnits, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.distUnits, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.tempUnits, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.wUnits, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.lnUnits, 6, 1, 1, 1)
        self.gridLayout.addWidget(self.dUnits, 7, 1, 1, 1)
        self.gridLayout.addWidget(self.pUnits, 8, 1, 1, 1)
        self.gridLayout.addWidget(self.dropUnits, 9, 1, 1, 1)
        self.gridLayout.addWidget(self.pathUnits, 10, 1, 1, 1)
        self.gridLayout.addWidget(self.angleUnits, 11, 1, 1, 1)
        self.gridLayout.addWidget(self.eUnits, 12, 1, 1, 1)
        self.gridLayout.addWidget(self.ogwUnits, 13, 1, 1, 1)
        self.gridLayout.addWidget(self.thUnits, 14, 1, 1, 1)

        self.tr_ui()

    def tr_ui(self):
        ...
