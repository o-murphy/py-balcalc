# -*u.- coding: utf-8 -*u.-

from PySide6 import QtWidgets, QtGui, QtCore


class NoWheelDoubleSpinBox(QtWidgets.QDoubleSpinBox):
    """implementation of QDoubleSpinBox with ignored wheelEvent"""
    def __init__(self):
        super(NoWheelDoubleSpinBox, self).__init__()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(80, 16777215))
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.setWrapping(False)
        self.setFrame(True)
        self.setReadOnly(False)
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.setAccelerated(False)
        self.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.setKeyboardTracking(False)
        self.setMinimum(-200.0)
        self.setMaximum(200.0)
        self.setSingleStep(0.25)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def wheelEvent(self, event):
        if self.hasFocus():
            super().wheelEvent(event)


class NoWheelSpinBox(QtWidgets.QSpinBox):
    """implementation of QSpinBox with ignored wheelEvent"""
    def __init__(self):
        super(NoWheelSpinBox, self).__init__()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.setFont(font)
        # self.setStyleSheet("")
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.setPrefix("")
        self.setMaximum(10000)
        self.setSingleStep(10)
        self.setProperty("value", 100)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def wheelEvent(self, event):
        if self.hasFocus():
            super().wheelEvent(event)


# ballistics coefficient spinbox
class BCSpinBox(NoWheelDoubleSpinBox):
    def __init__(self):
        super(BCSpinBox, self).__init__()
        self.setMaximum(1)
        self.setMinimum(0)
        self.setSingleStep(0.001)
        self.setDecimals(3)


# vUnits spinbox
class BVSpinBox(NoWheelSpinBox):
    def __init__(self):
        super(BVSpinBox, self).__init__()
        self.setMaximum(2000)
        self.setMinimum(-1)
        self.setSingleStep(1)


class DSpinbox(NoWheelSpinBox):
    def __init__(self):
        super(DSpinbox, self).__init__()
        self.setMinimum(0)
        self.setMaximum(5000)
        self.setSingleStep(1)


# shows value of a bullet dropUnits
class DropSpinBox(NoWheelDoubleSpinBox):
    def __init__(self):
        super(DropSpinBox, self).__init__()
        self.setMaximum(9999.9)
        self.setMinimum(0)
        self.setDecimals(1)


# shows value of a bullet dropUnits (readonly)
class DropRoSpinBox(DropSpinBox):
    def __init__(self):
        super(DropRoSpinBox, self).__init__()
        self.setDisabled(True)
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)


# shows value of a bullet dropUnits (readonly)
class DropRoSBw(QtWidgets.QWidget):
    def __init__(self):
        super(DropRoSBw, self).__init__()
        self.sb = DropRoSpinBox()
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.gridLayout)
        self.layout().addWidget(self.sb)


class DisabledDoubleSpinBox(NoWheelDoubleSpinBox):
    def __init__(self):
        super(DisabledDoubleSpinBox, self).__init__()
        self.setDisabled(True)
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
