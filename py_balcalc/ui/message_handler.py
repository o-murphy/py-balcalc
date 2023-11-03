from PySide6 import QtCore

from py_balcalc.logger import logger


def qt_message_handler(mode, context, message):
    if mode == QtCore.QtMsgType.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtMsgType.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtMsgType.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtMsgType.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    # logger.error('qt_message_handler: line: %d, func: %s(), file: %s' % (
    #       context.line, context.function, context.file))
    # logger.error('  %s: %s\n' % (mode, message))
    logger.exception(f"{mode}, {context}, {message}")
