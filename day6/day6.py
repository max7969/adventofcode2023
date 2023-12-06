import re
import math


def part1(content):
    times = [int(match.group(1)) for match in re.finditer(r' +(\d+)', content[0])]
    distances = [int(match.group(1)) for match in re.finditer(r' +(\d+)', content[1])]
    couples = [[times[i - 1], distances[i - 1]] for i in range(len(times))]

    result = 1
    for couple in couples:
        solutions = []
        for i in range(1, couple[0]):
            if (couple[0] - i) * i > couple[1]:
                solutions.append(i)
                break
        for i in range(couple[0], 1, -1):
            if (couple[0] - i) * i > couple[1]:
                solutions.append(i)
                break
        result = result * (solutions[1] - solutions[0] + 1)  
    return result

def part2(content):
    time = int(''.join([match.group(1) for match in re.finditer(r' +(\d+)', content[0])]))
    distance = int(''.join([match.group(1) for match in re.finditer(r' +(\d+)', content[1])]))
    couple = [time, distance]
    solutions = []
    for i in range(1, couple[0]):
        if (couple[0] - i) * i > couple[1]:
            solutions.append(i)
            break
    for i in range(couple[0], 1, -1):
        if (couple[0] - i) * i > couple[1]:
            solutions.append(i)
            break
    return (solutions[1] - solutions[0] + 1)