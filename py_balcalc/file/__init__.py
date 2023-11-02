from pathlib import Path

from PySide6.QtWidgets import QFileDialog
from a7p import A7PFile


# def open_file_dialog():
#     # self.close_file()
#     # if self.is_saved:
#     options = QFileDialog.Options()
#     file_names, file_format = QFileDialog.getOpenFileNames(
#         None,
#         "QFileDialog.getOpenFileName()",
#         # USER_RECENT,
#         filter="ArcherBC2 Profile (*.a7p)",
#         # filter="ArcherBC2 Profile (*.a7p);;JSON (*.json);;All Files (*)",
#         options=options
#     )
#     if file_names:
#         open_file(file_names)


def save_file(file_name, payload):
    with open(file_name, 'wb') as fp:
        A7PFile.dump(payload, fp)


def open_files(*file_names):
    """opens ballistic profiles from a json formatted file and loads it to working list"""
    profiles = []
    for path in file_names:
        print(path)
        if Path(path).is_dir():
            profiles.extend(open_files(*(Path(path).iterdir())))

        if Path(path).suffix in ['.a7p', '.A7P']:
            with open(path, 'rb') as fp:
                a7p_file = A7PFile.load(fp)
            profiles.append(a7p_file)
    return profiles

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
