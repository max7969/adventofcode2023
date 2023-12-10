import re
import math


def extract_map(content):
    map = {}
    start = ""
    empties = []
    for i, line in enumerate(content):
        for j, element in enumerate(list(line.replace("\n",""))):
            if element == "-":
                map[str(i) + "," + str(j)] = [str(i) + "," + str(j - 1), str(i) + "," + str(j + 1)]
            elif element == "|":
                map[str(i) + "," + str(j)] = [str(i - 1) + "," + str(j), str(i + 1) + "," + str(j)]
            elif element == "F":
                map[str(i) + "," + str(j)] = [str(i) + "," + str(j + 1), str(i + 1) + "," + str(j)]
            elif element == "7":
                map[str(i) + "," + str(j)] = [str(i) + "," + str(j - 1), str(i + 1) + "," + str(j)]
            elif element == "L":
                map[str(i) + "," + str(j)] = [str(i - 1) + "," + str(j), str(i) + "," + str(j + 1)]
            elif element == "J":
                map[str(i) + "," + str(j)] = [str(i - 1) + "," + str(j), str(i) + "," + str(j - 1)]
            elif element == "S":
                start = str(i) + "," + str(j)
                map[str(i) + "," + str(j)] = [str(i) + "," + str(j - 1), str(i) + "," + str(j + 1), str(i - 1) + "," + str(j), str(i + 1) + "," + str(j)]
            else:
                continue      
    return map, start

def transform_to_large_map(content):
    large_map = []
    originals = []
    transform_dict = {
        "-": ("...", "---", "..."),
        "|": (".|.", ".|.", ".|."),
        "F": ("...", ".F-", ".|."),
        "7": ("...", "-7.", ".|."),
        "J": (".|.", "-J.", "..."),
        "L": (".|.", ".L-", "..."),
        "S": (".|.", "-S-", ".|."),
    }
    for i, line in enumerate(content):
        line = line.replace("\n", "")
        line0, line1, line2 = "", "", ""
        for j, element in enumerate(line):
            transform = transform_dict.get(element, ("...", "...", "..."))
            line0 += transform[0]
            line1 += transform[1]
            line2 += transform[2]
            originals.append(f"{i * 3 + 1},{j * 3 + 1}")
        large_map.extend([line0, line1, line2])
    return large_map, set(originals)
    
def extract_map_search(content, path):
    search_map = {}
    path_set = set(path)
    for i in range(-1, len(content) + 1):
        for j in range(-1, len(list(content[0].replace("\n", ""))) + 1):
            search_map[str(i) + "," + str(j)] = []
            if not (str(i-1) + "," +str(j)) in path_set and i-1 >= -1:
                search_map[str(i) + "," + str(j)].append(str(i-1) + "," +str(j))
            if not (str(i+1) + "," +str(j)) in path_set and i+1 <= len(content):
                search_map[str(i) + "," + str(j)].append(str(i+1) + "," +str(j))
            if not (str(i) + "," +str(j-1)) in path_set and j-1 >= -1:
                search_map[str(i) + "," + str(j)].append(str(i) + "," +str(j-1))
            if not (str(i) + "," +str(j+1)) in path_set and j+1 <= len(list(content[0].replace("\n", ""))):
                search_map[str(i) + "," + str(j)].append(str(i) + "," +str(j+1))
    return search_map

def compute_path(map, start):
    steps = 0
    path = [start]
    while path[-1] != start or steps == 0:
        for possibility in map[path[-1]]:
            if possibility in map and path[-1] in map[possibility] and (steps == 0 or path[-2] != possibility):
                path.append(possibility)
                steps += 1
                break
    return path, steps

def manhattan_distance(start, end):
    start = start.split(",")
    end = end.split(",")
    return abs(int(start[0]) - int(end[0])) + abs(int(start[1]) - int(end[1]))

def look_for_path(start, end, search_map, havePath, haveNoPath):
    openSet = set([start])
    gScore = {}
    gScore[start] = 0
    fScore = {}
    fScore[start] = gScore[start] + manhattan_distance(start, end)
    
    while len(openSet) > 0:
        openSet = sorted(openSet, key=lambda element: fScore[element])
        current = openSet[0]
        if current == end or current in havePath:
            return 0, start
        elif current in haveNoPath:
            return 1, start
        openSet.remove(current)
        for neighbor in search_map[current]:
            tentative_gScore = gScore[current] + manhattan_distance(current, neighbor)
            if not neighbor in gScore or tentative_gScore < gScore[neighbor]:
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + manhattan_distance(neighbor, end)
                if not neighbor in openSet:
                    openSet.append(neighbor)
    return 1, start

def clean_map(map):
    for element in map:
        for possibility in map[element]:
            if not possibility in map:
                map[element].remove(possibility)
                
    toRemove = []
    for element in map:
        if len(map[element]) == 1:
            toRemove.append(element)
    for element in toRemove:
        del map[element]
    return map

def part1(content):
    map, start = extract_map(content)
    path, steps = compute_path(map, start)
    return steps / 2

def part2(content):
    large_map, toCheck = transform_to_large_map(content)
    map, start = extract_map(large_map)
    clean = clean_map(clean_map(map))
    path, steps = compute_path(clean, start)
    search_map = extract_map_search(large_map, path)
    sum = 0
    havePath = []
    haveNoPath = []
    
    for element in set(path):
        if element in toCheck:
            toCheck.remove(element)
    
    for pos in toCheck:
        result, element = look_for_path(pos, "-1,-1", search_map, havePath, haveNoPath)
        if result == 0:
            havePath.append(element)
        else:
            haveNoPath.append(element)
        sum += result
    return sum