char_array = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open ('input.txt', 'r') as file:
    inputs = [i.replace('\n','') for i in file.readlines()]

total_priority = 0

for line in inputs:
    #split them in half
    halfway = int(len(line) / 2) 
    first_half = line[0:halfway]
    second_half = line[halfway:]

    common_char = list(set(first_half)&set(second_half))[0]
    total_priority += char_array.index(common_char) + 1

print(f"Part 1 answer: {total_priority}")

total_priority = 0

for i in range(0, len(inputs), 3):
    common_char = list(set(inputs[i])&set(inputs[i+1])&set(inputs[i+2]))[0]
    total_priority += char_array.index(common_char) + 1


print(f"Part 2 answer: {total_priority}")