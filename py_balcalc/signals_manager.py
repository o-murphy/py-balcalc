from PySide6.QtCore import QObject, Signal


class SignalsManager(QObject):
    settings_units_updated = Signal()
    settings_locale_updated = Signal()
    translator_updated = Signal()


appSignalMgr = SignalsManager()
