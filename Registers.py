import enum

"""
Register options
"""
class RegistersOptions(enum.Enum):
    R1 = '0001'
    R2 = '0010'
    R3 = '0100'
    R4 = '1000'

"""
Create our registers with their initial values
"""
class Registers(object):
    def __init__(self):
        self.RegValues = dict()

        for register in RegistersOptions._member_names_:
            self.RegValues[register] = 0x00

    """
    Saves value to Register
    """
    def saveReg(self, register, value):
        # registers are only 16 bit, max value = 65535
        if value > 65535:
            value = 65535
        self.RegValues[register] = value

    """
    Gets value from Register
    """
    def getReg(self, register):
        return self.RegValues[register]

