# -*- coding: utf-8 -*-
from PySide6 import QtCore, QtGui

from py_balcalc.logger import logger
import os


def get_darkModePalette(app=None):
    darkPalette = app.palette()
    darkPalette.setColor(QtGui.QPalette.Window, QtCore.QColor(53, 53, 53))
    darkPalette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, QtCore.QColor(127, 127, 127))
    darkPalette.setColor(QtGui.QPalette.Base, QtCore.QColor(42, 42, 42))
    darkPalette.setColor(QtGui.QPalette.AlternateBase, QtCore.QColor(66, 66, 66))
    darkPalette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    darkPalette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    darkPalette.setColor(QtGui.QPalette.Text, QtCore.white)
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Text, QtCore.QColor(127, 127, 127))
    darkPalette.setColor(QtGui.QPalette.Dark, QtCore.QColor(35, 35, 35))
    darkPalette.setColor(QtGui.QPalette.Shadow, QtCore.QColor(20, 20, 20))
    darkPalette.setColor(QtGui.QPalette.Button, QtCore.QColor(53, 53, 53))
    darkPalette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, QtCore.QColor(127, 127, 127))
    darkPalette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    darkPalette.setColor(QtGui.QPalette.Link, QtCore.QColor(42, 130, 218))
    darkPalette.setColor(QtGui.QPalette.Highlight, QtCore.QColor(42, 130, 218))
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, QtCore.QColor(80, 80, 80))
    darkPalette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.white)
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, QtCore.QColor(127, 127, 127), )

    return darkPalette


def load_qss(file_name):
    """use setStylesheet(load_qss(filename))"""
    try:
        with open(file_name, 'r') as fh:
            return fh.read()
    except FileNotFoundError as err:
        logger.exception(err)
        return ''


def main_app_qss():
    """use setStylesheet(main_app_qss())"""
    try:
        qss_path = os.path.join(os.path.dirname(__file__), '../qss/application.qss')
        with open(qss_path, 'r') as fh:
            return fh.read()
    except FileNotFoundError as err:
        logger.exception(err)
        return ''


def load_from_resources(name: str):
    stylesheet = QtCore.QFile(name)
    stylesheet.open(QtCore.QIODevice.ReadOnly)
    return QtCore.QTextStream(stylesheet).readAll()
