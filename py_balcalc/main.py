import sys

from PySide6 import QtWidgets, QtGui

from py_balcalc.logger import logger
from py_balcalc.ui import MainWindow
from py_balcalc.ui.stylesheet import main_app_qss
from py_balcalc.ui.resources import *


def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    logger.error('qt_message_handler: line: %d, func: %s(), file: %s' % (
          context.line, context.function, context.file))
    logger.error('  %s: %s\n' % (mode, message))


def main():
    QtCore.qInstallMessageHandler(qt_message_handler)

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('.rsrc/Icon.ico'))
    app.setStyleSheet(main_app_qss())

    window = MainWindow(app)
    window.show()

    app.exit(app.exec())


if __name__ == '__main__':
    main()
