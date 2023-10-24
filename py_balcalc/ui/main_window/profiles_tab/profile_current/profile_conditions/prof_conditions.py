from PySide6 import QtWidgets, QtGui, QtCore
from .ui import Ui_conditions


# shows selected profile atmo conditions
class ProfileConditions(QtWidgets.QWidget, Ui_conditions):
    def __init__(self, parent=None):
        super(ProfileConditions, self).__init__(parent)
        self.setupUi(self)

        self._cur_profile = None
        self._cur_units = None

        # self.setConnects()

    def setupUi(self, conditions):
        super(ProfileConditions, self).setupUi(conditions)
        self.groupBox.layout().setAlignment(QtCore.Qt.AlignLeft)

    # def setConnects(self):
    #     """connects functions to its controllers in the inner widgets"""
    #     self.z_pressure.valueChanged.connect(self._pressure_changed)
    #     self.z_temp.valueChanged.connect(self._temp_changed)
    #     self.z_powder_temp.valueChanged.connect(self._powder_temp_changed)
    #     self.z_angle.valueChanged.connect(self._angle_changed)
    #     self.z_azimuth.valueChanged.connect(self._azimuth_changed)
    #     self.z_latitude.valueChanged.connect(self._latitude_changed)
    #     self.z_humidity.valueChanged.connect(self._humidity_changed)

    def set_current(self, profile):
        """updates inner widgets data with selected profile data"""
        self._cur_profile = profile
        self.setUnits()

    # def _humidity_changed(self, value):
    #     self._cur_profile.z_humidity = value
    #
    # def _temp_changed(self, value):
    #     self._cur_profile.z_temp = Temperature(value, self._cur_units.tempUnits.currentData())
    #
    # def _powder_temp_changed(self, value):
    #     self._cur_profile.z_powder_temp = Temperature(value, self._cur_units.tempUnits.currentData())
    #
    # def _angle_changed(self, value):
    #     self._cur_profile.z_angle = Angular(value, self._cur_units.angleUnits.currentData())
    #
    # def _azimuth_changed(self, value):
    #     self._cur_profile.z_azimuth = Angular(value, self._cur_units.angleUnits.currentData())
    #
    # def _latitude_changed(self, value):
    #     self._cur_profile.z_latitude = Angular(value, self._cur_units.angleUnits.currentData())
    #
    # def _pressure_changed(self, value):
    #     self._cur_profile.z_pressure = Pressure(value, self._cur_units.pUnits.currentData())

    def setUnits(self):
        self._cur_units = self.window().settings

        if self._cur_profile:
            _translate = QtCore.QCoreApplication.translate
            pu = self._cur_units.pUnits.currentData()
            tu = self._cur_units.tempUnits.currentData()
            au = self._cur_units.angleUnits.currentData()
            self.z_pressure.setValue(self._cur_profile.z_pressure >> pu)
            self.z_temp.setValue(self._cur_profile.z_temp >> tu)
            self.z_powder_temp.setValue(self._cur_profile.z_powder_temp >> tu)
            self.z_angle.setValue(self._cur_profile.z_angle >> au)
            # self.z_azimuth.setValue(self._cur_profile.z_azimuth >> au)
            # self.z_latitude.setValue(self._cur_profile.z_latitude >> au)

            self.z_humidity.setValue(self._cur_profile.z_humidity)

            self.z_pressure.setSuffix(' ' + _translate("units", pu.symbol))
            self.z_temp.setSuffix(' ' + _translate("units", tu.symbol))
            self.z_powder_temp.setSuffix(' ' + _translate("units", tu.symbol))
            self.z_angle.setSuffix(' ' + _translate("units", au.symbol))
            # self.z_azimuth.setSuffix(self._cur_units.angleUnits.currentText())
            # self.z_latitude.setSuffix(self._cur_units.angleUnits.currentText())
