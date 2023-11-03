import sys

from PySide6 import QtWidgets

from py_balcalc.resources import *
from py_balcalc.ui import MainWindow
from py_balcalc.ui.message_handler import qt_message_handler
from py_balcalc.ui.stylesheet import main_app_qss


def main():
    QtCore.qInstallMessageHandler(qt_message_handler)

    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowIcon(QtGui.QIcon('.rsrc/Icon.ico'))
    app.setStyleSheet(main_app_qss())

    window = MainWindow(app)
    window.show()

    app.exit(app.exec())


if __name__ == '__main__':
    main()
