from PySide6 import QtWidgets, QtCore

import qtawesome as qta


class AddButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(AddButton, self).__init__(parent)
        self.setup_ui(self)

    def setup_ui(self, addButton):
        addButton.setObjectName("Ui_addButton")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        self.setIcon(qta.icon('mdi6.file-outline', color='grey'))
        self.setIconSize(QtCore.QSize(20, 20))
        self.setObjectName("add")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setText(_translate("Ui_addButton", "Open file"))
