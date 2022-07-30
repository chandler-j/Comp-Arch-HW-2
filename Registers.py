import enum

class RegistersOptions(enum.Enum):
    R1 = 0b01
    R2 = 0b10
    R3 = 0b11

class Registers(object):
    def __init__(self):
        self.RegValues = dict()

        for register in range(RegistersOptions.R1.value, (RegistersOptions.R3.value+1)):
            self.RegValues[register] = 0x00

    def saveReg(self, register, value):
        self.RegValues[register] = value

    def getReg(self, register):
        return self.RegValues[register]