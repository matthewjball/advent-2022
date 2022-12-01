with open ('input.txt', 'r') as file:
    inputs = [str(i.replace('\n','')) for i in file.readlines()]

totals = []

cur = 0

for line in inputs:
    if line == "":
        totals.append(cur)
        cur = 0
    else:
        cur += int(line)

print(f"Part 1 answer: {max(totals)}")

totals.sort()
print(f"Part 2 answer: {sum(totals[len(totals)-3:])}")