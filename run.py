from InstructionInterpreter import InstructionInterpreter
from Registers import Registers
from Registers import RegistersOptions
from Memory import MemoryOptions
from Memory import Memory
from InstructionOperation import Executer
from InstructionOperation import OperationCode

"""
Simple run file to open instructions.txt file and begin interpretation and writing to registers
"""
file = open('instructions.txt', 'r')
interpreter = InstructionInterpreter()
executer = Executer(Registers(), Memory())
for line in file.readlines():
    
    # parse and build instruction
    instruction = interpreter.interpretFile(instruction=line)

    print("Registers Before: ", executer.registers.RegValues)
    print("Memory Before   : ", executer.memory.MemValues)
    # execute instruction
    executer.execute(instruction)

    print("Registers After : ", executer.registers.RegValues)
    print("Memory After    : ", executer.memory.MemValues)
    print("")
