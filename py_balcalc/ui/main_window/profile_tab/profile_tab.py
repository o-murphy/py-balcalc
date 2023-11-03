from PySide6 import QtCore, QtWidgets, QtGui

from py_ballisticcalc import Unit

from py_balcalc.signals_manager import appSignalMgr
from py_balcalc.translator import tr
from py_balcalc.ui.main_window.profile_weapon import ProfileWeapon
from py_balcalc.ui.main_window.profile_cartridge import ProfileCartridge
from py_balcalc.ui.main_window.profile_bullet import ProfileBullet
from py_balcalc.ui.main_window.profile_conditions import ProfileConditions
from py_balcalc.ui.main_window.profile_a7p_meta import ProfileA7PMeta
from py_balcalc.ui.main_window.data_worker import DataWorker


class ProfileTab(QtWidgets.QWidget, DataWorker):
    def __init__(self, parent=None, payload=None, file_name=None):
        super().__init__(parent)
        self.weapon = ProfileWeapon(self)
        self.cartridge = ProfileCartridge(self)
        self.bullet = ProfileBullet(self)
        self.conditions = ProfileConditions(self)
        self.a7p_meta = ProfileA7PMeta(self)
        self.init_ui()

        self._profile = payload.profile
        self.file_name = file_name
        self.__post_init__()

    def _update_values(self):
        super()._update_values()
        self.a7p_meta.distances.load_data(
            [Unit.METER(d / 100) for d in self._profile.distances]
        )
        self.weapon.zero_dist.set_raw_value(
            Unit.METER(self._profile.distances[self._profile.c_zero_distance_idx] / 100)
        )

    def init_ui(self):
        self.setObjectName("profileTab")

        self.gridLayout = QtWidgets.QGridLayout(self)

        self.content_tabs = QtWidgets.QTabWidget(self)

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

        self.content_tabs.addTab(
            self.munition_tab, QtGui.QIcon(":/icons/ammunition-orange.svg"), "")
        self.content_tabs.addTab(
            self.conditions_tab, QtGui.QIcon(":/icons/water-thermometer-outline-orange.svg"), "")
        self.content_tabs.addTab(
            self.a7p_meta_tab, QtGui.QIcon(":/icons/card-bulleted-outline-orange.svg"), "")

        self.gridLayout.addWidget(self.content_tabs, 0, 0, 1, 1)
        self.content_tabs.setCurrentIndex(0)

        self.munition_tab_layout.setAlignment(QtCore.Qt.AlignTop)
        self.conditions_tab_layout.setAlignment(QtCore.Qt.AlignTop)
        self.a7p_meta_tab_layout.setAlignment(QtCore.Qt.AlignTop)

        self.munition_tab_layout.addWidget(self.weapon, 0, 0, 1, 1)
        self.munition_tab_layout.addWidget(self.cartridge, 1, 0, 1, 1)
        self.munition_tab_layout.addWidget(self.bullet, 0, 1, 2, 1)
        self.conditions_tab_layout.addWidget(self.conditions, 0, 0, 1, 1)
        self.a7p_meta_tab_layout.addWidget(self.a7p_meta, 0, 0, 1, 1)

        self.munition_tab.layout().setColumnStretch(0, 1)
        self.munition_tab.layout().setColumnStretch(1, 1)

        self.tr_ui()
        appSignalMgr.translator_updated.connect(self.tr_ui)

    def tr_ui(self):
        self.content_tabs.setTabText(self.content_tabs.indexOf(self.munition_tab),
                                     tr("profileTab", "Current profile"))
        self.content_tabs.setTabText(self.content_tabs.indexOf(self.conditions_tab),
                                     tr("profileTab", "Zeroing conditions"))
        self.content_tabs.setTabText(self.content_tabs.indexOf(self.a7p_meta_tab),
                                     tr("profileTab", "A7P metadata"))
