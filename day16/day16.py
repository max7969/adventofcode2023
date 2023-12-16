import re
import math
from itertools import combinations
from functools import lru_cache

def beam_to_string(beam):
    return ','.join([str(beam['x']), str(beam['y']), str(beam['dx']), str(beam['dy'])])

def compute_energized(start, obstacles, content):
    beams = [start]
    alreadyVisited = set()
    while len(beams) > 0:
        newBeams = []
        for beam in beams:
            alreadyVisited.add(beam_to_string(beam))
            beam['x'] += beam['dx']
            beam['y'] += beam['dy']
            if (beam['x'], beam['y']) in obstacles.keys():
                if obstacles[(beam['x'], beam['y'])] == '/':
                    oldX, oldY = beam['dx'], beam['dy']
                    beam['dx'] = -oldY
                    beam['dy'] = -oldX
                    newBeams.append(beam)
                elif obstacles[(beam['x'], beam['y'])] == '\\':
                    oldX, oldY = beam['dx'], beam['dy']
                    beam['dx'] = oldY
                    beam['dy'] = oldX
                    newBeams.append(beam)
                elif obstacles[(beam['x'], beam['y'])] == '|':
                    if beam['dx'] != 0:
                        newBeams.append({'x': beam['x'], 'y': beam['y'], 'dx': 0, 'dy': -1})
                        newBeams.append({'x': beam['x'], 'y': beam['y'], 'dx': 0, 'dy': 1})
                    else:
                        newBeams.append(beam)
                elif obstacles[(beam['x'], beam['y'])] == '-':
                    if beam['dy'] != 0:
                        newBeams.append({'x': beam['x'], 'y': beam['y'], 'dx': -1, 'dy': 0})
                        newBeams.append({'x': beam['x'], 'y': beam['y'], 'dx': 1, 'dy': 0})
                    else:
                        newBeams.append(beam)
            else:
                if beam['x'] >= 0 and beam['x'] < len(content[0]) and beam['y'] >= 0 and beam['y'] < len(content):
                    newBeams.append(beam)
        beams = []
        for newBeam in newBeams:
            if not beam_to_string(newBeam) in alreadyVisited:
                beams.append(newBeam)    
    
    simpleCoords = set()
    for visited in alreadyVisited:
        simpleCoords.add(visited.split(',')[0] + ',' + visited.split(',')[1])
    return len(simpleCoords) - 1

def part1(content):
    newContent = []
    for line in content:
        newContent.append(line.replace('\n', ''))
    content = newContent
    obstacles = {}
    for i, line in enumerate(content):
        for j, element in enumerate(line.replace('\n', '')):
            if element != '.':
                obstacles[(j, i)] = element 
    return compute_energized({'x': -1, 'y': 0, 'dx': 1, 'dy': 0}, obstacles, content)
    

def part2(content):
    newContent = []
    for line in content:
        newContent.append(line.replace('\n', ''))
    content = newContent
    obstacles = {}
    for i, line in enumerate(content):
        for j, element in enumerate(line.replace('\n', '')):
            if element != '.':
                obstacles[(j, i)] = element 
    energized = []
    for i in range(len(content[0])):
        energized.append(compute_energized({'x': i, 'y': -1, 'dx': 0, 'dy': 1}, obstacles, content))
        energized.append(compute_energized({'x': i, 'y': len(content), 'dx': 0, 'dy': -1}, obstacles, content))
    for i in range(len(content)):
        energized.append(compute_energized({'x': -1, 'y': i, 'dx': 1, 'dy': 0}, obstacles, content))
        energized.append(compute_energized({'x': len(content[0]), 'y': i, 'dx': -1, 'dy': 0}, obstacles, content))
    return max(energized)
