from InstructionInterpreter import InstructionInterpreter

"""
Simple run file to open instructions.txt file and begin interpretation and writing to registers
"""
file = open('instructions.txt', 'r')
interpreter = InstructionInterpreter()
for line in file.readlines():
    interpreter.interpretFile(line)
    print(interpreter.Regs.RegValues)