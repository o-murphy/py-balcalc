from PySide6 import QtWidgets, QtGui


class RegExpLineEdit(QtWidgets.QLineEdit):
    def __init__(self, *args, valid_regex):
        super().__init__(*args)
        self.setValidator(QtGui.QRegularExpressionValidator(valid_regex))
        self.textChanged.connect(self.update_style)
        self.update_style()

    def valid(self):
        return not self.property("invalid")

    def set_valid(self, valid: bool = True):
        self.setProperty("invalid", not valid)

    def update_style(self):
        if self.hasAcceptableInput():
            self.set_valid()
        else:
            self.set_valid(False)
        self.style().unpolish(self)
        self.style().polish(self)
        self.setFocus()
