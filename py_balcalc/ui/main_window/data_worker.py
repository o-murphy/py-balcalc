import a7p
from PySide6 import QtWidgets, QtGui
from py_ballisticcalc import Unit

from py_balcalc.signals_manager import appSignalMgr
from .profile_weapon import ProfileWeapon
from .profile_cartridge import ProfileCartridge
from .profile_bullet import ProfileBullet
from .profile_a7p_meta import ProfileA7PMeta


class DataWorker:
    _profile: a7p.Profile
    weapon: ProfileWeapon
    cartridge: ProfileCartridge
    bullet: ProfileBullet
    a7p_meta: ProfileA7PMeta

    def __post_init__(self):
        """
        updates inner widgets data with selected profile data
        enables/disables inner tabs if profile type is correct
        """

        self.weapon.profile_name.setText(self._profile.profile_name)
        self.weapon.caliber.setText(self._profile.caliber)
        self.weapon.tileTop.setText(self._profile.short_name_top)
        self.weapon.rightTwist.setChecked(self._profile.twist_dir == 0)

        self.cartridge.cartridge_name.setText(self._profile.cartridge_name)
        self.bullet.bullet_name.setText(self._profile.bullet_name)
        self.bullet.tileBot.setText(self._profile.short_name_bot)

        if not self._profile.short_name_top:
            self.weapon.auto_tile()

        self._update_values()

        self.a7p_meta.device_uuid.setText(self._profile.device_uuid)
        self.a7p_meta.user_note.setPlainText(self._profile.user_note)
        self.a7p_meta.zero_x.setValue(self._profile.zero_x / -1000)
        self.a7p_meta.zero_y.setValue(self._profile.zero_y / 1000)

        appSignalMgr.settings_units_updated.connect(self._update_values)

    def _update_values(self):
        self.weapon.sh.set_raw_value(Unit.MILLIMETER(self._profile.sc_height))
        self.weapon.twist.set_raw_value(Unit.INCH(self._profile.r_twist / 100))

        self.cartridge.mv.set_raw_value(Unit.MPS(self._profile.c_muzzle_velocity / 10))
        self.cartridge.temp.set_raw_value(Unit.CELSIUS(self._profile.c_zero_temperature))
        self.cartridge.ts.setValue(self._profile.c_t_coeff / 1000)

        self.bullet.weight.set_raw_value(Unit.GRAIN(self._profile.b_weight / 10))
        self.bullet.length.set_raw_value(Unit.INCH(self._profile.b_length / 1000))
        self.bullet.diameter.set_raw_value(Unit.INCH(self._profile.b_diameter / 1000))

        if self._profile.bc_type == a7p.GType.G1:
            self.bullet.drag_model_label.setText("Drag model: G1")
            self.bullet.drag_model.setCurrentIndex(0)
            for i, row in enumerate(self._profile.coef_rows):
                v = self.bullet.drag_model.g1.cellWidget(i, 0)
                c = self.bullet.drag_model.g1.cellWidget(i, 1)
                v.set_raw_value(Unit.MPS(row.mv / 10))
                c.setValue(Unit.MPS(row.bc_cd / 10000))
        elif self._profile.bc_type == a7p.GType.G7:
            self.bullet.drag_model_label.setText("Drag model: G7")
            self.bullet.drag_model.setCurrentIndex(1)
            for i, row in enumerate(self._profile.coef_rows):
                v = self.bullet.drag_model.g7.cellWidget(i, 0)
                c = self.bullet.drag_model.g7.cellWidget(i, 1)
                v.set_raw_value(Unit.MPS(row.mv / 10))
                c.setValue(Unit.MPS(row.bc_cd / 10000))

        elif self._profile.bc_type == a7p.GType.CUSTOM:
            self.bullet.drag_model_label.setText("CDM")
            self.bullet.drag_model.setCurrentIndex(2)
            self.bullet.drag_model.cdm.load_data(self._profile.coef_rows)

        if hasattr(self, 'conditions'):
            self.conditions.z_pressure.set_raw_value(Unit.HP(self._profile.c_zero_air_pressure / 10))
            self.conditions.z_temp.set_raw_value(Unit.CELSIUS(self._profile.c_zero_temperature))
            self.conditions.z_powder_temp.set_raw_value(Unit.CELSIUS(self._profile.c_zero_p_temperature))
            self.conditions.z_angle.set_raw_value(Unit.DEGREE(self._profile.c_zero_w_pitch))
            self.conditions.z_humidity.setValue(self._profile.c_zero_air_humidity)

    def export_a7p(self):

        self._profile.profile_name = self.weapon.profile_name.text()
        self._profile.cartridge_name = self.weapon.caliber.text()
        self._profile.short_name_top = self.weapon.tileTop.text()
        self._profile.short_name_bot = self.bullet.tileBot.text()
        self._profile.r_twist = int((self.weapon.twist.raw_value() >> Unit.INCH) * 100)
        self._profile.sc_height = int(self.weapon.sh.raw_value() >> Unit.MILLIMETER)
        self._profile.twist_dir = 1 if self.weapon.rightTwist.isChecked() else 0

        self._profile.cartridge_name = self.cartridge.cartridge_name.text()
        self._profile.c_muzzle_velocity = int((self.cartridge.mv.raw_value() >> Unit.MPS) * 10)
        self._profile.c_t_coeff = int((self.cartridge.ts.value()) * 1000)

        self._profile.bullet_name = self.bullet.bullet_name.text()
        self._profile.b_weight = int((self.bullet.weight.raw_value() >> Unit.GRAIN) * 10)
        self._profile.b_length = int((self.bullet.length.raw_value() >> Unit.INCH) * 1000)
        self._profile.b_diameter = int((self.bullet.diameter.raw_value() >> Unit.INCH) * 1000)

        self._profile.user_note = self.a7p_meta.user_note.toPlainText()
        self._profile.zero_x = int(self.a7p_meta.zero_x.value() * -1000)
        self._profile.zero_y = int(self.a7p_meta.zero_y.value() * 1000)

        coef_rows = []
        if self.bullet.drag_model.currentIndex() == 0:
            self._profile.bc_type = a7p.GType.G1
            for i in range(self.bullet.drag_model.g1.rowCount()):
                v = self.bullet.drag_model.g1.cellWidget(i, 0).raw_value() >> Unit.MPS
                c = self.bullet.drag_model.g1.cellWidget(i, 1).value()
                if v > 0 and c > 0:
                    coef_rows.append(a7p.CoefRow(mv=int(v * 10), bc_cd=int(c * 10000)))

        elif self.bullet.drag_model.currentIndex() == 1:
            self._profile.bc_type = a7p.GType.G7
            for i in range(self.bullet.drag_model.g7.rowCount()):
                v = self.bullet.drag_model.g7.cellWidget(i, 0).raw_value() >> Unit.MPS
                c = self.bullet.drag_model.g7.cellWidget(i, 1).value()
                if v > 0 and c > 0:
                    coef_rows.append(a7p.CoefRow(mv=int(v * 10), bc_cd=int(c * 10000)))

        elif self.bullet.drag_model.currentIndex() == 2:
            self._profile.bc_type = a7p.GType.CUSTOM
            coef_rows = self.bullet.drag_model.cdm.dump_data()

        # TODO: add CDM

        self._profile.user_note = self.a7p_meta.user_note.toPlainText()[:250]
        self._profile.zero_x = int(self.a7p_meta.zero_x.value() / -1000)
        self._profile.zero_y = int(self.a7p_meta.zero_y.value() / 1000)

        zero_dist = int((self.weapon.zero_dist.raw_value() >> Unit.METER) * 100)
        dist_list = self.a7p_meta.distances.dump_data()

        proto_dist_list = [int((d >> Unit.METER) * 100) for d in dist_list]
        if not zero_dist in proto_dist_list:
            proto_dist_list.append(zero_dist)
        proto_dist_list.sort()

        self._profile.c_zero_distance_idx = proto_dist_list.index(zero_dist)
        del self._profile.distances[:]
        self._profile.distances.extend(proto_dist_list)

        del self._profile.coef_rows[:]
        self._profile.coef_rows.extend(coef_rows)

        self._profile.c_zero_air_pressure = int((Unit.HP(1000) >> Unit.HP) * 10)
        self._profile.c_zero_temperature = int(Unit.CELSIUS(15) >> Unit.CELSIUS)
        self._profile.c_zero_p_temperature = int(Unit.CELSIUS(15) >> Unit.CELSIUS)
        self._profile.c_zero_w_pitch = int(Unit.DEGREE(0) >> Unit.DEGREE)
        self._profile.c_zero_air_humidity = int(50)

        if not self._profile.switches:
            # TODO: add switches
            self._profile.switches.extend([
                a7p.SwPos(c_idx=255, zoom=1, distance=10000),
                a7p.SwPos(c_idx=255, zoom=2, distance=20000),
                a7p.SwPos(c_idx=255, zoom=3, distance=30000),
                a7p.SwPos(c_idx=255, zoom=4, distance=100000),
            ])

        return a7p.Payload(profile=self._profile)

    def validate(self):
        childs = [ch for ch in self.findChildren(QtWidgets.QWidget) if hasattr(ch, 'valid')]
        try:
            for ch in childs:
                assert ch.valid()
            return True
        except AssertionError:
            QtWidgets.QMessageBox.warning(
                self,
                "Warning!",
                "Invalid profile data!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
        return False

    def create_name(self):
        return f"{self.weapon.tileTop.text()}_" \
               f"{self.bullet.tileBot.text()}_" \
               f"{self.bullet.bullet_name.text()}.a7p".replace(" ", "_")
