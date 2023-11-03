from PySide6 import QtCore, QtGui, QtWidgets
from .units_tab import UnitsTab
from .general_tab import GeneralTab


class UiAppSettings(object):
    def setup_ui(self, AppSettings):
        AppSettings.setObjectName("AppSettings")
        AppSettings.resize(328, 424)

        self.gridLayout = QtWidgets.QGridLayout(AppSettings)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(AppSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1, QtCore.Qt.AlignBottom)

        self.tabsSettings = QtWidgets.QTabWidget(AppSettings)
        self.tabsSettings.setObjectName("tabsSettings")

        self.general_tab = GeneralTab(self)
        self.tabsSettings.addTab(self.general_tab, "")

        self.units_tab = UnitsTab(self)
        self.tabsSettings.addTab(self.units_tab, "")

        self.tabExtensions = QtWidgets.QWidget()
        self.tabExtensions.setObjectName("tabExtensions")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabExtensions)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabsSettings.addTab(self.tabExtensions, "")
        self.gridLayout.addWidget(self.tabsSettings, 0, 0, 1, 1, QtCore.Qt.AlignTop)

        self.retranslate_ui(AppSettings)
        self.tabsSettings.setCurrentIndex(2)
        self.buttonBox.accepted.connect(AppSettings.accept) # type: ignore
        self.buttonBox.rejected.connect(AppSettings.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AppSettings)

    def retranslate_ui(self, AppSettings):
        _translate = QtCore.QCoreApplication.translate
        AppSettings.setWindowTitle(_translate("AppSettings", "Settings"))

        self.tabsSettings.setTabText(self.tabsSettings.indexOf(self.general_tab), _translate("AppSettings", "General settings"))


        self.tabsSettings.setTabText(self.tabsSettings.indexOf(self.units_tab), _translate("AppSettings", "Units"))
        self.tabsSettings.setTabText(self.tabsSettings.indexOf(self.tabExtensions), _translate("AppSettings", "Extensions"))
