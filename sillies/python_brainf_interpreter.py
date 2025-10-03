# Hello World Program:
# ++++++[>++++++++++++<-]>.[-]<++++[>+++++++++++++++++++++++++<-]>+.+++++++..+++.[-]<++++[>+++++++++++<-]>.------------.[-]<++++++++[>+++++++++++++++<-]>-.--------.+++.------.--------.[-]<+++[>+++++++++++<-]>.
code = input("Input Brainfuck code: ")
loop_start = []
memory = []
for i in range(65535):
    memory.append(0)
idx = 0
pointer = 0
output = ""
while idx < len(code):
    match code[idx]:
        case ">":
            pointer = (pointer+1)%65535
        case "<":
            pointer = (pointer-1)%65535
        case "+":
            memory[pointer] = (memory[pointer]+1)%256
        case "-":
            memory[pointer] = (memory[pointer]-1)%256
        case ".":
            output += chr(memory[pointer])
        case ",":
            memory[pointer] = ord(input("Input required: "))
        case "[":
            loop_start.append(idx)
        case "]":
            if memory[pointer] == 0:
                loop_start.pop()
            else:
                idx = loop_start[-1]
    idx += 1
print("Output:")
print(output)