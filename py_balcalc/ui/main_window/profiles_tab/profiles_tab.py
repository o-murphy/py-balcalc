import os
from datetime import datetime

from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox

# from modules.env_update import USER_RECENT
from .add_button import AddButton
# from .profile_item import ProfileItem
from .ui import Ui_profilesTab
from .profiles_table import ProfilesTable
from .profiles_tools import ProfilesTools
from .profile_current import ProfileCurrent
# from ..close_dialog import CloseDialog


# main widget of working profiles list tab
class ProfilesTab(QWidget, Ui_profilesTab):
    def __init__(self, *args):
        super().__init__()

        self.profiles_table_widget = ProfilesTable(self)
        self.profiles_table = self.profiles_table_widget.tableWidget
        self.profiles_tools = ProfilesTools(self)
        self.profile_current = ProfileCurrent(self)
        self.add_button = AddButton()

        self.setupUi(self)

        # self.setupConnects()
        # if len(args) > 1:
        #     try:
        #         self.open_file(args[1])
        #     except FileExistsError:
        #         pass
        #     except FileNotFoundError:
        #         pass
        #
        # # self.profile_current.set_current(None)

    def setupUi(self, profiles_tab: 'ProfilesTab'):
        """Sets default widget positions in a gridLayout"""
        super(ProfilesTab, self).setupUi(profiles_tab)
        self.gridLayout.addWidget(self.profiles_table_widget, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.profiles_tools, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.profile_current, 0, 1, 2, 1)
        self.insert_add_button(0)

    def setupConnects(self):
        """connects functions to its controllers in the inner widgets"""
        # self.profiles_tools.newProfileButton.clicked.connect(self.add_profile)
        # self.add_btn.add.clicked.connect(self.add_profile)
        # self.profiles_tools.removeProfileButton.clicked.connect(self.remove_profile)
        # self.profiles_tools.downProfile.clicked.connect(self.move_profile_down)
        # self.profiles_tools.upProfile.clicked.connect(self.move_profile_up)
        #
        # self.profiles_tools.saveAsButton.clicked.connect(self.save_as_file_dialog)
        # self.profiles_tools.saveButton.clicked.connect(self.save_file_dialog)
        # self.profiles_tools.openFile.clicked.connect(self.open_file_dialog)
        # self.profiles_tools.closeFile.clicked.connect(self.close_file)
        # self.profiles_table.currentCellChanged.connect(self.current_cell_changed)
        #
        # self.profiles_tools.loadBookMark.clicked.connect(self.load_bookmark)
        ...

    def current_cell_changed(self, row, col, prow, pcol):
        """sets selected ballistic profile data to profileCurrent widget"""
        # cur = self.profiles_table.cellWidget(row, col)
        # self.profile_current.set_current(cur)
        ...

    def insert_add_button(self, last_row):
        """set AddButton to last row into profilesTable"""
        self.profiles_table.insertRow(last_row)
        self.profiles_table.setCellWidget(last_row, 0, self.add_button)

    def add_profile(self, data=None):
        """
        creates new Profile widget, and fill it with input data
        updates profilesTable data
        """
        # if self.profiles_table.rowCount() < 21:
        #     new_item = ProfileItem(self)
        #
        #     new_item.set(data)
        #     self.profiles_table_widget.add_row(new_item)
        #
        #     self.set_is_saved(False)
        #
        #     row_count = self.profiles_table_widget.tableWidget.rowCount()
        #     self.profiles_table_widget.tableWidget.setCurrentCell(row_count - 1, 0)
        #
        #     last_row = self.profiles_table.rowCount()
        #     self.insert_add_btn(last_row)
        #     self.profiles_table.removeRow(last_row - 2)
        ...

    def add_many(self, data):
        """creates multiple profiles at least, look ProfilesTab.add_profile for more info"""
        # for prof in data:
        #     new_item = ProfileItem(self)
        #
        #     new_item.set(prof)
        #     self.profiles_table_widget.add_row(new_item)
        #
        # self.set_is_saved(False)
        #
        # row_count = self.profiles_table_widget.tableWidget.rowCount()
        # self.profiles_table_widget.tableWidget.setCurrentCell(row_count - 1, 0)
        #
        # last_row = self.profiles_table.rowCount()
        # self.insert_add_btn(last_row)
        # self.profiles_table.removeRow(0)
        ...

    def remove_profile(self):
        """removes selected profile from profilesTable, deletes all data of selected profile from working list"""
        # if self.profiles_table.rowCount() > 0:
        #     self.profiles_table_widget.remove_row()
        #     self.set_is_saved(False)
        ...

    def move_profile_up(self):
        """moves selected row up on 1 step"""
        # if self.profiles_table.rowCount() > 0:
        #     self.profiles_table_widget.move_up()
        ...

    def move_profile_down(self):
        """moves selected row down on 1 step"""
        # if self.profiles_table.currentRow() < self.profiles_table.rowCount() - 2:
        #     if self.profiles_table.rowCount() > 0:
        #         self.profiles_table_widget.move_down()
        ...

    @staticmethod
    def get_datetime():
        """return: datetime in default app format"""
        return datetime.now().strftime("%y-%m-%d_%H-%M-%S")

    def save_as_file_dialog(self, fileName=None):
        # options = QFileDialog.Options()
        # fileName, fileFormat = QFileDialog.getSaveFileName(
        #     self,
        #     "QFileDialog.getSaveFileName()",
        #     rf'{USER_RECENT}\{fileName}' if fileName else rf'{USER_RECENT}\recent_{self.get_datetime()}',
        #     "PyBalCalc Profiles (*.arbcp);;JSON (*.json);;All Files (*);;Text Files (*.txt)",
        #     options=options
        # )
        # if fileName:
        #     self.save_profiles(fileName)
        ...

    def get_recent_profile_table(self):
        """return list of dicts of all ballistic profiles in working list"""
        # profiles = []
        # for i in range(self.profiles_table.rowCount() - 1):
        #     p = self.profiles_table.cellWidget(i, 0).get()
        #     profiles.append(p)
        # return profiles
        ...

    def save_profiles(self, fileName):
        """saves all ballistic profiles in working list as json formatted file"""
        # import json
        # with open(fileName, 'w') as fp:
        #     json.dump(self.get_recent_profile_table(), fp)
        # self.current_file = fileName
        # self.set_is_saved(True)
        ...

    def save_file_dialog(self):
        if self.current_file != '':
            if os.path.isfile(self.current_file):
                self.save_profiles(self.current_file)
            else:
                self.save_as_file_dialog(self.current_file)
        else:
            self.save_as_file_dialog()

    def open_file_dialog(self):
        # self.close_file()
        # if self.is_saved:
        #     options = QFileDialog.Options()
        #     fileName, fileFormat = QFileDialog.getOpenFileName(
        #         self,
        #         "QFileDialog.getOpenFileName()",
        #         USER_RECENT,
        #         "PyBalCalc Profiles (*.arbcp);;JSON (*.json);;All Files (*);;Python Files (*.py)",
        #         options=options
        #     )
        #     if fileName:
        #         self.open_file(fileName)
        ...

    def open_file(self, fileName):
        """opens ballistic profiles from a json formatted file and loads it to working list"""
        # with open(fileName, 'r') as fp:
        #     import json
        #     data = json.load(fp)
        # # for d in data:
        # #     self.add_profile(data=d)
        #
        # self.add_many(data)
        #
        # self.current_file = fileName
        # self.set_is_saved(True)
        ...

    def close_file(self):
        """removes all profiles from working list and set is_saved param to True"""
        # choice = QMessageBox.Cancel
        # if not self.is_saved:
        #     choice = CloseDialog().exec_()
        #     if choice == QMessageBox.Save:
        #         self.save_file_dialog()
        #     if choice == QMessageBox.Close:
        #         self.set_is_saved(True)
        # if self.is_saved:
        #     self.profiles_table_widget.remove_all()
        #     self.current_file = ''
        #     self.set_is_saved(True)
        # return choice
        ...

    def load_bookmark(self):
        """opens master for adding templates from database into working list"""
        # from .profile_bookmarks import BookMarks
        # from dbworker import get_templates
        #
        # rifles = BookMarks(self, 0)
        #
        # if rifles.exec_():
        #     rifle_id = rifles.selected
        #     if rifle_id:
        #         cartridges = BookMarks(self, 1, cal=rifles.cal)
        #         if cartridges.exec_():
        #             cart_id = cartridges.selected
        #             if cart_id:
        #                 data = get_templates(rifle_id, cart_id)
        #
        #                 self.add_profile(data)
        ...
