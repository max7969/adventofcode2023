import re
import math
from itertools import combinations
from functools import lru_cache


def find_pattern(pattern, times, original = -1):
    patterns=[]
    reflexion = []
    for i in range (1, len(pattern)):
        first_part = ''.join(reversed(pattern[:i]))
        second_part = ''.join(pattern[i:])
        if len(first_part) >= len(second_part):
            if first_part.startswith(second_part):
                reflexion.append(i * times)
        else:
            if second_part.startswith(first_part):
                reflexion.append(i * times)    
    if original == -1 and len(reflexion) > 0:
        return max(reflexion)
    else:
        for element in reflexion:
            if element != original:
                return element
    return 0

def part1(content):
    patterns = []
    currentPattern = []
    for line in content:
        if line == '\n':
            patterns.append(currentPattern)
            currentPattern = []
        else:
            currentPattern.append(line.replace('\n',''))
    patterns.append(currentPattern)
    
    result = 0
    for pattern in patterns:
        result += compute_original(pattern)
    return result

def compute_original(pattern):
    result = 0
    currentPattern = pattern.copy()
    horizontal = find_pattern(pattern, 100)
    result += horizontal
    pattern = [''.join(element) for element in list(zip(*pattern))]
    vertical = find_pattern(pattern, 1)
    result += vertical
    return result

def part2(content):
    result = 0
    patterns = []
    currentPattern = []
    for line in content:
        if line == '\n':
            patterns.append(currentPattern)
            currentPattern = []
        else:
            currentPattern.append(line.replace('\n',''))
    patterns.append(currentPattern)
    for pattern in patterns:
        reflexion = 0
        initialReflexion = compute_original(pattern)
        for i,line in enumerate(pattern):
            for j,element in enumerate(list(line)):
                currentPattern = pattern.copy()
                newElement = '#'
                if pattern[i][j] == '#':
                    newElement = '.'
                currentPattern[i] = pattern[i][:j] + newElement + pattern[i][j+1:]
                horizontal = find_pattern(currentPattern, 100, initialReflexion)
                if horizontal > 0 and horizontal != initialReflexion:
                    reflexion = horizontal
                    break
                else:        
                    currentPattern = [''.join(element) for element in list(zip(*currentPattern))]
                    vertical = find_pattern(currentPattern, 1, initialReflexion)
                    if vertical > 0 and vertical != initialReflexion:
                        reflexion = vertical
                        break
            if reflexion > 0:
                break
        result += reflexion
    return result
