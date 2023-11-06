import sys

from PySide6 import QtWidgets, QtGui
from py_balcalc.resources import *
from py_balcalc.ui import MainWindow, stylesheet
from py_balcalc.ui.message_handler import qt_message_handler


def main():
    QtCore.qInstallMessageHandler(qt_message_handler)
    # sys.argv += ['-platform', 'windows:darkmode=2']
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setWindowIcon(QtGui.QIcon(':/app_icon.ico'))
    app.setStyleSheet(stylesheet.load_from_resources(":/qss/application.qss"))

    window = MainWindow(app)
    window.show()

    app.exit(app.exec())


if __name__ == '__main__':
    main()
