from PySide6 import QtCore, QtWidgets


class Ui_profileTab:
    def setupUi(self, profileTab):
        profileTab.setObjectName("profileTab")

        self.gridLayout = QtWidgets.QGridLayout(profileTab)

        self.content_tabs = QtWidgets.QTabWidget(profileTab)

        self.munition_tab = QtWidgets.QWidget()
        self.conditions_tab = QtWidgets.QWidget()


        self.content_tabs.setObjectName("content_tabs")
        self.munition_tab.setObjectName("munition_tab")
        self.conditions_tab.setObjectName("conditions_tab")

        self.munition_tab_layout = QtWidgets.QGridLayout(self.munition_tab)
        self.munition_tab_layout.setContentsMargins(6, 6, 6, 6)
        self.munition_tab_layout.setObjectName("munition_tab_layout")

        self.conditions_tab_layout = QtWidgets.QGridLayout(self.conditions_tab)
        self.conditions_tab_layout.setContentsMargins(6, 6, 6, 6)
        self.conditions_tab_layout.setObjectName("conditions_tab_layout")

        self.content_tabs.addTab(self.munition_tab, "")
        self.content_tabs.addTab(self.conditions_tab, "")

        self.gridLayout.addWidget(self.content_tabs, 0, 0, 1, 1)

        self.retranslateUi(profileTab)
        self.content_tabs.setCurrentIndex(0)

    def retranslateUi(self, profileTab):
        _translate = QtCore.QCoreApplication.translate
        self.content_tabs.setTabText(self.content_tabs.indexOf(self.munition_tab),
                                     _translate("profileTab", "Current profile"))
        self.content_tabs.setTabText(self.content_tabs.indexOf(self.conditions_tab),
                                     _translate("profileTab", "Zeroing conditions"))
