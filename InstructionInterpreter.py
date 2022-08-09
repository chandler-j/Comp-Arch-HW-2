# Class to interpret the input instructions

# from InstructionOperation import InstructionPicker
from Registers import Registers
from Registers import RegistersOptions
from Memory import Memory
from Memory import MemoryOptions
from InstructionOperation import OperationCode
#from InstructionOperation import InstructionType
from InstructionOperation import Instruction
import sys
from bitarray import bitarray
from bitarray.util import int2ba
#from InstructionOperation import Execute

import re
"""
Interprets the text file and chooses the registers, opcode, instruction type, and immediate value
"""
class InstructionInterpreter():
    def __init__(self):
        self.Regs = Registers()
        self.regex = " |, "

    """
    RType instruction format: <add,sub,mul,div> <R1,R2,R3>
    IType instruction format: <addi,subi,muli,divi> <R1,R2,R3>, <immediate#>
    """
    def interpretFile(self, instruction):
        binins = bitarray()
        """
        parse instructions
        """
        fields = re.split(self.regex, instruction.strip("\n"))
     
        binins.extend(self.verify_fields(fields))
        
        ins_len = len(fields)
        operation = fields[0].upper()
        target = fields[1]
        op_a, op_b = fields[len(fields) -2 : len(fields)]

        self.print_instruction(ins_len, fields, binins[0:4].to01(), binins[4:8].to01(), binins[8:16].to01(), binins.to01(), instruction.strip("\n"))
    
        ins = Instruction(operation, target, op_a, op_b, ins_len)
        return ins

        
    def get_opcode(self, operation):
        if operation not in OperationCode._member_names_:
            sys.exit("INVALID INSTRUCTION")
        return bitarray(getattr(OperationCode, operation).value)

    def get_memcode(self, memory):
        if memory not in MemoryOptions._member_names_:
            sys.exit("INVALID MEMORY ADDRESS {}".format( memory))
        return  bitarray(getattr(MemoryOptions, memory).value)

    def get_regcode(self, register):
        if register not in RegistersOptions._member_names_:
            sys.exit("INVALID REGISTER {}".format( register))
        return  bitarray(getattr(RegistersOptions, register).value)

    def get_int(self, integer):
        pos_word = bitarray('01111111')
        neg_word = bitarray('11111111')
        opb = ''
        if integer >= 126:
            opb = pos_word
        elif integer <= -127:
            opb = neg_word
        else:
            opb = int2ba(int(integer), 8)
            opb &= neg_word
        return opb

    def check_int(self, op_b):
        try:
            if int(op_b) > 126:
                op_b = 126
            elif int(op_b) < -127:
                op_b = -127
            return int(op_b)
        except ValueError:
            sys.exit("IMMEDIATE INSTRUCTION REQUIRES INT OPERAND")

    def print_instruction(self, ins_len, fields, opcode, tarcode, operandcodes, binins, instruction):
        headers = "{:^12} : {:^12} : {:^12} : {:^12}"
        field_val = "{:<12} : {:<12} : {:<12} : {:<12}"
        field_bins = "{:<12} : {:<12} : {:<12} : {:<12}"

        short_headers = "{:^12} : {:^12} : {:^12}"
        short_val = "{:<12} : {:<12} : {:<12}"
        short_bins = "{:<12} : {:<12} : {:<12}"
                        
        print(">> {} ---> {}".format( instruction, binins))
        if ins_len == 4:
            print(headers.format("operation", "target", "operand A", "operand B"))
            print("-------------------------------------------------------------")
            print(field_val.format(fields[0], fields[1], fields[2], fields[3]))
            print(field_bins.format(opcode, tarcode, operandcodes[0:4], operandcodes[4:8]))
        if ins_len == 3:
            print(short_headers.format("operation", "target", "operand A"))
            print("-------------------------------------------------------------")
            print(short_val.format(fields[0], fields[1], fields[2]))
            print(short_bins.format(opcode, tarcode, operandcodes))

    def verify_fields(self, fields):
        fields[0] = fields[0].upper()
        REGULAR = ["ADD", "SUB", "MUL", "DIV"]
        IMMEDIATE = ["ADDI", "SUBI", "MULI", "DIVI"]
        MEMORY = ["LD", "STR"]
        instruction = bitarray()
        instruction.extend(self.get_opcode(fields[0]))
        if fields[0] in REGULAR:
            instruction.extend(self.verify_regular(fields))
        elif fields[0] in IMMEDIATE:
            instruction.extend(self.verify_immediate(fields))
        elif fields[0] in MEMORY:
            instruction.extend(self.verify_memory(fields))
            instruction.extend('0000')
        else:
            sys.exit("INVALID COMMAND")
        return instruction

    def verify_regular(self, fields):
        if len(fields) != 4:
            sys.exit("INVALID NUMBER OF ARGUMENTS TO {}".format(fields[0]))

        registers = bitarray()
        for reg in fields[1:]:
            registers.extend(self.get_regcode(reg))
        return registers

    def verify_immediate(self, fields):
        if len(fields) != 3:
            sys.exit("INVALID NUMBER OF ARGUMENTS TO {}".format(fields[0]))
        operands = bitarray()
        operands.extend(self.get_regcode(fields[1]))
        try:
            operands.extend(self.get_int(int(fields[2])))
        except ValueError:
            sys.exit("INVALID OPERAND {}".format(fields[2]))
        return operands

    def verify_memory(self, fields):
        if len(fields) != 3:
            sys.exit("INVALID NUMBER OF ARGUMENTS TO {}".format(fields[0]))
        addresses = bitarray()
        if fields[0] == "LD":
            addresses.extend(self.get_regcode(fields[1]))
            addresses.extend(self.get_memcode(fields[2]))
        else:
            addresses.extend(self.get_memcode(fields[1]))
            addresses.extend(self.get_regcode(fields[2]))
        return addresses
