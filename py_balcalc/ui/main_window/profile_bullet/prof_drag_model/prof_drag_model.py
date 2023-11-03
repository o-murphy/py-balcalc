from PySide6 import QtWidgets, QtCore
from py_ballisticcalc import Unit

from py_balcalc.ui.custom_widgets import UnitSpinBox, NoWheelDoubleSpinBox


class ModelG(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setColumnCount(2)
        self.setRowCount(5)

        for i in range(5):
            u = UnitSpinBox(self, Unit.MPS(0), 'unit/velocity')
            u.setMaximum(3000)
            d = NoWheelDoubleSpinBox(self)
            d.setMaximum(2)
            d.setDecimals(3)
            d.setSingleStep(0.001)
            self.setCellWidget(i, 0, u)
            self.setCellWidget(i, 1, d)

        self.setEditTriggers(QtWidgets.QTableView.DoubleClicked)

        self.tr_ui()

    def tr_ui(self):
        tr = QtCore.QCoreApplication.translate
        self.setHorizontalHeaderItem(
            0, QtWidgets.QTableWidgetItem(tr("drag_model", "Velocity"))
        )
        self.setHorizontalHeaderItem(
            1, QtWidgets.QTableWidgetItem(tr("drag_model", "BC"))
        )


class ModelCDM(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO: ModelCDM editing


class ProfileDragModel(QtWidgets.QStackedWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.g1 = ModelG(self)
        self.g7 = ModelG(self)
        self.cdm = ModelCDM(self)

        self.addWidget(self.g1)
        self.addWidget(self.g7)
        self.addWidget(self.cdm)
        self.tr_ui()

    def tr_ui(self):
        ...
