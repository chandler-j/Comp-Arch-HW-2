# Class to interpret the input instructions

from InstructionOperation import InstructionPicker
from Registers import Registers
from Registers import RegistersOptions
from InstructionOperation import OperationCode
from InstructionOperation import InstructionType

"""
Interprets the text file and chooses the registers, opcode, instruction type, and immediate value
"""
class InstructionInterpreter():
    def __init__(self):
        self.Regs = Registers()

    """
    RType instruction format: <add,sub,mul,div> <R1,R2,R3>
    IType instruction format: <addi,subi,muli,divi> <R1,R2,R3>, <immediate#>
    """
    def interpretFile(self, instruction):
        # If there's a comma, it's an immediate instruction
        if ',' in instruction: 
            immediate = instruction.split(', ')[1]
            immediate = immediate.split('\n')[0]
        else: immediate=None

        # Choose the register for the instruction
        if 'R1' in instruction:
            register = RegistersOptions.R1.value
        elif 'R2' in instruction:
            register = RegistersOptions.R2.value
        elif 'R3' in instruction:
            register = RegistersOptions.R3.value

        # Choose the opcode for the instruction
        if 'add' in instruction:
            opcode = OperationCode.ADD.value
        elif 'sub' in instruction:
            opcode = OperationCode.SUB.value
        elif 'mul' in instruction:
            opcode = OperationCode.MUL.value
        elif 'div' in instruction:
            opcode = OperationCode.DIV.value
        
        # If there's an i at the end of the instruction, it's an immediate instruction
        if 'i' in instruction and not 'div ' in instruction:
            instruction_type = InstructionType.TypeI.value
        else:
            instruction_type = InstructionType.TypeR.value

        # Perform the instruction on registers
        InstructionPicker(registers=self.Regs).performInstruction(instructionType=instruction_type, opcode=opcode, register=register, immediate=immediate)


