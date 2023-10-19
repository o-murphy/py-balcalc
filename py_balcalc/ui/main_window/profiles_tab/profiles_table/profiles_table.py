from PySide6.QtWidgets import QWidget, QTableWidgetItem

# from .profile_item import ProfileItem
from .ui import Ui_profilesTable


# shows working list of ballistic profiles
class ProfilesTable(QWidget, Ui_profilesTable):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, profilesTable):
        super().setupUi(profilesTable)
        self.tableWidget.verticalHeader().setHidden(True)

    def select(self):
        """Returns current cellWidget"""
        if self.tableWidget.currentItem():
            row = self.tableWidget.currentRow()
            column = self.tableWidget.currentColumn()
            return self.tableWidget.cellWidget(row, column)

    def bottom_row(self):
        """returns row in the bottom in the table"""
        return self.tableWidget.cellWidget(self.tableWidget.rowCount() - 1, 0)

    def add_row(self, widget: 'ProfileItem'):
        row_count = self.tableWidget.rowCount()

        if row_count < 21:
            self.tableWidget.setRowCount(row_count + 1)
            self.tableWidget.setItem(row_count, 0, QTableWidgetItem())
            self.tableWidget.setCellWidget(row_count, 0, widget)
            return row_count

    def remove_row(self):
        if self.tableWidget.rowCount() > 1:
            row = self.tableWidget.selectedItems()[0].row()
            for item in self.tableWidget.selectedItems():
                self.tableWidget.removeRow(item.row())
            if self.tableWidget.item(row, 0):
                self.tableWidget.item(row, 0).setSelected(True)
            elif self.tableWidget.item(row - 1, 0):
                self.tableWidget.item(row - 1, 0).setSelected(True)

    def remove_all(self):
        for i in range(self.tableWidget.rowCount() - 2, -1, -1):
            self.tableWidget.removeRow(i)

    def move_up(self):
        """moves selected row up on 1 step"""
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        if row > 0:
            w = self.tableWidget.cellWidget(row, column)
            self.tableWidget.insertRow(row - 1)
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(row - 1, i, self.tableWidget.takeItem(row + 1, i))
                self.tableWidget.setCellWidget(row - 1, i, w)
                self.tableWidget.setCurrentCell(row - 1, column)
            self.tableWidget.removeRow(row + 1)

    def move_down(self):
        """moves selected row down on 1 step"""
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        if row < self.tableWidget.rowCount() - 1:
            w = self.tableWidget.cellWidget(row, column)
            self.tableWidget.insertRow(row + 2)
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(row + 2, i, self.tableWidget.takeItem(row, i))
                self.tableWidget.setCellWidget(row + 2, i, w)
                self.tableWidget.setCurrentCell(row + 2, column)
            self.tableWidget.removeRow(row)

    def get_current_item(self):
        """returns widget of current selected item"""
        if self.tableWidget.currentItem():
            return self.tableWidget.cellWidget(
                self.tableWidget.currentRow(),
                self.tableWidget.currentColumn())
