import re
import math

def get_extensions(content):
    content = [line.replace("\n","") for line in content]
    linesToExtend = []
    for i,line in enumerate(content):
        if len(set(list(line))) == 1:
            linesToExtend.append(i)
    
    columnsToExtend = []
    for i in range(len(content[0])):
        isEmpty = True
        for j in range(len(content)):
            if list(content[j])[i] != ".":
                isEmpty = False
        if isEmpty:
            columnsToExtend.append(i)
    return columnsToExtend, linesToExtend

def move_galaxies(galaxies, linesToExtend, columnsToExtend, step=2):
    for line in sorted(linesToExtend, reverse=True):
        for galaxy in galaxies:
            if int(galaxies[galaxy].split(",")[0]) >= line:
                galaxies[galaxy] = str(int(galaxies[galaxy].split(",")[0]) + step - 1) + "," + galaxies[galaxy].split(",")[1]
    for column in sorted(columnsToExtend, reverse=True):
        for galaxy in galaxies:
            if int(galaxies[galaxy].split(",")[1]) >= column:
                galaxies[galaxy] = galaxies[galaxy].split(",")[0] + "," + str(int(galaxies[galaxy].split(",")[1]) + step - 1)
    return galaxies
    
def manhattan_distance(start, end):
    start = start.split(",")
    end = end.split(",")
    return abs(int(start[0]) - int(end[0])) + abs(int(start[1]) - int(end[1]))

def compute(content, step):
    columnsToExtend, linesToExtend = get_extensions(content)
    galaxies = {}
    count = 0
    for i, line in enumerate(content):
        for j, char in enumerate(line):
            if char == "#":
                galaxies[count] = str(i) + "," + str(j)
                count += 1
    galaxies = move_galaxies(galaxies, linesToExtend, columnsToExtend,step=step)
    
    galaxies = set(galaxies.values())
    distances = {}
    sum = 0
    for galaxy in galaxies.copy():
        distances[galaxy] = [0]
        for otherGalaxy in galaxies:
            if galaxy != otherGalaxy:
                distances[galaxy].append(manhattan_distance(galaxy, otherGalaxy))
                sum += manhattan_distance(galaxy, otherGalaxy)
        galaxies.remove(galaxy)
    return sum