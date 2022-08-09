sub R2, R1, R2
mul R1, R3, R1
div R2, R3, R3
addi R2, 5
subi R3, 5
muli R2, 2
divi R1, 20
add R1, R2, R3
sub R1, R2, R3
div R1, R2, R2
add R3, R3, R2
mul R3, R1, R2
mul R2, R2, R3
subi R2, 1070
addi R1, 10
div R3, R2, R3

"""
class Instruction(object):
    def __init__(self, opcode, register, registers, immediate=None):
        self.registers = registers
        self.opcode = opcode
        self.register = register
        self.immediate = immediate

    Performs the operation specified by the opcode
    @abstractmethod
    def performOperation(self):
        pass
"""
"""
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
"""

"""
class InstructionPicker(object):
    def __init__(self, registers):
        self.registers = registers

    def performInstruction(self, instructionType, opcode, register, immediate=None):
        if instructionType == InstructionType.TypeI.value:
            from InstructionOperation import TypeI as Instruction
            instruction = Instruction(opcode, register, self.registers, immediate)
        elif instructionType == InstructionType.TypeR.value:
            from InstructionOperation import TypeR as Instruction
            instruction = Instruction(opcode, register, self.registers)

        # Perform instruction operation and save it to register
        value = instruction.performOperation()
        self.registers.saveReg(register, value)
"""

"""
Instruction Type Options
class InstructionType(enum.Enum):
    TypeR = 0
    TypeI = 1
    
"""
