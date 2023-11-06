import a7p
from PySide6 import QtWidgets, QtCore, QtGui
from py_ballisticcalc import Unit

from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr
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
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        self.setHorizontalHeaderItem(
            0, QtWidgets.QTableWidgetItem(tr("drag_model", "Velocity"))
        )
        self.setHorizontalHeaderItem(
            1, QtWidgets.QTableWidgetItem(tr("drag_model", "BC"))
        )


class SpinBoxDelegate(QtWidgets.QItemDelegate):
    def createEditor(self, parent, option, index):
        spinbox = QtWidgets.QDoubleSpinBox(parent)
        spinbox.setFrame(False)  # Remove the frame around the spinbox
        spinbox.setRange(0, 100)  # Set the range for the spinbox
        spinbox.setDecimals(3)
        spinbox.setSingleStep(0.001)
        return spinbox

    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.EditRole)
        editor.setValue(value)

    def setModelData(self, editor, model, index):
        value = editor.value()
        model.setData(index, value, QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self._headers = []

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal and section < len(self._headers):
                return self._headers[section]
            elif orientation == QtCore.Qt.Vertical:
                return str(section + 1)
        return super().headerData(section, orientation, role)

    def setHeaders(self, headers):
        self._headers = headers
        self.layoutChanged.emit()  # Notify the view to update the headers


class ModelCDM(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        delegate = SpinBoxDelegate()
        self.setItemDelegateForColumn(0, delegate)
        self.setItemDelegateForColumn(1, delegate)
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def load_data(self, data: list[a7p.CoefRow]):
        rows = [[i.mv / 10000, i.bc_cd / 10000] for i in data]
        self.model = TableModel(rows)
        self.setModel(self.model)
        self.tr_ui()

    def dump_data(self) -> list[a7p.CoefRow]:
        return [a7p.CoefRow(mv=int(i[0] * 10000), bc_cd=int(i[1] * 10000)) for i in self.model._data]

    def tr_ui(self):
        header_labels = [tr("bullet", "Mach"), tr("bullet", "CD")]
        self.model.setHeaders(header_labels)


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
