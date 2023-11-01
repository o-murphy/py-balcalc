from PySide6 import QtWidgets, QtCore, QtGui

import qtawesome as qta


class AddButton(QtWidgets.QPushButton):

    def __init__(self, parent=None):
        super(AddButton, self).__init__(parent)
        self.setup_ui(self)
        self.setAcceptDrops(True)

    def setup_ui(self, addButton):
        addButton.setObjectName("Ui_addButton")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        self.setIcon(qta.icon('mdi6.file-outline', color='grey'))
        self.setIconSize(QtCore.QSize(20, 20))
        self.setObjectName("add")

        self.setStyleSheet(
        """
            QPushButton {
                color: grey;
            }
            QPushButton:hover {
                color: orange;
            }
        """
        )

        self.retranslateUi()

    def enterEvent(self, QEvent):
        self.setIcon(qta.icon('mdi6.file-outline', color='orange'))

    def leaveEvent(self, QEvent):
        self.setIcon(qta.icon('mdi6.file-outline', color='grey'))

    def dragEnterEvent(self, event) -> None:
        self.setIcon(qta.icon('mdi6.file-outline', color='orange'))
        super(AddButton, self).dragEnterEvent(event)

    def dragLeaveEvent(self, event) -> None:
        self.setIcon(qta.icon('mdi6.file-outline', color='grey'))
        super(AddButton, self).dragLeaveEvent(event)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setText(_translate("Ui_addButton", "Click here or drop files"))
