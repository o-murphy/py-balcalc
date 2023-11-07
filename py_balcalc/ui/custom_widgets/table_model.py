from PySide6 import QtCore


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self._headers = []

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The b_length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the b_length (only works if all rows are an equal b_length)
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal and section < len(self._headers):
                return self._headers[section]
            elif orientation == QtCore.Qt.Vertical:
                return str(section + 1)
        return super().headerData(section, orientation, role)

    def setHeaders(self, headers):
        self._headers = headers
        self.layoutChanged.emit()  # Notify the view to update the headers
