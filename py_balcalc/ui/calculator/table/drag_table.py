import a7p
from PySide6 import QtWidgets
from py_ballisticcalc import HitResult, Unit

from py_balcalc.settings import app_settings
from py_balcalc.translator import tr
from py_balcalc.ui.custom_widgets import TableModel, SpinBoxDelegate


class DragTable(QtWidgets.QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)
        delegate = SpinBoxDelegate()
        self.setItemDelegateForColumn(0, delegate)
        self.setItemDelegateForColumn(1, delegate)

    def data(self):
        return [{'Mach': i[0], 'CD': i[1]} for i in self._model._data]

    def load_data(self, data: list):

        self._model = TableModel(data)
        self.setModel(self._model)
        header_labels = [
            f'{tr("calculator", "Time")},\n({tr("unit", "c")})',
            f'{tr("unit", "Mach")}',
            f'{tr("calculator", "Range")},\n({tr("unit", ud.symbol)})',
            f'{tr("calculator", "V")},\n({tr("unit", uv.symbol)})',
            f'{tr("calculator", "Drop")},\n({tr("unit", up.symbol)})',
            f'{tr("calculator", "Drop adj.")}\n({tr("unit", uj.symbol)})',
            f'{tr("calculator", "Wind.")},\n({tr("unit", up.symbol)})',
            f'{tr("calculator", "Wind. adj.")}\n({tr("unit", uj.symbol)})',
            f'{tr("calculator", "Angle")},\n({tr("unit", ua.symbol)})',
            f'{tr("calculator", "Energy")},\n({tr("unit", ue.symbol)})',
        ]
        self._model.setHeaders(header_labels)
        self.resizeColumnsToContents()
        self.setSelectionMode(QtWidgets.QTableView.SelectionMode.NoSelection)
        # total_width = self.verticalHeader().width() + 14
        # for col in range(len(header_labels)):
        #     total_width += self.columnWidth(col)
        # self.setMinimumWidth(total_width)

    def dump_data(self) -> list[a7p.CoefRow]:
        return [a7p.CoefRow(mv=int(i[0] * 10000), bc_cd=int(i[1] * 10000)) for i in self._model._data]
