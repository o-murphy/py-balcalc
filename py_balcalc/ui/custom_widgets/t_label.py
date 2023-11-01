from PySide6 import QtWidgets, QtCore


class TLabel(QtWidgets.QLabel):
    """Localized label"""

    def __init__(self, *args):
        super().__init__(*args)
        self.setAlignment(QtCore.Qt.AlignTop)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setText(_translate('TLabel', self.text()))
