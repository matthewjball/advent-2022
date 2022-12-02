with open ('input.txt', 'r') as file:
    inputs = [i.replace('\n','').split(" ") for i in file.readlines()]

score = 0

for game in inputs:
    key = game[0]
    val = game[1]

    match key:
        case "A":
            match val:
                case "X":
                    score += 4
                case "Y":
                    score += 8
                case "Z":
                    score += 3
        case "B":
            match val:
                case "X":
                    score += 1
                case "Y":
                    score += 5
                case "Z":
                    score += 9
        case "C":
            match val:
                case "X":
                    score += 7
                case "Y":
                    score += 2
                case "Z":
                    score += 6

print(f"Part 1 answer: {score}")

score = 0

for game in inputs:
    key = game[0]
    val = game[1]

    match key:
        case "A":
            match val:
                case "X":
                    score += 3
                case "Y":
                    score += 4
                case "Z":
                    score += 8
        case "B":
            match val:
                case "X":
                    score += 1
                case "Y":
                    score += 5
                case "Z":
                    score += 9
        case "C":
            match val:
                case "X":
                    score += 2
                case "Y":
                    score += 6
                case "Z":
                    score += 7

print(f"Part 2 answer: {score}")
