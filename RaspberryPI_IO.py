"""Raspberry Pi code to set the value for a
laser printers power settings remotely instead
of having to use the hardware buttons.
"""


class RPIO:
    """Class that handles the control of hardware for
    the raspberryPi-Laser project
    """

    def __init__(self):
        pass

    def _home_settings(self):
        return NotImplemented

    def _add_10_percent(self):
        return NotImplemented

    def _add_1_percent(self):
        return NotImplemented

    def _add_point_1_percent(self):
        return NotImplemented

    def get_value(self):
        return NotImplemented

    def set_value(self, target: float) -> bool:
        return NotImplemented


rpi = RPIO()
