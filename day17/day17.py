import re
import math
from itertools import combinations
from functools import lru_cache

def manhattan_distance(start, end):
    start = start.split(",")
    end = end.split(",")
    return abs(int(start[0]) - int(end[0])) + abs(int(start[1]) - int(end[1]))

def look_for_path(start, end, search_map, max):
    startKey = start + ";" + "0,0"
    openSet = set([startKey])
    paths = {}
    paths[startKey] = start
    gScore = {}
    gScore[startKey] = 0
    fScore = {}
    fScore[startKey] = gScore[startKey] + manhattan_distance(start, end)
    
    while len(openSet) > 0:
        openSet = sorted(openSet, key=lambda element: fScore[element])
        current = openSet[0]
        openSet.remove(current)
        currentCoords = current.split(";")[0]
        currentDirection = current.split(";")[1]
        reverseCurrentDirection = str(-int(currentDirection.split(',')[0])) + "," + str(-int(currentDirection.split(',')[1]))
        
        if currentCoords == end:
            return gScore[current], paths[current]
        
        for neighbor in search_map[currentCoords]['neighbours']:
            if current.split(';')[1] != neighbor['direction']:
                neighborKey = neighbor['coords'] + ";" + neighbor['direction']
                tentative_gScore = gScore[current] + neighbor['cost']
                if neighbor['moves'] < max and neighbor['direction'] != reverseCurrentDirection and (not neighborKey in gScore or tentative_gScore < gScore[neighborKey]):
                    gScore[neighborKey] = tentative_gScore
                    fScore[neighborKey] = gScore[neighborKey] + manhattan_distance(neighbor['coords'], end)
                    if not neighborKey in openSet:
                        openSet.append(neighborKey)
                        paths[neighborKey] = paths[current] + ";" + neighbor['coords']
    return 0, "0,0;0,0"

def extract_search_map(content, min, max):
    searchMap = {}
    for i in range(len(content)):
        for j in range(len(content[0])):
            searchMap[str(i) + "," + str(j)] = {'neighbours': [], 'value': int(content[i][j]) }
            costs = {}
            costs[0], costs[1], costs[2], costs[3] = 0,0,0,0
            for k in range(1, min):
                if i-k >= 0:
                    costs[0] += int(content[i-k][j])
                if i < len(content) - k:
                    costs[1] += int(content[i+k][j])
                if j-k >= 0:
                    costs[2] += int(content[i][j-k])
                if j < len(content[0]) - k:
                    costs[3] += int(content[i][j+k])
            for k in range(min, max + 1):
                if i-k >= 0:
                    costs[0] += int(content[i-k][j])
                    searchMap[str(i) + "," + str(j)]['neighbours'].append({'coords': str(i-k) + "," + str(j), 'direction': "-1,0", 'moves': k, 'cost': costs[0] })
                if i < len(content) - k:
                    costs[1] += int(content[i+k][j])
                    searchMap[str(i) + "," + str(j)]['neighbours'].append({'coords': str(i+k) + "," + str(j), 'direction': "1,0", 'moves': k, 'cost': costs[1] })
                if j-k >= 0:
                    costs[2] += int(content[i][j-k])
                    searchMap[str(i) + "," + str(j)]['neighbours'].append({'coords': str(i) + "," + str(j-k), 'direction': "0,-1", 'moves': k, 'cost': costs[2] })
                if j < len(content[0]) - k:
                    costs[3] += int(content[i][j+k])
                    searchMap[str(i) + "," + str(j)]['neighbours'].append({'coords': str(i) + "," + str(j+k), 'direction': "0,1", 'moves': k, 'cost': costs[3] })
    return searchMap

def print_path(map, path):
    print("=====================================")
    path = path.split(";")
    for i in range(len(map)):
        line = ""
        for j in range(len(map[0])):
            if str(i) + "," + str(j) in path:
                line += 'X'
            else:
                line += '.'
        print(line)
    print("=====================================")

def part1(content):
    content = [line.replace('\n','') for line in content]
    searchMap = extract_search_map(content, 1, 3)
    result, path = look_for_path("0,0", str(len(content) - 1) + "," + str(len(content[0]) - 1), searchMap, 4)
    print_path(content, path)
    return result
    

def part2(content):
    content = [line.replace('\n','') for line in content]
    searchMap = extract_search_map(content, 4, 10)
    result, path = look_for_path("0,0", str(len(content) - 1) + "," + str(len(content[0]) - 1), searchMap, 11)
    print_path(content, path)
    return result
