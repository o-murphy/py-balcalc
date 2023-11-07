import logging
from pathlib import Path

import a7p.protovalidate
from PySide6 import QtCore
from a7p import A7PFile

from py_balcalc.ui.message_handler import qt_message_handler


def save_file(file_name, payload):
    try:
        data = A7PFile.dumps(payload)
        with open(file_name, 'wb') as fp:
            fp.write(data)
        return True
    except a7p.protovalidate.ValidationError as err:
        logging.warning(err.violations)
        qt_message_handler(
            QtCore.QtMsgType.QtWarningMsg,
            err,
            "Invalid profile\n\n" + str(err.violations))
        return False


def save_file_stream(file_name, data):
    with open(file_name, 'wb') as fp:
        fp.write(data)


def open_files(*file_names, validate: bool=True):
    """opens ballistic profiles from a json formatted file and loads it to working list"""
    profiles = []
    for path in file_names:
        if Path(path).is_dir():
            profiles.extend(open_files(*(Path(path).iterdir(), validate)))

        if Path(path).suffix in ['.a7p', '.A7P']:
            if not validate:
                try:
                    with open(path, 'rb') as fp:
                        a7p_file = A7PFile.load(fp, validate=False)
                    profiles.append((path, a7p_file))
                except Exception as err:
                    qt_message_handler(QtCore.QtMsgType.QtWarningMsg, err, err)
            else:
                try:
                    try:
                        with open(path, 'rb') as fp:
                            a7p_file = A7PFile.load(fp)
                        profiles.append((path, a7p_file))
                    except a7p.protovalidate.ValidationError as err:
                        logging.warning(err.violations)
                        qt_message_handler(
                            QtCore.QtMsgType.QtWarningMsg,
                            err,
                            "Invalid file, trying to load unsafe\n\n" + str(err.violations))
                        with open(path, 'rb') as fp:
                            a7p_file = A7PFile.load(fp, validate=False)
                        profiles.append((path, a7p_file))
                except Exception as err:
                    qt_message_handler(QtCore.QtMsgType.QtWarningMsg, err, err)
    return profiles
