from PySide6 import QtWidgets, QtCore

from py_balcalc.settings import appSettings
from py_balcalc.signals_manager import appSignalMgr
from .ui import Ui_conditions


class ProfileConditions(QtWidgets.QWidget, Ui_conditions):
    """shows selected profile atmo conditions"""
    def __init__(self, parent=None):
        super(ProfileConditions, self).__init__(parent)
        self.setupUi(self)

        self._cur_profile = None

        appSignalMgr.appSettingsUpdated.connect(self.setUnits)

    def setupUi(self, conditions):
        super(ProfileConditions, self).setupUi(conditions)
        self.groupBox.setCheckable(False)
        self.groupBox.layout().setAlignment(QtCore.Qt.AlignLeft)

    def set_current(self, profile):
        """updates inner widgets data with selected profile data"""
        self._cur_profile = profile
        self.setUnits()

    def _pressure_changed(self, value):
        self._cur_profile.z_pressure = appSettings.value('unit/pressure')(value)

    def setUnits(self):
        if self._cur_profile:
            _translate = QtCore.QCoreApplication.translate
            self.z_pressure.set_raw_value(self._cur_profile.z_pressure)
            self.z_temp.set_raw_value(self._cur_profile.z_temp)
            self.z_powder_temp.set_raw_value(self._cur_profile.z_powder_temp)
            self.z_angle.set_raw_value(self._cur_profile.z_angle)
            # self.z_azimuth.setValue(self._cur_profile.z_azimuth >> au)
            # self.z_latitude.setValue(self._cur_profile.z_latitude >> au)

            self.z_humidity.setValue(self._cur_profile.z_humidity)
