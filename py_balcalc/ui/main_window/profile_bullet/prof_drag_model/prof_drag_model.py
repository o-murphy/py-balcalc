import a7p
from PySide6 import QtWidgets, QtCore
from py_ballisticcalc import Unit, TableG1, TableG7

from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr
from py_balcalc.ui.custom_widgets import UnitSpinBox, NoWheelDoubleSpinBox, TableModel
from py_balcalc.ui.custom_widgets.spin_box_delegate import SpinBoxDelegate


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
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def data(self):
        coefficients = []
        for i in range(self.rowCount()):
            v = self.cellWidget(i, 0).raw_value()
            c = self.cellWidget(i, 1).value()
            if v > 0 and c > 0:
                coefficients.append({"V": v, "BC": c})
        return coefficients

    def load_data(self, coefficients: list[a7p.CoefRow]):
        for i, row in enumerate(coefficients):
            v = self.cellWidget(i, 0)
            c = self.cellWidget(i, 1)
            v.set_raw_value(Unit.MPS(row.mv / 10))
            c.setValue(row.bc_cd / 10000)

    def dump_data(self) -> list[a7p.CoefRow]:
        coefficients = []
        for i in range(self.rowCount()):
            v = self.cellWidget(i, 0).raw_value() >> Unit.MPS
            c = self.cellWidget(i, 1).value()
            if v > 0 and c > 0:
                coefficients.append(a7p.CoefRow(mv=int(v * 10), bc_cd=int(c * 10000)))
        return coefficients

    def tr_ui(self):
        self.setHorizontalHeaderItem(
            0, QtWidgets.QTableWidgetItem(tr("drag_model", "Velocity"))
        )
        self.setHorizontalHeaderItem(
            1, QtWidgets.QTableWidgetItem(tr("drag_model", "BC"))
        )


class ModelCDM(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        delegate = SpinBoxDelegate()
        self.setItemDelegateForColumn(0, delegate)
        self.setItemDelegateForColumn(1, delegate)
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def data(self):
        return [{'Mach': i[0], 'CD': i[1]} for i in self._model._data]

    def load_data(self, data: list[a7p.CoefRow]):
        rows = [[i.mv / 10000, i.bc_cd / 10000] for i in data]
        self._model = TableModel(rows)
        self.setModel(self._model)
        self.tr_ui()

    def dump_data(self) -> list[a7p.CoefRow]:
        return [a7p.CoefRow(mv=int(i[0] * 10000), bc_cd=int(i[1] * 10000)) for i in self._model._data]

    def tr_ui(self):
        header_labels = [tr("bullet", "Mach"), tr("bullet", "CD")]
        self._model.setHeaders(header_labels)


class ProfileDragModel(QtWidgets.QStackedWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self._model = None
        self.__post_init__()

    def __post_init__(self):
        self.currentChanged.connect(self._set_model)

    def data(self):
        return self.currentWidget().data()

    def load_data(self, data: list[a7p.CoefRow]):
        self.currentWidget().load_data(data)

    def dump_data(self) -> list[a7p.CoefRow]:
        return self.currentWidget().dump_data()

    def model(self):
        self._set_model()
        return self._model

    def _set_model(self):
        current = self.currentWidget()
        if current == self.g1:
            self._model = TableG1
        elif current == self.g7:
            self._model = TableG7
        elif current == self.cdm:
            self._model = self.cdm.dump_data()

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
