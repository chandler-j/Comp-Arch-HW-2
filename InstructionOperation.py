# Classes for the instruction types

from abc import abstractmethod
from Registers import RegistersOptions
import enum

class OperationCode(enum.Enum):
    ADD = 0b00
    SUB = 0b01
    MUL = 0b10
    DIV = 0b11

class InstructionType(enum.Enum):
    TypeR = 0
    TypeI = 1

class Instruction(object):
    def __init__(self, opcode, register, registers, immediate=None):
        self.registers = registers
        self.opcode = opcode
        self.register = register
        self.immediate = immediate

    @abstractmethod
    def performOperation(self):
        pass

class TypeI(Instruction):
    def __init__(self, opcode, register, registers, immediate):
        super().__init__(opcode=opcode, register=register, registers=registers, immediate=immediate)

    def performOperation(self):
        if self.opcode == OperationCode.ADD.value:
            save_value = self.registers.getReg(self.register) + int(self.immediate)
        elif self.opcode == OperationCode.SUB.value:
            save_value = self.registers.getReg(self.register) - int(self.immediate)
        elif self.opcode == OperationCode.MUL.value:
            save_value = self.registers.getReg(self.register) * int(self.immediate)
        elif self.opcode == OperationCode.DIV.value:
            save_value = self.registers.getReg(self.register) / int(self.immediate)
        return save_value

class TypeR(Instruction):
    def __init__(self, opcode, register, registers):
        super().__init__(opcode=opcode, register=register, registers=registers)

    def performOperation(self):
        if self.register == RegistersOptions.R1.value:
            if self.opcode == OperationCode.ADD.value:
                save_value = self.registers.getReg(RegistersOptions.R2.value) + self.registers.getReg(RegistersOptions.R3.value)
            elif self.opcode == OperationCode.SUB.value:
                save_value = self.registers.getReg(RegistersOptions.R2.value) - self.registers.getReg(RegistersOptions.R3.value)
            elif self.opcode == OperationCode.MUL.value:
                save_value = self.registers.getReg(RegistersOptions.R2.value) * self.registers.getReg(RegistersOptions.R3.value)
            elif self.opcode == OperationCode.DIV.value:
                save_value = self.registers.getReg(RegistersOptions.R2.value) / self.registers.getReg(RegistersOptions.R3.value)
        elif self.register == RegistersOptions.R2.value:
            if self.opcode == OperationCode.ADD.value:
                save_value = self.registers.getReg(RegistersOptions.R1.value) + self.registers.getReg(RegistersOptions.R3.value)
            elif self.opcode == OperationCode.SUB.value:
                save_value = self.registers.getReg(RegistersOptions.R1.value) - self.registers.getReg(RegistersOptions.R3.value)
            elif self.opcode == OperationCode.MUL.value:
                save_value = self.registers.getReg(RegistersOptions.R1.value) * self.registers.getReg(RegistersOptions.R3.value)
            elif self.opcode == OperationCode.DIV.value:
                save_value = self.registers.getReg(RegistersOptions.R1.value) / self.registers.getReg(RegistersOptions.R3.value)
        elif self.register == RegistersOptions.R3.value:
            if self.opcode == OperationCode.ADD.value:
                save_value = self.registers.getReg(RegistersOptions.R1.value) + self.registers.getReg(RegistersOptions.R2.value)
            elif self.opcode == OperationCode.SUB.value:
                save_value = self.registers.getReg(RegistersOptions.R1.value) - self.registers.getReg(RegistersOptions.R2.value)
            elif self.opcode == OperationCode.MUL.value:
                save_value = self.registers.getReg(RegistersOptions.R1.value) * self.registers.getReg(RegistersOptions.R2.value)
            elif self.opcode == OperationCode.DIV.value:
                save_value = self.registers.getReg(RegistersOptions.R1.value) / self.registers.getReg(RegistersOptions.R2.value)
        return save_value

class InstructionTypePicker(object):
    def __init__(self, registers):
        self.registers = registers

    def chooseInstructionType(self, instructionType, opcode, register, immediate=None):
        if instructionType == InstructionType.TypeI.value:
            from InstructionOperation import TypeI as Instruction
            instruction = Instruction(opcode, register, self.registers, immediate)
        elif instructionType == InstructionType.TypeR.value:
            from InstructionOperation import TypeR as Instruction
            instruction = Instruction(opcode, register, self.registers)

        
        value = instruction.performOperation()
        self.registers.saveReg(register, value)