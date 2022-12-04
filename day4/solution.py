with open ('input.txt', 'r') as file:
    inputs = [i.replace('\n','').split(",") for i in file.readlines()]

contained_pairs = 0

for line in inputs:
    first_lower = int(line[0].split("-")[0])
    first_upper = int(line[0].split("-")[1])
    second_lower = int(line[1].split("-")[0])
    second_upper = int(line[1].split("-")[1])

    if (first_lower >= second_lower and first_upper <= second_upper):
        contained_pairs += 1
    elif (first_lower <= second_lower and first_upper >= second_upper):
        contained_pairs += 1

print(f"Part 1 answer: {contained_pairs}")

contained_pairs = 0

for line in inputs:
    first_lower = int(line[0].split("-")[0])
    first_upper = int(line[0].split("-")[1])
    second_lower = int(line[1].split("-")[0])
    second_upper = int(line[1].split("-")[1])

    if not (first_lower > second_upper or first_upper < second_lower):
        contained_pairs += 1

print(f"Part 2 answer: {contained_pairs}")