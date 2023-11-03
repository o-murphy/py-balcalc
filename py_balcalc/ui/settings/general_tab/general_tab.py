from PySide6 import QtWidgets, QtCore, QtGui

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
        self.Language = QtWidgets.QComboBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Language.sizePolicy().hasHeightForWidth())
        self.Language.setSizePolicy(sizePolicy)
        self.Language.setMinimumSize(QtCore.QSize(100, 0))
        self.Language.setObjectName("Language")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/flags/res/flags/united-kingdom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Language.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/flags/res/flags/ukraine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Language.addItem(icon1, "")
        self.gridLayout.addWidget(self.Language, 0, 1, 1, 1)

        self.gridLayout.addWidget(TLabel("Language"), 0, 0)

        self.line = QtWidgets.QFrame(self)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.translate_ui()

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.Language.setItemText(0, _translate("AppSettings", "English"))
        self.Language.setItemText(1, _translate("AppSettings", "Українська"))
