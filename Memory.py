import enum

"""
Memory options
"""
class MemoryOptions(enum.Enum):
    M1 = '0001'
    M2 = '0010'
    M3 = '0100'
    M4 = '1000'

"""
Create our registers with their initial values
"""
class Memory(object):
    def __init__(self):
        self.MemValues = dict()

        for memory in MemoryOptions._member_names_:
            self.MemValues[memory] = 0x00

    """
    Saves value to Memory
    """
    def saveMem(self, memory, value):
        # memory is only 16 bit, max value = 32767
        if value > 32767:
            value = 32767
        elif value < -32768:
            value = -32768
        self.MemValues[memory] = value

    """
    Gets value from Memory
    """
    def getMem(self, memory):
        return self.MemValues[memory]

