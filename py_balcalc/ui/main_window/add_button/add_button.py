from PySide6.QtWidgets import QWidget

from .ui import Ui_addButton


# this button used as last row in profiles table
class AddButton(QWidget, Ui_addButton):
    def __init__(self, parent=None):
        super(AddButton, self).__init__(parent)
        self.setupUi(self)
