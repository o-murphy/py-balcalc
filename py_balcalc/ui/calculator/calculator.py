from PySide6 import QtWidgets

from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.ui.main_window.data_worker import DataWorker


class CalculatorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, tab: [QtWidgets.QWidget, DataWorker] = None):
        super(CalculatorDialog, self).__init__(parent)
        self.init_ui()
        self.tab = tab

    def init_ui(self):
        self.tr_ui()
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        ...
