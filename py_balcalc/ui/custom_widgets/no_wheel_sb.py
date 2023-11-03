# -*u.- coding: utf-8 -*u.-

from PySide6 import QtWidgets, QtCore


class NoWheelDoubleSpinBox(QtWidgets.QDoubleSpinBox):
    """implementation of QDoubleSpinBox with ignored wheelEvent"""
    def __init__(self, parent=None):
        super(NoWheelDoubleSpinBox, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def wheelEvent(self, event):
        # if self.hasFocus():
        #     super().wheelEvent(event)
        pass


class NoWheelSpinBox(QtWidgets.QSpinBox):
    """implementation of QSpinBox with ignored wheelEvent"""
    def __init__(self, parent=None):
        super(NoWheelSpinBox, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def wheelEvent(self, event):
        # if self.hasFocus():
        #     super().wheelEvent(event)
        pass
