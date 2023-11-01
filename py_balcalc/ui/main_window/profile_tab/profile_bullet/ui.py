from PySide6 import QtCore, QtWidgets
from py_ballisticcalc import Unit

from py_balcalc.ui.custom_widgets import UnitSpinBox, TLabel


class Ui_bullet:

    def setupUi(self, bullet):
        bullet.setObjectName("bullet")
        bullet.setCheckable(False)

        self.gridLayout = QtWidgets.QGridLayout(bullet)
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.gridLayout.addWidget(TLabel('Name:'), 0, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Weight:'), 1, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Length:'), 2, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Diameter:'), 3, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('Drag function:'), 4, 0, 1, 1)
        self.gridLayout.addWidget(TLabel('DF info:'), 4, 0, 1, 1)

        self.bulletName = QtWidgets.QLineEdit(bullet)
        self.weight = UnitSpinBox(bullet, Unit.GRAIN(175), 'unit/weight')
        self.diameter = UnitSpinBox(bullet, Unit.INCH(0.308), 'unit/diameter')
        self.length = UnitSpinBox(bullet, Unit.INCH(1.2), 'unit/length')

        self.bulletName.setObjectName("bulletName")
        self.weight.setObjectName("weight")
        self.diameter.setObjectName("diameter")
        self.length.setObjectName("length")

        self.gridLayout.addWidget(self.bulletName, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.weight, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.diameter, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.length, 3, 1, 1, 1)

        self.weight.setMaximum(1000.0)
        self.bulletName.setMaxLength(20)

        # self.dragType = QtWidgets.QComboBox(bullet)
        # self.dragType.setObjectName("dragType")
        # self.gridLayout.addWidget(self.dragType, 4, 1, 1, 3)

        # self.dragEditor = QtWidgets.QPushButton(bullet)
        # self.gridLayout.addWidget(self.dragEditor, 5, 4, 1, 1)


        # self.dragFuncData = QtWidgets.QLineEdit(bullet)
        # self.dragFuncData.setObjectName("dragFuncData")
        # self.gridLayout.addWidget(self.dragFuncData, 5, 1, 1, 3)

        # self.widget = QtWidgets.QWidget(bullet)
        # self.widget.setObjectName("widget")

        # self.dfDataEditor = QtWidgets.QToolButton(self.widget)

        # self.dfDataEditor.setIcon(qta.icon('mdi6.pencil', color='white', color_disabled='grey'))
        # self.dfDataEditor.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        # self.dfDataEditor.setObjectName("dfDataEditor")
        # self.addDrag = QtWidgets.QToolButton(self.widget)
        # self.addDrag.setEnabled(True)

        # self.addDrag.setIcon(qta.icon('mdi6.plus', color='white', color_disabled='grey'))
        # self.addDrag.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        # self.addDrag.setObjectName("addDrag")
        # self.removeDrag = QtWidgets.QToolButton(self.widget)

        # self.removeDrag.setIcon(qta.icon('mdi6.minus', color='white', color_disabled='grey'))
        # self.removeDrag.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        # self.removeDrag.setObjectName("removeDrag")

        self.retranslateUi(bullet)
        # self.dragType.setCurrentIndex(-1)

    def retranslateUi(self, bullet):
        _translate = QtCore.QCoreApplication.translate
        bullet.setTitle(_translate("bullet", "Bullet"))

        # self.dragEditor.setToolTip(_translate("bullet", "Edit drag function"))
        # self.dragEditor.setText(_translate("bullet", "Calculator"))
        # self.dfDataEditor.setToolTip(_translate("bullet", "Edit selected"))
        # self.addDrag.setToolTip(_translate("bullet", "Add new"))
        # self.removeDrag.setToolTip(_translate("bullet", "Remove selected"))
