from shapely.geometry import Polygon, LineString
import matplotlib.pyplot as plt
import math
import numpy
import collections
from itertools import filterfalse
        
def part1(content, turns):
    content = [line.replace('\n', '') for line in content]
    start = (0, 0)
    map = {}
    for i, line in enumerate(content):
        for j, element in enumerate(line):
            if element == '.':
                map[(i, j)] = []
            elif element == 'S':
                map[(i, j)] = []
                start = (i, j)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for element in map:
        for direction in directions:
            if (element[0] + direction[0], element[1] + direction[1]) in map:
                map[element].append((element[0] + direction[0], element[1] + direction[1]))
                
    current = set()
    current.add(start)
    for i in range(turns):
        next = set()
        for element in current:
            for neighbour in map[element]:
                next.add(neighbour)
        current = next
    return len(current)

def computeNext(point, map, size, target):
    result = 0
    current = set()
    current.add(point)
    quadratic = []
    for i in range(1, target + 1):
        next = set()
        for element in current:
            for neighbour in map[element]:
                next.add(neighbour)
        current = next
        
        if i % size == target % size:
            quadratic.append(len(current))
            if len(quadratic) == 3:
                f = numpy.polyfit([0, 1, 2], quadratic, 2)
                print(f'polynomial: {f}')
                x = (target - (target % size)) // size
                return int(f[0]*x**2 + f[1]*x + f[2])
        
    return result

def part2(content):
    content = [line.replace('\n', '') for line in content]
    
    target = 26501365
    
    elements = collections.deque()
    map = {}
    for i, line in enumerate(content):
        for j, element in enumerate(line):
            map[(i, j)] = element
    elements.append((len(content) // 2, len(content) // 2))
    size = len(content)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    quadratic = []
    steps = 0
    while steps < target:
        steps += 1
        newElements = collections.deque()
        visited = set()
        while len(elements) > 0:
            element = elements.popleft()
            for direction in directions:
                neighbour = (element[0] + direction[0], element[1] + direction[1])
                neighbour_in_sample = ((element[0] + direction[0]) % size, (element[1] + direction[1]) % size)
                if map[neighbour_in_sample] != '#':
                    if neighbour not in visited:
                        visited.add(neighbour)
                        newElements.append(neighbour)
        elements = newElements
        
        if steps % size == target % size:
            quadratic.append(len(visited))
            print(quadratic)
            # On recherche les 3 premières solutions où steps % size = 65 (target % size), soit 65, puis 131 + 65, puis 2*131 + 65
            if len(quadratic) == 3:  
                b0 = quadratic[0]
                b1 = quadratic[1]-quadratic[0]
                b2 = quadratic[2]-quadratic[1]
                
                n = target // size
                
                # Sachant qu'on est sur un motif repetable, il répond à l'équation suivante où b0, b1, b2 peuvent être calculés grace aux 3 premières solutions ou n = 0, n = 1 & n = 2
                return b0 + b1*n + (n*(n-1)//2)*(b2-b1)
