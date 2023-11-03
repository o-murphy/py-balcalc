from PySide6 import QtWidgets, QtCore
from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr


class TLabel(QtWidgets.QLabel):
    """Localized label"""

    def __init__(self, *args):
        super().__init__(*args)
        self._default_text = self.text()
        self.init_ui()
        self.__post_init__()

    def init_ui(self):
        self.setAlignment(QtCore.Qt.AlignTop)
        self.tr_ui()

    def __post_init__(self):
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        # tr = QtCore.QCoreApplication.translate
        self.setText(tr('TLabel', self._default_text))
