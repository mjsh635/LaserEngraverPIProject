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
        # variables to be used throughout the class
        self.last_set_value = 0.0
        self.relay_settle_time = 0.0675

        # self.GPIO.setwarnings(False)
        # Set the mode to BCM (the chip used in RPI)
        # this determines how the pins should be 
        # addressed.
        self.GPIO.setmode(self.GPIO.BCM)

        # Pin array that should be set to outputs
        self.output_pins = [4,17,27,22]
        # Loop over the pin array setting each pin
        # to an output as it goes
            self.GPIO.setup(pin, self.GPIO.OUT)

    def _home_settings(self):
        """Set the power setting to zero by
        subtracting 10% 10 times
        """
        # Loop for 10 cycles to zero the power level out
        for _ in range(1,11):
            # Toggle the power ON
            self.GPIO.output(4, True)
            print(f"minus {10*_}",end='\r')
            # Time for the relay to settle
            self.time.sleep(self.relay_settle_time)
            # Toggle the power OFF
            self.GPIO.output(4, False)
        print("Value homed at 0 %                           ")
            

    def _add_10_percent(self, tens : int):
        """Add 10% power level 
        """
        # Loop for the required 10's to add
        for _ in range(1,tens+1):
            # Toggle relay ON
            self.GPIO.output(17, True)
            print(f"adding {10*_}",end='\r')
            # time for the relay to settle
            self.time.sleep(self.relay_settle_time)
            # Toggle relay OFF
            self.GPIO.output(17, False)
        print(f"added {10*tens}                              ")

    def _add_1_percent(self, ones:int):
        """Add 1% power level
        """
        # Loop for the required 1's to add
        for _ in range(1,ones+1):
            # Toggle relay ON
            self.GPIO.output(27, True)
            print(f"adding {1*_}",end='\r')
            # Time for the relay to settle
            self.time.sleep(self.relay_settle_time)
            # Toggle relay OFF
            self.GPIO.output(27, False)
        print(f"added {1*ones}                              ")


    def _add_point_1_percent(self, pnt_ones:int):
        """Add 0.1% power level
        """
        # Loop for the required 0.1's to add
        for _ in range(1,pnt_ones+1):
            # Toggle relay ON
            self.GPIO.output(22, True)
            print(f"adding {float}",end='\r')
            # Time for the relay to settle
            self.time.sleep(self.relay_settle_time)
            # Toggle relay OFF
            self.GPIO.output(22, False)
        print(f"\nadded {float(0.1)*pnt_ones}               ")

    def get_value(self):
        """Return the last set power level
        """
        return self.last_set_value

    def set_value(self, target: float) -> bool:
        """Set the power level desired and return if
        completed successfully
        """
        # count tens and then subtract from total
        #count remaining ones then subtract from total
        #remainder should be point ones
        #call the functions for their values
        #if completed okay then set last set value
        #This should be change, return true if
        #completed okay


rpi = RPIO()
rpi._home_settings()
rpi._add_10_percent(5)
rpi._add_1_percent(5)
rpi._add_point_1_percent(5)

