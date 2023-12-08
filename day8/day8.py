import re
import math
from functools import reduce

def part1(content):
    steps = [int(element) for element in list(content[0].replace("\n","").replace("L","0").replace("R","1"))]
    map = {}
    for line in content[2:]:
        split = line.split(" = ")
        dest = split[1].replace("\n","").replace("(","").replace(")","").split(", ")
        map[split[0]] = [dest[0], dest[1]]
    
    count = 0
    current = "AAA"
    while (current != "ZZZ"):
        current = map[current][steps[count % len(steps)]]
        count += 1
    return count

def compute_pgcd(a, b):
    while b:
        a, b = b, a%b
    return a
    

def compute_ppcm(a, b):
    return a * b // compute_pgcd(a, b)

def part2(content):
    steps = [int(element) for element in list(content[0].replace("\n","").replace("L","0").replace("R","1"))]
    map = {}
    for line in content[2:]:
        split = line.split(" = ")
        dest = split[1].replace("\n","").replace("(","").replace(")","").split(", ")
        map[split[0]] = [dest[0], dest[1]]
    
    startingPoints = {}
    for element in map.keys():
        if element.endswith("A"):
            startingPoints[element] = 0
            count = 0
            current = element
            while  not current.endswith("Z"):
                current = map[current][steps[count % len(steps)]]
                count += 1
            startingPoints[element] = count    
    return reduce(compute_ppcm, startingPoints.values())