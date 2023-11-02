import sys

from PySide6 import QtWidgets

from py_balcalc.logger import logger
from py_balcalc.ui import MainWindow
from py_balcalc.ui.resources import *
from py_balcalc.ui.stylesheet import main_app_qss


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


def main():
    # QtCore.qInstallMessageHandler(qt_message_handler)

    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowIcon(QtGui.QIcon('.rsrc/Icon.ico'))
    app.setStyleSheet(main_app_qss())

    window = MainWindow(app)
    window.show()

    app.exit(app.exec())


if __name__ == '__main__':
    main()
