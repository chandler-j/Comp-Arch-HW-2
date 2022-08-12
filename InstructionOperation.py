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
    DIVI = '1101'
    STR  = '1011'
    LD   = '1111'

"""
Base class for our instructions
"""

class Instruction(object):
    def __init__(self, operation, target, op_a, op_b, ins_len, bin_ins):
        
        self.operation = operation
        self.target = target
        self.op_a = op_a
        self.op_b = op_b
        self.ins_len = ins_len
        self.bin_ins = bin_ins


"""
Picks which instruction type based on instructionType bit setting
"""
class Executer:
    def __init__(self, registers, memory):
        self.registers = registers
        self.memory = memory
        self.operations = {}
        self.operations["ADD"]   = self.add
        self.operations["SUB"]   = self.sub
        self.operations["MUL"]   = self.mul
        self.operations["DIV"]   = self.div
        self.operations["ADDI"]  = self.addi
        self.operations["SUBI"]  = self.subi
        self.operations["MULI"]  = self.muli
        self.operations["DIVI"]  = self.divi
        self.operations["LD"]    = self.load
        self.operations["STR"]  = self.store

    def execute(self,instruction):


        if instruction.operation in ["LD", "STR"]:
            val = self.operations[instruction.operation](instruction.op_b)
            if instruction.operation == "LD":
                self.saveReg(instruction.target, val)
            else:
                self.saveMem(instruction.target, val)
        else:
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
        try:
            return int(self.registers.getReg(a) / self.registers.getReg(b))
        except ZeroDivisionError:
            sys.exit("Division BY 0 ERROR")

    def addi(self, a, b):
        return self.registers.getReg(a) + int(b)
        
    def subi(self, a, b):
        return self.registers.getReg(a) - int(b)

    def muli(self, a, b):
        return self.registers.getReg(a) * int(b)

    def divi(self, a, b):
        try:
            return int(self.registers.getReg(a) / int(b))
        except ZeroDivisionError:
            sys.exit("DIVISION BY 0 ERROR")

    def saveReg(self, target, value):
        self.registers.saveReg(target, value)

    def saveMem(self, target, value):
        self.memory.saveMem(target, value) 

    def load(self, memaddr):
        print("Do Load Thing")
        return self.memory.getMem(memaddr)
        # get from memory  

    def store(self, register):
        print("Do Store Thing")
        return self.registers.getReg(register)
        # put in memory

  
