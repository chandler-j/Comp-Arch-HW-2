# Class to interpret the input instructions

# from InstructionOperation import InstructionPicker
from Registers import Registers
from Registers import RegistersOptions
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
        #print(fields)
      
        # grab instruction length
        ins_len = len(fields)

        # grab the instruction to be completed 
        # validate it's a valid instruction
        # return the binary representation of the opcode
        operation = fields[0].upper()
        opcode = self.get_opcode(operation)
        binins.extend(opcode)
        # validates length and operation
        self.validate_length(ins_len, operation)

        # populate the target 
        # validates the target ( it will always be a register)
        # return the binary representation of the target register
        target = fields[1]
        tarcode = self.get_regcode(target)
        # opcode.extend(self.get_regcode(target))

        binins.extend(tarcode)
        # populate op_a, and op_b
        # in 3 arg instructions, op_a == target
        # validate the operands
        op_a, op_b = fields[len(fields) -2 : len(fields)]

        operandcodes = self.get_operandcodes(op_a, op_b, ins_len)

        binins.extend(operandcodes)
        # opcode.extend(operandcodes)

        #print(opcode)
        self.print_instruction(ins_len, fields, opcode.to01(), tarcode.to01(), operandcodes.to01(), binins.to01())
    
        ins = Instruction(operation, target, op_a, op_b, ins_len)
        return ins

    def print_instruction(self, ins_len, fields, opcode, tarcode, operandcodes, binins):
        headers = "{:^12} : {:^12} : {:^12} : {:^12}"
        field_val = "{:<12} : {:<12} : {:<12} : {:<12}"
        field_bins = "{:<12} : {:<12} : {:<12} : {:<12}"


        short_headers = "{:^12} : {:^12} : {:^12}"
        short_val = "{:<12} : {:<12} : {:<12}"
        short_bins = "{:<12} : {:<12} : {:<12}"
                        
        print(binins)
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

    def get_opcode(self, operation):
        if operation not in OperationCode._member_names_:
            sys.exit("INVALID INSTRUCTION")
        return bitarray(getattr(OperationCode, operation).value)

    def get_regcode(self, register):
        if register not in RegistersOptions._member_names_:
            sys.exit("INVALID REGISTER")
        return  bitarray(getattr(RegistersOptions, register).value)

    def validate_length(self, length, operand):
        immediates=["ADDI", "SUBI","MULI", "DIVI"]
        if length == 3:
            if operand not in immediates:
                sys.exit("INVALID INSTRUCTION LENGTH")
        elif length == 4:
            if operand in immediates:
                sys.exit("INVALID INSTRUCTION LENGTH")
        else:
            sys.exit("INVALID INSTRUCTION LENGHT")

    def get_operandcodes(self, op_a, op_b, length):
        if length == 3:
            opa = self.get_int(op_b)
        elif length == 4:
            opa = self.get_regcode(op_a)
            opa.extend(self.get_regcode(op_b))
        else:
           sys.exit("INVALID INSTRUCTION LENGTH")
        return opa

    def get_int(self, integer):
        if not integer.isdigit():
            sys.exit("MUST PASS INTEGER TO IMMEDIATE INSTRUCTION")
        else:
            integer = int(integer)
            word = bitarray('11111111')
            opb = ''
            if integer >= 256:
                opb = word
            else:
                opb = int2ba(int(integer), 8)
                opb &= word
            return opb

           
