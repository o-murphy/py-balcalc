from PySide6 import QtWidgets, QtCore, QtGui

from py_balcalc.settings import appSettings
from py_balcalc.signals_manager import appSignalMgr
from .ui import Ui_weapon
import qtawesome as qta


# shows selected profile weapon property
class ProfileWeapon(QtWidgets.QWidget, Ui_weapon):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._cur_profile = None

        self.setConnects()

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

        self.setConnects()
        appSignalMgr.appSettingsUpdated.connect(self.setUnits)

    def setConnects(self):
        """connects functions to its controllers in the inner widgets"""
        # self.sh.valueChanged.connect(self._sh_changed)
        self.twist.valueChanged.connect(self._twist_changed)
        self.rifleName.textChanged.connect(self._rifle_name_changed)
        self.caliberName.textChanged.connect(self._caliber_name_changed)
        self.rightTwist.clicked.connect(self._twist_direction_changed)
        self.caliberShort.textChanged.connect(self._set_caliber_short)

    def disconnect(self):
        # self.sh.valueChanged.disconnect(self._sh_changed)
        self.twist.valueChanged.disconnect(self._twist_changed)
        self.rifleName.textChanged.disconnect(self._rifle_name_changed)
        self.caliberName.textChanged.disconnect(self._caliber_name_changed)
        self.rightTwist.clicked.disconnect(self._twist_direction_changed)
        self.caliberShort.textChanged.disconnect(self._set_caliber_short)

    def _auto_tile(self):
        self._cur_profile.auto_tile()
        self.caliberShort.setText(self._cur_profile.caliberShort)

    def _set_caliber_short(self, text):
        self._cur_profile.caliberShort = text

    def _rifle_name_changed(self, text):
        self._cur_profile.rifleName = text

    def _caliber_name_changed(self, text):
        self._cur_profile.caliberName = text

    def _twist_direction_changed(self):
        self._cur_profile.rightTwist = self.rightTwist.isChecked()

    # def _sh_changed(self, value):
    #     self._cur_profile.sh = appSettings.value('unit/sight_height')(value)

    def _twist_changed(self, value):
        self._cur_profile.twist = appSettings.value('unit/twist')(value)

    def setUnits(self):
        self.disconnect()
        _translate = QtCore.QCoreApplication.translate

        shu = appSettings.value('unit/sight_height')
        tu = appSettings.value('unit/twist')

        # self.sh.setValue(self._cur_profile.sh >> shu)
        # self.sh.setSuffix(' ' + _translate("units", shu.symbol))

        self.sh.set_raw_value(self._cur_profile.sh)

        self.twist.setValue(self._cur_profile.twist >> tu)
        self.twist.setSuffix(' ' + _translate("units", tu.symbol))
        self.setConnects()

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
