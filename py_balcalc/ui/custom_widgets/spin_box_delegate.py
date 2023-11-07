from PySide6 import QtWidgets, QtCore


class SpinBoxDelegate(QtWidgets.QItemDelegate):
    def createEditor(self, parent, option, index):
        spinbox = QtWidgets.QDoubleSpinBox(parent)
        spinbox.setFrame(False)  # Remove the frame around the spinbox
        spinbox.setRange(0, 100)  # Set the range for the spinbox
        spinbox.setDecimals(3)
        spinbox.setSingleStep(0.001)
        return spinbox

    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.EditRole)
        editor.setValue(value)

    def setModelData(self, editor, model, index):
        value = editor.value()
        model.setData(index, value, QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
