with open ('input.txt', 'r') as file:
    inputs = file.readlines()[0]

stack = []
for i in range(len(inputs)):
    stack.insert(0, inputs[i])
    if len(stack) > 4:
        stack.pop()
    
    if len(stack) == len(list(set(stack))) and len(stack) == 4:
        print(f"Part 1 answer: {i + 1}")
        break

for i in range(len(inputs)):
    stack.insert(0, inputs[i])
    if len(stack) > 14:
        stack.pop()
    
    if len(stack) == len(list(set(stack))) and len(stack) == 14:
        print(f"Part 2 answer: {i + 1}")
        break
