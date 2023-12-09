import re
import math


def part1(content):
    result = 0
    all_results = []
    for line in content:
        numbers = [int(element) for element in line.replace("\n","").split(" ")]
        placeholders = []
        while sum([abs(number) for number in numbers]) != 0:
            placeholders.append(numbers.copy())
            newNumbers = []
            for i in range(1, len(numbers)):
                newNumbers.append(numbers[i] - numbers[i - 1])
            numbers = newNumbers.copy()
        placeholders[-1].append(placeholders[-1][-1])
        for i in range(len(placeholders) - 1, 0, -1):
            placeholders[i - 1].append(placeholders[i][-1] + placeholders[i - 1][-1])
        all_results.append(placeholders[0][-1])
    return sum(all_results)

def part2(content):
    result = 0
    all_results = []
    for line in content:
        numbers = [int(element) for element in line.replace("\n","").split(" ")]
        placeholders = []
        while sum([abs(number) for number in numbers]) != 0:
            placeholders.append(numbers.copy())
            newNumbers = []
            for i in range(1, len(numbers)):
                newNumbers.append(numbers[i] - numbers[i - 1])
            numbers = newNumbers.copy()
        placeholders[-1].append(placeholders[-1][-1])
        for i in range(len(placeholders) - 1, 0, -1):
            placeholders[i - 1] = [(placeholders[i - 1][0] - placeholders[i][0])] + placeholders[i - 1].copy()
        all_results.append(placeholders[0][0])
    return sum(all_results)