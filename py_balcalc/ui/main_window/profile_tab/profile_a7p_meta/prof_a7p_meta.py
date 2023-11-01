from PySide6 import QtWidgets, QtCore

from py_balcalc.ui.custom_widgets import TLabel


class ProfileA7PMeta(QtWidgets.QGroupBox):
    """shows selected profile a7p_meta. property"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, a7p_meta):
        a7p_meta.setObjectName("a7p_meta")
        a7p_meta.setCheckable(False)

        self.gridLayout = QtWidgets.QGridLayout(a7p_meta)
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.gridLayout.addWidget(TLabel('Device UUID:'), 0, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Zero X:'), 1, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Zero Y:'), 2, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Distances list:'), 3, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Note:'), 4, 0, 1, 1)

        self.device_uuid = QtWidgets.QLabel(self)
        self.zero_x = QtWidgets.QDoubleSpinBox(self)
        self.zero_y = QtWidgets.QDoubleSpinBox(self)
        self.distances = QtWidgets.QComboBox(self)
        self.user_note = QtWidgets.QPlainTextEdit(self)

        self.gridLayout.addWidget(self.device_uuid, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.zero_x, 1, 1)
        self.gridLayout.addWidget(self.zero_y, 2, 1)
        self.gridLayout.addWidget(self.distances, 3, 1)
        self.gridLayout.addWidget(self.user_note, 4, 1)

        self.retranslateUi(a7p_meta)

    def retranslateUi(self, a7p_meta):
        _translate = QtCore.QCoreApplication.translate
        a7p_meta.setTitle(_translate("a7p_meta", "A7P Meta"))
