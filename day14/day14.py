import re
import math
from itertools import combinations
from functools import lru_cache

def treat_line(line):
   split = line.split("#")
   newLine = []
   for element in split:
       rocks = element.count("O")
       newElement = ''.join(["O" for i in range(rocks)]) + ''.join(["." for i in range(len(element) - rocks)])
       newLine.append(newElement)
   return '#'.join(newLine)        

def rotate(content):
    transposed = list(zip(*content))
    rotated = [''.join(row) for row in transposed[::-1]]
    return rotated

def compute_weight(content):
    result = 0
    newContent = []
    for line in content:
        newContent.append(line[::-1])
        
    for i in range (len(newContent[0])):
        elements = [element[i] for element in newContent]
        result += (i + 1) * elements.count('O')
    return result
        

def part1(content):
    result = 0
    content = [line.replace('\n','') for line in content]
    content = [''.join(element) for element in list(zip(*content))]
    newContent = []
    for line in content:
        newContent.append(treat_line(line)[::-1])
        
    for i in range (len(newContent[0])):
        elements = [element[i] for element in newContent]
        result += (i + 1) * elements.count('O')
        
    return result

def part2(content):
    result = 0
    content = [line.replace('\n','') for line in content]
    content = [''.join(element) for element in list(zip(*content))]
    states = {}
    statesById = {} 
    for i in range (1000000000):
        for j in range(4):
            newContent = []
            for line in content:
                newContent.append(treat_line(line))
            content = newContent.copy()
            content = rotate(content)
        joined = ''.join(content)
        statesById[i] = content.copy()
        if joined in states:
            result = i - states[joined]
            break
        states[''.join(content)] = i
    return compute_weight(statesById[states[''.join(content)] + ((1000000000 - states[''.join(content)]) % result) - 1])
