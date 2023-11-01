from PySide6 import QtWidgets, QtCore
from py_ballisticcalc import Unit

from py_balcalc.ui.custom_widgets import UnitSpinBox, NoWheelDoubleSpinBox


class ModelG(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setColumnCount(2)
        self.setRowCount(5)

        for i in range(5):
            u = UnitSpinBox(self, Unit.MPS(0), 'unit/velocity')
            d = NoWheelDoubleSpinBox(self)
            self.setCellWidget(i, 0, u)
            self.setCellWidget(i, 1, d)

        self.setEditTriggers(QtWidgets.QTableView.DoubleClicked)
        self.retranslateUi(self)

    def retranslateUi(self, drag_model):
        _translate = QtCore.QCoreApplication.translate
        self.setHorizontalHeaderItem(
            0, QtWidgets.QTableWidgetItem(_translate("drag_model", "Velocity"))
        )
        self.setHorizontalHeaderItem(
            1, QtWidgets.QTableWidgetItem(_translate("drag_model", "BC"))
        )


class ModelCDM(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)


class ProfileDragModel(QtWidgets.QStackedWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.g1 = ModelG(self)
        self.g7 = ModelG(self)
        self.cdm = ModelCDM(self)

        self.addWidget(self.g1)
        self.addWidget(self.g7)
        self.addWidget(self.cdm)
