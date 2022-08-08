# Classes for the instruction types

from abc import abstractmethod
from Registers import RegistersOptions
import enum
import sys
from bitarray import bitarray
from bitarray.util import int2ba

"""
Opcode Options
"""
class OperationCode(enum.Enum):
    ADD =  '0000'
    SUB =  '0001'
    MUL =  '0010'
    DIV =  '0011'
    ADDI = '1000'
    SUBI = '1001'
    MULI = '1010'
    DIVI = '1011'

"""
Base class for our instructions
"""

class Instruction(object):
    def __init__(self, operation, target, op_a, op_b, ins_len):
        
        self.operation = operation
        self.target = target
        self.op_a = op_a
        self.op_b = op_b
        self.ins_len = ins_len


"""
Picks which instruction type based on instructionType bit setting
"""
class Executer:
    def __init__(self, registers):
        self.registers = registers
        self.operations = {}
        self.operations["ADD"]   = self.add
        self.operations["SUB"]   = self.sub
        self.operations["MUL"]  = self.mul
        self.operations["DIV"]   = self.div
        self.operations["ADDI"]  = self.addi
        self.operations["SUBI"]  = self.subi
        self.operations["MULI"] = self.muli
        self.operations["DIVI"]  = self.divi

    def execute(self,instruction):


        val = self.operations[instruction.operation](instruction.op_a, instruction.op_b)
        self.registers.saveReg(instruction.target, val)

        return 0


    def add(self, a, b):
        return self.registers.getReg(a) + self.registers.getReg(b)
        
    def sub(self, a, b):
        return self.registers.getReg(a) - self.registers.getReg(b)

    def mul(self, a, b):
        return self.registers.getReg(a) * self.registers.getReg(b)

    def div(self, a, b):
        return self.registers.getReg(a) / self.registers.getReg(b)

    def addi(self, a, b):
        return self.registers.getReg(a) + int(b)
        
    def subi(self, a, b):
        return self.registers.getReg(a) - int(b)

    def muli(self, a, b):
        return self.registers.getReg(a) * int(b)

    def divi(self, a, b):
        return self.registers.getReg(a) / int(b)

  
