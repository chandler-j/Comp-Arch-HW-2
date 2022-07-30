from InstructionInterpreter import InstructionInterpreter

file = open('instructions.txt', 'r')
interpreter = InstructionInterpreter()
for line in file.readlines():
    interpreter.interpretFile(line)
    print(interpreter.Regs.RegValues)