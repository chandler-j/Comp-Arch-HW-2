from InstructionInterpreter import InstructionInterpreter
from Registers import Registers
from Registers import RegistersOptions
from InstructionOperation import Executer
from InstructionOperation import OperationCode

"""
Simple run file to open instructions.txt file and begin interpretation and writing to registers
"""
file = open('instructions.txt', 'r')
interpreter = InstructionInterpreter()
executer = Executer(Registers())
for line in file.readlines():
    """
    print("R1: ", RegistersOptions.R1.value)
    print("R2: ", RegistersOptions.R2.value)
    print("R3: ", RegistersOptions.R3.value)
    print("ADD: ", OperationCode.ADD.value)
    print("SUB: ", OperationCode.SUB.value)
    print("MUL: ", OperationCode.MUL.value)
    print("DIV: ", OperationCode.DIV.value)
    print("ADDI: ", OperationCode.ADDI.value)
    print("SUBI: ", OperationCode.SUBI.value)
    print("MULI: ", OperationCode.MULI.value)
    print("DIVI: ", OperationCode.DIVI.value)
    """
    # parse and build instruction
    print(">> ", line.strip("\n"))
    instruction = interpreter.interpretFile(instruction=line)


    print("Registers Before: ", executer.registers.RegValues)
    # execute instruction
    executer.execute(instruction)

    print("Registers After : ", executer.registers.RegValues)
    print("")
