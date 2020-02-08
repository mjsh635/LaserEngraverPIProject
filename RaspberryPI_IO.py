"""Raspberry Pi code to set the value for a
laser printers power settings remotely instead
of having to use the hardware buttons.
"""


class RPIO:
    """Class that handles the control of hardware for
    the raspberryPi-Laser project
    """
    import time
    import RPi.GPIO as GPIO
    
    def __init__(self):
        """ import the RPIO and set the 
        mode to BCM, then set the mode for 
        the list of pins to output
        pin 04 => - 10
        pin 17 => + 10
        pin 27 => +   1
        pin 22 => + 0.1
        """
        # self.GPIO = GPIO
        self.GPIO.setwarnings(False)
        self.GPIO.setmode(self.GPIO.BCM)
        self.pins = [4,17,27,22]
        for pin in self.pins:
            self.GPIO.setup(pin, self.GPIO.OUT)

    def _home_settings(self):
        for _ in range(1,11):
            self.GPIO.output(4, True)
            print(f"minus {10*_}",end='\r')
            self.time.sleep(0.0675)
            self.GPIO.output(4, False)
        print("Value homed at 0 %")
            

    def _add_10_percent(self, tens : int):
        for _ in range(1,tens+1):
            self.GPIO.output(17, True)
            print(f"adding {10*_}",end='\r')
            self.time.sleep(0.0675)
            self.GPIO.output(17, False)
        print(f"added {10*tens}               ")

    def _add_1_percent(self, ones:int):
        for _ in range(1,ones+1):
            self.GPIO.output(27, True)
            print(f"adding {1*_}",end='\r')
            self.time.sleep(0.0675)
            self.GPIO.output(27, False)
        print(f"added {1*ones}               ")


    def _add_point_1_percent(self,pnt_ones:int):
        for _ in range(1,pnt_ones+1):
            self.GPIO.output(22, True)
            print(f"adding {float}",end='\r')
            self.time.sleep(0.0675)
            self.GPIO.output(22, False)
        print(f"\nadded {float(0.1)*pnt_ones}               ")

    def get_value(self):
        return NotImplemented

    def set_value(self, target: float) -> bool:
        return NotImplemented


rpi = RPIO()
rpi._home_settings()
rpi._add_10_percent(5)
rpi._add_1_percent(5)
rpi._add_point_1_percent(5)

