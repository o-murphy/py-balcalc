import a7p
from PySide6 import QtWidgets, QtCore

from .ui import Ui_bullet
from ..prof_drag_model import ProfileDragModel


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

        self.buttons.setStandardButtons(
            self.buttons.StandardButton.Ok
        )

        self.translateUi()

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

    def translateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate('drag_model', "Change drag model"))


class ProfileBullet(QtWidgets.QGroupBox, Ui_bullet):
    """shows selected profile bullet property"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__post_init__()

    def setupUi(self, bullet):
        super().setupUi(bullet)
        self.drag_model = ProfileDragModel(self)
        self.gridLayout.addWidget(self.drag_model, self.gridLayout.rowCount(), 0, 1, 2)

    def __post_init__(self):
        self.change_drag_model.clicked.connect(self.on_change_drag_model)

    def on_change_drag_model(self):

        warn = QtWidgets.QMessageBox.warning(
            self,
            "Warning!",
            "You'll lost all the previous drag model!",
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

    # def _open_df_editor(self):
    #     """
    #     opens drag function editor
    #     updates bullet data with data its returns
    #     """
    #     idx = self.dragType.currentData()
    #     print(idx)
    #     cur_df = self._cur_profile.drags[idx]
    #     state = self._cur_profile.get()
    #     state['df_data'] = cur_df.data
    #     state['df_type'] = cur_df.drag_type
    #     state['df_comment'] = cur_df.comment
    #
    #     idx = self.dragType.currentData()
    #     cur_df = self._cur_profile.drags[idx]
    #
    #     cdf_edit = DragFuncEditDialog(state=state)
    #     if cdf_edit.exec_():
    #         edited_df = cdf_edit.__getstate__()
    #         self._save_cur_df(edited_df['df_data'], edited_df['df_comment'], edited_df['df_type'])
