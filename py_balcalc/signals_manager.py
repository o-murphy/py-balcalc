from PySide6.QtCore import QObject, Signal


class SignalsManager(QObject):
    appSettingsUpdated = Signal()


appSignalMgr = SignalsManager()
