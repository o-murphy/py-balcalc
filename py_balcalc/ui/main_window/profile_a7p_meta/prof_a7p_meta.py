import a7p
from PySide6 import QtWidgets, QtCore, QtGui
from py_ballisticcalc import Unit

from py_balcalc.settings import DEF_DISTANCES_LIST_SIZE, DEF_FLOAT_LIMITS
from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr
from py_balcalc.ui.custom_widgets import TLabel, UnitSpinBox


class DistancesList(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setRowCount(1)
        self.verticalHeader().setHidden(True)
        self.setEditTriggers(QtWidgets.QTableView.DoubleClicked)
        self.tr_ui()

    def create_cols(self, count=DEF_DISTANCES_LIST_SIZE):
        self.clear()
        self.setColumnCount(count)

    def fit_to_content(self):
        total_height = self.rowHeight(0) \
                       + self.horizontalHeader().height() \
                       + self.horizontalScrollBar().height()
        self.setFixedHeight(total_height)

    def load_data(self, distances):
        self.create_cols()
        for i, d in enumerate(distances):
            w = UnitSpinBox(self, Unit.METER(0), 'unit/distance')
            w.set_raw_value(d)
            self.setCellWidget(0, i, w)
        self.fit_to_content()

    def dump_data(self):
        out = []
        for i in range(self.columnCount()):
            out.append(self.cellWidget(0, i).raw_value())
        return out

    def tr_ui(self):
        ...


# class DistanceDelegate(QtWidgets.QStyledItemDelegate):
#
#     def createEditor(self, parent, option, index):
#         spinbox = UnitSpinBox(parent, Unit.METER(0), 'unit/distance')
#         spinbox.setFrame(False)  # Remove the frame around the spinbox
#         return spinbox
#
#     def setEditorData(self, editor, index):
#         value = index.model().data(index, QtCore.Qt.EditRole)
#         # editor.set_raw_value(value)  # Use the custom set_raw_value method of your UnitSpinBox
#         print(f'set editor {value}')
#
#         editor.set_raw_value(value)  # Use the custom set_raw_value method of your UnitSpinBox
#
#     def setModelData(self, editor, model, index):
#         value = editor.raw_value()
#         print(f'set model {value}')
#
#         model.setData(index, value, QtCore.Qt.EditRole)
#
#     def updateEditorGeometry(self, editor, option, index):
#         editor.setGeometry(option.rect)
#
#
# class DistancesListView(QtWidgets.QListView):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setFlow(self.Flow.LeftToRight)
#
#         self.model = QtGui.QStandardItemModel(self)
#         self.setModel(self.model)
#         delegate = DistanceDelegate()
#         self.setItemDelegate(delegate)
#
#     def load_data(self, distances):
#         for raw_value in distances:
#             item = QtGui.QStandardItem()
#             item.setData(raw_value, QtCore.Qt.EditRole)
#             self.model.appendRow(item)


class ProfileA7PMeta(QtWidgets.QGroupBox):
    """shows selected profile a7p_meta. property"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.__post_init__()

    def __post_init__(self):
        self.zero_x.setMaximum(DEF_FLOAT_LIMITS['zero_x']['max'])
        self.zero_x.setMinimum(DEF_FLOAT_LIMITS['zero_x']['min'])
        self.zero_y.setMaximum(DEF_FLOAT_LIMITS['zero_y']['max'])
        self.zero_y.setMinimum(DEF_FLOAT_LIMITS['zero_y']['min'])
        # self.device_uuid.setMaxLength(DEF_STRINGS_LIMITS['device_uuid'])
        # self.user_note.setMaxLength(DEF_STRINGS_LIMITS['user_note'])  # TODO: setMaxLength

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

    def init_ui(self):
        self.setObjectName("ProfileA7PMeta")
        self.setCheckable(True)

        self.gridLayout = QtWidgets.QGridLayout(self)
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
        # self.distances = DistancesListView(self)
        self.user_note = QtWidgets.QPlainTextEdit(self)

        self.change_distances = QtWidgets.QHBoxLayout()

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

        # self.gridLayout.addWidget(self.distances, 4, 1)
        self.gridLayout.addWidget(self.distances, 4, 1)
        self.gridLayout.addWidget(self.user_note, 5, 1)

        self.tr_ui()
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        self.setTitle(tr("a7p_meta", "A7P Meta"))
