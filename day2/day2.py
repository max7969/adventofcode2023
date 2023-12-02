import re

def extract_game(line):
    split = line.replace("\n","").split(": ")
    gameId = int(re.search("Game ([0-9]*)", split[0]).group(1))
    turns = [[color.split(" ") for color in element.split(", ")] for element in split[1].split("; ")]
    return turns, gameId


def part1(content):
    sum = 0
    for line in content:
        turns, gameId = extract_game(line)
        for turn in turns:
            for color in turn:
                if (color[1] == "red" and int(color[0]) > 12) or (color[1] == "green" and int(color[0]) > 13) or (color[1] == "blue" and int(color[0]) > 14):
                    gameId = 0
                    break
        sum += gameId
    return sum

def part2(content):
    sum = 0
    for line in content:
        turns, gameId = extract_game(line)
        minRed, minGreen, minBlue = 0, 0, 0
        for turn in turns:
            for color in turn:
                if color[1] == "red" and int(color[0]) > minRed:
                    minRed = int(color[0])
                elif color[1] == "green" and int(color[0]) > minGreen:
                    minGreen = int(color[0])
                elif color[1] == "blue" and int(color[0]) > minBlue:
                    minBlue = int(color[0])
        sum += minRed * minGreen * minBlue
    return sum