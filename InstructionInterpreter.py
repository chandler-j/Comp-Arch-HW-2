# Class to interpret the input instructions

from InstructionOperation import InstructionTypePicker
from Registers import Registers
from Registers import RegistersOptions
from InstructionOperation import OperationCode
from InstructionOperation import InstructionType

class InstructionInterpreter():
    def __init__(self):
        self.Regs = Registers()

    def interpretFile(self, instruction):
        if ',' in instruction:
            immediate = instruction.split(', ')[1]
            immediate = immediate.split('\n')[0]
        else: immediate=None

        if 'R1' in instruction:
            register = RegistersOptions.R1.value
        elif 'R2' in instruction:
            register = RegistersOptions.R2.value
        elif 'R3' in instruction:
            register = RegistersOptions.R3.value

        if 'add' in instruction:
            opcode = OperationCode.ADD.value
        elif 'sub' in instruction:
            opcode = OperationCode.SUB.value
        elif 'mul' in instruction:
            opcode = OperationCode.MUL.value
        elif 'div' in instruction:
            opcode = OperationCode.DIV.value
        
        if 'i' in instruction and not 'div ' in instruction:
            instruction_type = InstructionType.TypeI.value
        else:
            instruction_type = InstructionType.TypeR.value

        InstructionTypePicker(registers=self.Regs).chooseInstructionType(instructionType=instruction_type, opcode=opcode, register=register, immediate=immediate)


