from PySide6 import QtWidgets, QtCore, QtGui
from .ui import Ui_weapon
import qtawesome as qta


# shows selected profile weapon property
class ProfileWeapon(QtWidgets.QWidget, Ui_weapon):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, weapon):
        super().setupUi(weapon)
        self.rifleGroupBox.layout().setAlignment(QtCore.Qt.AlignLeft)
        self.auto_tile_act = QtGui.QAction(
            qta.icon('mdi6.autorenew', color='white', color_active='orange', color_disabled='grey'),
            'Auto'
        )
        self.caliberShort.addAction(self.auto_tile_act, QtWidgets.QLineEdit.TrailingPosition)
        self.auto_tile_act.triggered.connect(self._auto_tile)

        # self._cur_profile = None
        # self._cur_units = None

        # self.setConnects()

    # def setConnects(self):
    #     """connects functions to its controllers in the inner widgets"""
    #     self.sh.valueChanged.connect(self._sh_changed)
    #     self.twist.valueChanged.connect(self._twist_changed)
    #     self.rifleName.textChanged.connect(self._rifle_name_changed)
    #     self.caliberName.textChanged.connect(self._caliber_name_changed)
    #     self.rightTwist.clicked.connect(self._twist_direction_changed)
    #     self.caliberShort.textChanged.connect(self._set_caliber_short)
    #
    def _auto_tile(self):
        # self._cur_profile._auto_tile()
        # self.caliberShort.setText(self._cur_profile.caliberShort)
        ...

    # def _set_caliber_short(self, text):
    #     self._cur_profile.caliberShort = text
    #     self._cur_profile.create_tile()
    #
    # def _rifle_name_changed(self, text):
    #     self._cur_profile.rifleName.setText(text)
    #
    # def _caliber_name_changed(self, text):
    #     self._cur_profile.caliberName = text
    #
    # def _twist_direction_changed(self):
    #     self._cur_profile.rightTwist = self.rightTwist.isChecked()

    # def _sh_changed(self, value):
    #     self._cur_profile.sh = Distance(value, self._cur_units.shUnits.currentData())
    #
    # def _twist_changed(self, value):
    #     self._cur_profile.twist = Distance(value, self._cur_units.twistUnits.currentData())

    def setUnits(self):
        self._cur_units = self.window().app_settings

        if self._cur_profile:
            self.sh.setValue(int(self._cur_profile.sh.get_in(self._cur_units.shUnits.currentData())))
            self.sh.setSuffix(self._cur_units.shUnits.currentText())
            self.twist.setValue(self._cur_profile.twist.get_in(self._cur_units.twistUnits.currentData()))
            self.twist.setSuffix(self._cur_units.twistUnits.currentText())
            self.caliberShort.setText(self._cur_profile.caliberShort)

    def set_current(self, profile):
        """updates inner widgets data with selected profile data"""
        self._cur_profile = profile
        self.setUnits()

        self.rifleName.setText(self._cur_profile.rifleName.text())
        self.caliberName.setText(self._cur_profile.caliberName)
        self.rightTwist.setChecked(self._cur_profile.rightTwist)

    def retranslateUi(self, weapon):
        _translate = QtCore.QCoreApplication.translate
        self.caliberShort.setPlaceholderText(_translate("weapon", 'Tile text:'))
        super().retranslateUi(weapon)
