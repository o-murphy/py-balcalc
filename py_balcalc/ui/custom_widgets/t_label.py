from PySide6 import QtWidgets, QtCore
from py_balcalc.signals_manager import appSignalMgr


class TLabel(QtWidgets.QLabel):
    """Localized label"""

    def __init__(self, *args):
        super().__init__(*args)
        self.setAlignment(QtCore.Qt.AlignTop)
        appSignalMgr.settings_locale_updated.connect(self.tr)

    def tr(self):
        _translate = QtCore.QCoreApplication.translate
        self.setText(_translate('TLabel', self.text()))
