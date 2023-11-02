from PySide6 import QtCore, QtWidgets


class UiProfileTab:
    def setup_ui(self, profileTab):
        profileTab.setObjectName("profileTab")

        self.gridLayout = QtWidgets.QGridLayout(profileTab)

        self.content_tabs = QtWidgets.QTabWidget(profileTab)

        self.munition_tab = QtWidgets.QWidget()
        self.conditions_tab = QtWidgets.QWidget()
        self.a7p_meta_tab = QtWidgets.QWidget()


        self.content_tabs.setObjectName("content_tabs")
        self.munition_tab.setObjectName("munition_tab")
        self.conditions_tab.setObjectName("conditions_tab")
        self.a7p_meta_tab.setObjectName("a7p_meta_tab")

        self.munition_tab_layout = QtWidgets.QGridLayout(self.munition_tab)
        self.munition_tab_layout.setContentsMargins(6, 6, 6, 6)
        self.munition_tab_layout.setObjectName("munition_tab_layout")

        self.conditions_tab_layout = QtWidgets.QGridLayout(self.conditions_tab)
        self.conditions_tab_layout.setContentsMargins(6, 6, 6, 6)
        self.conditions_tab_layout.setObjectName("conditions_tab_layout")

        self.a7p_meta_tab_layout = QtWidgets.QGridLayout(self.a7p_meta_tab)
        self.a7p_meta_tab_layout.setContentsMargins(6, 6, 6, 6)
        self.a7p_meta_tab_layout.setObjectName("conditions_tab_layout")

        self.content_tabs.addTab(self.munition_tab, "")
        self.content_tabs.addTab(self.conditions_tab, "")
        self.content_tabs.addTab(self.a7p_meta_tab, "")

        self.gridLayout.addWidget(self.content_tabs, 0, 0, 1, 1)

        self.retranslate_ui(profileTab)
        self.content_tabs.setCurrentIndex(0)

    def retranslate_ui(self, profileTab):
        _translate = QtCore.QCoreApplication.translate
        self.content_tabs.setTabText(self.content_tabs.indexOf(self.munition_tab),
                                     _translate("profileTab", "Current profile"))
        self.content_tabs.setTabText(self.content_tabs.indexOf(self.conditions_tab),
                                     _translate("profileTab", "Zeroing conditions"))
        self.content_tabs.setTabText(self.content_tabs.indexOf(self.a7p_meta_tab),
                                     _translate("profileTab", "A7P metadata"))
