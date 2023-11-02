import a7p
from PySide6 import QtWidgets, QtCore, QtGui
from py_ballisticcalc import Unit

from py_balcalc.ui.custom_widgets import TLabel, UnitSpinBox
from ..prof_drag_model import ProfileDragModel
import qtawesome as qta


class ChangeDragModel(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)
        self.resize(200, 50)
        self.lt = QtWidgets.QVBoxLayout(self)
        self.combo = QtWidgets.QComboBox(self)
        self.combo.addItem("Model G1", a7p.GType.G1)
        self.combo.addItem("Model G7", a7p.GType.G7)
        self.combo.addItem("CDM", a7p.GType.CUSTOM)
        self.buttons = QtWidgets.QDialogButtonBox(self)
        self.lt.addWidget(self.combo)
        self.lt.addWidget(self.buttons, alignment=QtCore.Qt.AlignHCenter)

        self.buttons.setStandardButtons(self.buttons.StandardButton.Ok)

        self.translate_ui()

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate('drag_model', "Change drag model"))


class ProfileBullet(QtWidgets.QGroupBox):
    """shows selected profile bullet property"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui(self)
        self.__post_init__()

    def __post_init__(self):
        self.change_drag_model.clicked.connect(self.on_change_drag_model)
        self.auto_tile_act.triggered.connect(self.auto_tile)
        self.tile_help.triggered.connect(self.show_tile_help)

    def auto_tile(self):
        value = self.weight.value()
        value = int(value) if value % 1 == 0 else value
        self.tileBot.setText(f"{value}{self.weight.suffix()}".replace(" ", ""))

    def show_tile_help(self):
        # TODO:
        ...

    def on_change_drag_model(self):

        warn = QtWidgets.QMessageBox.warning(
            self,
            "Warning!",
            "You'll lost the previous drag model!",
            QtWidgets.QMessageBox.StandardButton.Ok,
            QtWidgets.QMessageBox.StandardButton.Cancel,
        )
        if warn:
            dlg = ChangeDragModel()
            if dlg.exec():
                gtype = dlg.combo.currentData()
                if gtype == a7p.GType.G1:
                    self.drag_model_label.setText("Drag model: G1")
                    self.drag_model.setCurrentIndex(0)
                elif gtype == a7p.GType.G7:
                    self.drag_model_label.setText("Drag model: G7")
                    self.drag_model.setCurrentIndex(1)
                else:
                    self.drag_model_label.setText("Drag model: CDM")
                    self.drag_model.setCurrentIndex(2)

    def setup_ui(self, bullet):
        bullet.setObjectName("bullet")
        bullet.setCheckable(False)

        self.gridLayout = QtWidgets.QGridLayout(bullet)
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.gridLayout.addWidget(TLabel('Name:'), 0, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Weight:'), 1, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Length:'), 2, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Diameter:'), 3, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Tile bottom:'), 4, 0, 1, 1)

        self.drag_model_label = TLabel('None')
        self.gridLayout.addWidget(self.drag_model_label, 5, 0, 1, 1)

        self.tileBot = QtWidgets.QLineEdit(bullet)
        self.tileBot.setMinimumSize(QtCore.QSize(0, 0))
        self.tileBot.setMaxLength(8)
        self.tileBot.setObjectName("caliberShort")

        self.bulletName = QtWidgets.QLineEdit(bullet)
        self.weight = UnitSpinBox(bullet, Unit.GRAIN(175), 'unit/weight')
        self.diameter = UnitSpinBox(bullet, Unit.INCH(0.308), 'unit/diameter')
        self.length = UnitSpinBox(bullet, Unit.INCH(1.2), 'unit/length')

        self.bulletName.setObjectName("bulletName")
        self.weight.setObjectName("weight")
        self.diameter.setObjectName("diameter")
        self.length.setObjectName("length")

        self.gridLayout.addWidget(self.bulletName, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.weight, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.diameter, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.length, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.tileBot, 4, 1, 1, 1)

        self.change_drag_model = QtWidgets.QPushButton("Change drag model")
        self.gridLayout.addWidget(self.change_drag_model, 5, 1, 1, 1)

        self.weight.setMaximum(1000.0)
        # self.bulletName.setMaxLength(20)

        self.auto_tile_act = QtGui.QAction(
            qta.icon(
                'mdi6.autorenew', color='white', color_active='orange', color_disabled='grey'
            ), 'Auto')
        self.tile_help = QtGui.QAction(
            qta.icon(
                'mdi6.help', color='white', color_active='orange', color_disabled='grey'
            ), 'Help')
        self.tileBot.addAction(self.tile_help, QtWidgets.QLineEdit.TrailingPosition)
        self.tileBot.addAction(self.auto_tile_act, QtWidgets.QLineEdit.TrailingPosition)

        self.drag_model = ProfileDragModel(self)
        self.gridLayout.addWidget(self.drag_model, self.gridLayout.rowCount(), 0, 1, 2)

        self.retranslate_ui(bullet)

    def retranslate_ui(self, bullet):
        _translate = QtCore.QCoreApplication.translate
        bullet.setTitle(_translate("bullet", "Bullet"))