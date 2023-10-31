from PySide6 import QtWidgets, QtCore, QtGui

from py_balcalc.signals_manager import appSignalMgr
from .ui import Ui_weapon
import qtawesome as qta


class ProfileWeapon(QtWidgets.QWidget, Ui_weapon):
    """shows selected profile weapon property"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._cur_profile = None

    def setupUi(self, weapon):
        super().setupUi(weapon)
        self.rifleGroupBox.setCheckable(False)
        self.rifleGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)
        self.auto_tile_act = QtGui.QAction(
            qta.icon('mdi6.autorenew', color='white', color_active='orange', color_disabled='grey'),
            'Auto'
        )
        self.caliberShort.addAction(self.auto_tile_act, QtWidgets.QLineEdit.TrailingPosition)
        self.auto_tile_act.triggered.connect(self._auto_tile)

        appSignalMgr.appSettingsUpdated.connect(self.setUnits)

    def _auto_tile(self):
        self._cur_profile.auto_tile()
        self.caliberShort.setText(self._cur_profile.caliberShort)

    def setUnits(self):
        # self.disconnect()
        _translate = QtCore.QCoreApplication.translate
        self.sh.set_raw_value(self._cur_profile.sh)
        self.twist.set_raw_value(self._cur_profile.twist)
        # self.setConnects()

    def set_current(self, profile):
        """updates inner widgets data with selected profile data"""
        self._cur_profile = profile
        self.setUnits()

        self.rifleName.setText(self._cur_profile.rifleName)
        self.caliberName.setText(self._cur_profile.caliberName)
        self.caliberShort.setText(self._cur_profile.caliberShort)
        self.rightTwist.setChecked(self._cur_profile.rightTwist)

    def retranslateUi(self, weapon):
        _translate = QtCore.QCoreApplication.translate
        self.caliberShort.setPlaceholderText(_translate("weapon", 'Tile text:'))
        super().retranslateUi(weapon)
