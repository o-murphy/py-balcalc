from PySide6 import QtWidgets, QtCore

from py_balcalc.convertor import Convertor


class ConvertorSpinBox(QtWidgets.QDoubleSpinBox):
    def __init__(self, parent, step=1, name: str = None, vmin=-10000, vmax=10000):
        super().__init__(parent)

        if name:
            self.setObjectName(name)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.setMinimum(vmin)
        self.setMaximum(vmax)
        self.setSingleStep(step)
        # self.setDecimals(decimals)

        self._convertor: Convertor = None

    def wheelEvent(self, event) -> None:
        pass

    def validate(self, text: str, pos: int) -> object:
        text = text.replace(".", ",")
        return QtWidgets.QDoubleSpinBox.validate(self, text, pos)

    def valueFromText(self, text: str) -> float:
        text = text.replace(",", ".")
        return float(text)

    def convertor(self) -> Convertor:
        return self._convertor

    def setConvertor(self, value: Convertor):
        self._convertor = value
        self.setDecimals(self._convertor.accuracy)
        single_step = 10**(-self.decimals())
        self.setSingleStep(single_step)

    def setRawValue(self, value):
        if self._convertor is not None:
            self.setValue(self._convertor.fromRaw(value))
        else:
            self.setValue(value)

    def rawValue(self):
        if self._convertor is not None:
            return self._convertor.toRaw(self.value())
        else:
            return self.value()
