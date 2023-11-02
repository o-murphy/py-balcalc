import a7p
from PySide6 import QtWidgets, QtCore
from py_ballisticcalc import Unit

from py_balcalc.ui.custom_widgets import TLabel, UnitSpinBox


class DistancesList(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRowCount(1)
        self.verticalHeader().setHidden(True)
        self.setEditTriggers(QtWidgets.QTableView.DoubleClicked)
        self.retranslate_ui()

    def create_cols(self, count=196):
        self.setColumnCount(count)

        for i in range(self.columnCount()):
            d = UnitSpinBox(self, Unit.METER(0), 'unit/distance')
            d.setMaximum(3000)
            d.setDecimals(1)
            d.setSingleStep(0.1)
            self.setCellWidget(0, i, d)

        total_height = self.rowHeight(0) \
                       + self.horizontalHeader().height() \
                       + self.horizontalScrollBar().height()
        self.setFixedHeight(total_height)

    def load_data(self, distances):
        count = len(distances)
        self.clear()
        self.create_cols(196 if count <= 196 else count)
        for i, d in enumerate(distances):
            w = self.cellWidget(0, i)
            w.set_raw_value(d)

    def dump_data(self):
        out = []
        for i in range(self.columnCount()):
            out.append(self.cellWidget(0, i).raw_value())
        return out

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate


class ProfileA7PMeta(QtWidgets.QGroupBox):
    """shows selected profile a7p_meta. property"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui(self)

    def change_distances_list(self, item):

        warn = QtWidgets.QMessageBox.warning(
            self,
            "Warning!",
            "You'll lost the previous distance table!",
            QtWidgets.QMessageBox.StandardButton.Ok,
            QtWidgets.QMessageBox.StandardButton.Cancel,
        )
        if warn == QtWidgets.QMessageBox.StandardButton.Ok:
            values = [Unit.METER(d) for d in a7p.A7PFactory.DistanceTable[item].value]
            self.distances.load_data(values)

    def setup_ui(self, a7p_meta):
        a7p_meta.setObjectName("ProfileA7PMeta")
        a7p_meta.setCheckable(True)

        self.gridLayout = QtWidgets.QGridLayout(a7p_meta)
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.gridLayout.addWidget(TLabel('Device UUID:'), 0, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Zero X:'), 1, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Zero Y:'), 2, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Distances list:'), 3, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Note:'), 5, 0, 1, 1)

        self.device_uuid = QtWidgets.QLabel(self)
        self.zero_x = QtWidgets.QDoubleSpinBox(self)
        self.zero_y = QtWidgets.QDoubleSpinBox(self)
        self.distances = DistancesList(self)
        self.user_note = QtWidgets.QPlainTextEdit(self)

        self.change_distances = QtWidgets.QHBoxLayout(self)

        for item in a7p.A7PFactory.DistanceTable.__members__:
            button = QtWidgets.QPushButton(item)
            self.change_distances.addWidget(button)
            button.clicked.connect(
                lambda *args, item=item: self.change_distances_list(item)
            )

        self.gridLayout.addWidget(self.device_uuid, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.zero_x, 1, 1)
        self.gridLayout.addWidget(self.zero_y, 2, 1)

        self.gridLayout.addLayout(self.change_distances, 3, 1)

        self.gridLayout.addWidget(self.distances, 4, 1)
        self.gridLayout.addWidget(self.user_note, 5, 1)

        self.retranslate_ui(a7p_meta)

    def retranslate_ui(self, a7p_meta):
        _translate = QtCore.QCoreApplication.translate
        a7p_meta.setTitle(_translate("a7p_meta", "A7P Meta"))
