with open ('input.txt', 'r') as file:
    inputs = [i.replace('\n','').split(" ") for i in file.readlines()]

stacks_inputs = inputs[:8]

for stacks_input in stacks_inputs:
    print(stacks_input)

instructions_inputs = inputs[10:]
stacks = [[],[],[],[],[],[],[],[],[]]

for i in reversed(range(len(stacks_inputs[0]))):
    for j in range(len(stacks_inputs)):
        stacks[i].append(stacks_inputs[j][i])
for stack in stacks:
    print(stack)

for stack in stacks:
    for i in range(len(stack)):
        if '[0]' in stack:
            stack.remove('[0]')

stacks.insert(0,[])

for stack in stacks:
    print(stack)

for instruction in instructions_inputs:
    print(instruction)
    count = int(instruction[1])
    from_list = int(instruction[3])
    to_list = int(instruction[5])
    for c in range(count):
        stacks[to_list].insert(0, stacks[from_list].pop(0))

stack_tops = []
stacks.remove([])

for stack in stacks:
    stack_tops.append(stack.pop(0))
empty_str = ""

print(f"Part 1 answer: {empty_str.join(stack_tops).replace('[', '').replace(']','')}")
