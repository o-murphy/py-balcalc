import logging

from PySide6 import QtCore, QtWidgets

from py_balcalc.logger import logger


def qt_message_handler(mode, context, message):
    if mode == QtCore.QtMsgType.QtInfoMsg:
        mode, level = 'INFO', logging.INFO
        icon = QtWidgets.QMessageBox.Icon.Information
    elif mode == QtCore.QtMsgType.QtWarningMsg:
        mode, level = 'WARNING', logging.WARNING
        icon = QtWidgets.QMessageBox.Icon.Warning
    elif mode == QtCore.QtMsgType.QtCriticalMsg:
        mode, level = 'CRITICAL', logging.CRITICAL
        icon = QtWidgets.QMessageBox.Icon.Critical
    elif mode == QtCore.QtMsgType.QtFatalMsg:
        mode, level = 'FATAL', logging.FATAL
        icon = QtWidgets.QMessageBox.Icon.Critical
    else:
        mode, level = 'DEBUG', logging.DEBUG
        icon = QtWidgets.QMessageBox.Icon.Information
    # logger.error('qt_message_handler: line: %d, func: %s(), file: %s' % (
    #       context.line, context.function, context.file))
    # logger.error('  %s: %s\n' % (mode, message))
    logger.log(level, f"{context}, {message}")
    dlg = QtWidgets.QMessageBox(
        icon, mode, str(message),
        QtWidgets.QMessageBox.StandardButton.Ok,
    )
    dlg.exec()
