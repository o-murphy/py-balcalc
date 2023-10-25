from PySide6 import QtWidgets, QtGui, QtCore
# Qt, pyqtSignal, QCoreApplication
# from PyQt5.QtWidgets import QWidget

# from dbworker.models import DragFunc
# from gui.db_widgets.edit.df_type_dlg import DFTypeDlg
# from gui.db_widgets.edit.drag_func_settings import BCEdit
# from gui.db_widgets.edit.drag_func_settings import CDFEdit
# from gui.db_widgets.edit.drag_func_settings import MBCEdit
# from gui.drag_func_editor.drag_func_edit import DragFuncEditDialog
# from py_ballisticcalc.bmath.unit import Weight, Distance
from py_balcalc.settings import appSettings
from py_balcalc.signals_manager import appSignalMgr
from .ui import Ui_bullet


# shows selected profile bullet property
class ProfileBullet(QtWidgets.QWidget, Ui_bullet):
    itemEvent = QtCore.Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # self._ch_df_text = {}
        self._cur_profile = None
        self.setConnects()
        appSignalMgr.appSettingsUpdated.connect(self.setUnits)

    def setupUi(self, bullet):
        super().setupUi(bullet)
        self.bulletGroupBox.setCheckable(False)
        self.bulletGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)

    def setConnects(self):
        """connects functions to its controllers in the inner widgets"""
        self.weight.valueChanged.connect(self._weight_changed)
        self.length.valueChanged.connect(self._length_changed)
        self.diameter.valueChanged.connect(self._diameter_changed)
        self.bulletName.textChanged.connect(self._bullet_name_changed)
        # self.dragType.currentIndexChanged.connect(self._df_changed)

        # self.weight.valueChanged.connect(lambda: self._cur_profile.create_tile())

        # self.addDrag.clicked.connect(self._add_drag)
        # self.dfDataEditor.clicked.connect(self._edit_drag)
        # self.dragEditor.clicked.connect(self._open_df_editor)

    def disconnect(self):
        self.weight.valueChanged.disconnect(self._weight_changed)
        self.length.valueChanged.disconnect(self._length_changed)
        self.diameter.valueChanged.disconnect(self._diameter_changed)
        self.bulletName.textChanged.disconnect(self._bullet_name_changed)
        # self.weight.valueChanged.disconnect(lambda: self._cur_profile.create_tile())

    def set_current(self, profile):
        """updates inner widgets data with selected profile data"""
        self._cur_profile = profile
        # idx = profile.drag_idx
        self.setUnits()

        # self.dragType.clear()
        # for i, df in enumerate(self._cur_profile.drags):
        #     # if isinstance(df, dict):
        #     #     df = DragFunc(**df, attrs='rw')
        #
        #     self.dragType.addItem(df.drag_type + ', ' + df.comment, i)
        #
        # self.dragType.setCurrentIndex(self.dragType.findData(idx))

    def setUnits(self):
        self.setConnects()
        if self._cur_profile:
            _translate = QtCore.QCoreApplication.translate

            wu = appSettings.value('unit/weight')
            lnu = appSettings.value('unit/length')
            du = appSettings.value('unit/diameter')

            self.weight.setSuffix(' ' + _translate("units", wu.symbol))
            self.length.setSuffix(' ' + _translate("units", lnu.symbol))
            self.diameter.setSuffix(' ' + _translate("units", du.symbol))

            self.weight.setValue(self._cur_profile.weight >> wu)
            self.length.setValue(self._cur_profile.length >> lnu)
            self.diameter.setValue(self._cur_profile.diameter >> du)

            self.bulletName.setText(self._cur_profile.bulletName)
        self.disconnect()

    def _bullet_name_changed(self, text):
        self._cur_profile.bulletName = text

    def _weight_changed(self, value):
        self._cur_profile.wUnits = appSettings.value('unit/weight')(value)

    def _length_changed(self, value):
        self._cur_profile.lnUnits = appSettings.value('unit/length')(value)

    def _diameter_changed(self, value):
        self._cur_profile.dUnits = appSettings.value('unit/diameter')(value)

    # def _df_changed(self, idx):
    #     """updates list of drag function for selected bullet"""
    #     if idx >= 0:
    #         self._cur_profile.drag_idx = self.dragType.currentData()
    #         cur_df = self._cur_profile.drags[self._cur_profile.drag_idx]
    #
    #         self.retranslateUi(self)
    #
    #         drag_type = cur_df.drag_type
    #         data = cur_df.data
    #         comment = cur_df.comment
    #
    #         if drag_type in ['G1', 'G7']:
    #             text = f'{self._ch_df_text["bc"]}: {data:.3f}'
    #         elif drag_type.endswith('Multi-BC'):
    #             count = [(bc, v) for (bc, v) in data if bc > 0 and v >= 0]
    #             text = f'{self._ch_df_text["points"]}: ' + str(len(count))
    #         else:
    #             text = f'{self._ch_df_text["dfl"]}: ' + str(len(data))
    #
    #         self.dragFuncData.setText(text)
    #         self.dragType.setToolTip(comment)
    #
    # def _edit_drag(self, data=None, comment=''):
    #     """opens drag func editor with current bullet data and selected drag function"""
    #     idx = self.dragType.currentData()
    #     cur_df = self._cur_profile.drags[idx]
    #
    #     df_data = cur_df.data
    #     df_type = cur_df.drag_type
    #     df_comment = cur_df.comment
    #
    #     if df_type in ['G1', 'G7']:
    #         bc_edit = BCEdit(df_data)
    #         if bc_edit.exec_():
    #             data = bc_edit.get()
    #
    #     elif df_type.endswith('Multi-BC'):
    #         bc_edit = MBCEdit(df_data, comment)
    #         if bc_edit.exec_():
    #             data = bc_edit.get()
    #
    #     elif df_type == 'Custom':
    #         edit = CDFEdit(df_data)
    #         if edit.exec_():
    #             data = edit.get()
    #
    #     if data:
    #
    #         if df_type in ['G1', 'G7']:
    #             self._save_cur_df(data, df_comment)
    #
    #         elif df_type.endswith('Multi-BC'):
    #             self._save_cur_df(*data)
    #
    #         elif df_type == 'Custom':
    #             self._save_cur_df(*data)
    #
    # def _add_drag(self, data=None, comment=''):
    #     """opens master to create new drag func for selected bullet"""
    #     df_type = DFTypeDlg()
    #
    #     if df_type.exec_():
    #         drag_type = df_type.combo.currentData()
    #
    #         if drag_type in ['G1', 'G7']:
    #             bc_edit = BCEdit(data)
    #             if bc_edit.exec_():
    #                 data = bc_edit.get()
    #
    #         elif drag_type.endswith('Multi-BC'):
    #             mbc_edit = MBCEdit(data)
    #             if mbc_edit.exec_():
    #                 data, comment = mbc_edit.get()
    #
    #         elif drag_type == 'Custom':
    #             edit = CDFEdit(data)
    #             if edit.exec_():
    #                 data, comment = edit.get()
    #
    #         self._save_new_df(drag_type, data, comment)
    #
    #         return drag_type
    #
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
    #
    # def _save_new_df(self, drag_type, data, comment):
    #     """saves new drag function data to list"""
    #     if data:
    #         new_df = DragFunc(drag_type, data, comment, None, 'rw')
    #         self._cur_profile.drags.append(new_df)
    #         idx = len(self._cur_profile.drags) - 1
    #         self.dragType.addItem(new_df.drag_type + ', ' + new_df.comment, idx)
    #         self.dragType.setCurrentIndex(idx)
    #
    # def _save_cur_df(self, data, comment, df_type=None):
    #     """updates selected drag function"""
    #     idx = self.dragType.currentIndex()
    #     cur_df = self._cur_profile.drags[idx]
    #
    #     cur_df.drag_type = df_type if df_type else cur_df.drag_type
    #
    #     if data:
    #         cur_df.data = data
    #         cur_df.comment = comment
    #         self._df_changed(idx)
    #         self.dragType.setItemText(idx, cur_df.drag_type + ', ' + cur_df.comment)

    def retranslateUi(self, bullet):
        _translate = QtCore.QCoreApplication.translate
        self._ch_df_text = {
            'bc': _translate("bullet", 'BC'),
            'points': _translate("bullet", 'Points'),
            'dfl': _translate("bullet", 'DFL')
        }
        super().retranslateUi(bullet)
