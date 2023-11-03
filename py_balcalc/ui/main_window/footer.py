# -*- coding: utf-8 -*-

from PySide6 import QtWidgets, QtCore
from py_balcalc import __version__


# footer of the main app window
class FooterWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setObjectName("FooterWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.insertWidget(
            0, QtWidgets.QLabel(f"v{__version__}"), QtCore.Qt.AlignLeft
        )
        self.tr_ui()

    def tr_ui(self):
        ...
