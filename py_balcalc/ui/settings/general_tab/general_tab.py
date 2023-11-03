from PySide6 import QtWidgets, QtCore

from py_balcalc.ui.custom_widgets import TLabel


class GeneralTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setObjectName("tabGeneral")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 2)
        self.locale = QtWidgets.QComboBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locale.sizePolicy().hasHeightForWidth())
        self.locale.setSizePolicy(sizePolicy)
        self.locale.setMinimumSize(QtCore.QSize(100, 0))
        self.locale.setObjectName("locale")

        self.gridLayout.addWidget(TLabel("Language"), 0, 0)
        self.gridLayout.addWidget(self.locale, 0, 1, 1, 1)

        self.line = QtWidgets.QFrame(self)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.tr_ui()

    def tr_ui(self):
        ...
