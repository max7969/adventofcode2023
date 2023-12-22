from shapely.geometry import Polygon, LineString, Point
import matplotlib.pyplot as plt
import math
import queue 
import copy

def createShape(coords):
    if coords[0] == coords[1]:
        return Point(coords[0])
    elif coords[0][0] == coords[1][0] or coords[0][1] == coords[1][1]:
        return LineString(coords)
    else:
        return Polygon([coords[0], (coords[0][0], coords[1][1]), coords[1], (coords[1][0], coords[0][1])])

def isOverlapping(cube1, cube2):
    square1 = [tuple([cube1[0][0],cube1[0][1]]),tuple([cube1[0][0] + (cube1[1][0] - cube1[0][0]),cube1[0][1] + (cube1[1][1] - cube1[0][1])])]
    square2 = [tuple([cube2[0][0],cube2[0][1]]),tuple([cube2[0][0] + (cube2[1][0] - cube2[0][0]),cube2[0][1] + (cube2[1][1] - cube2[0][1])])]
    shape1 = createShape(square1)
    shape2 = createShape(square2)
    return shape1.intersects(shape2)

def getSortedCubes(content):
    cubes = []
    for line in content:
        split = line.split('~')
        cubes.append(tuple([tuple([int(element) for element in split[0].split(',')]), tuple([int(element) for element in split[1].split(',')])]))
    
    return sorted(cubes, key=lambda x: x[0][2])

def createTower(cubes):
    q = queue.Queue()
    for cube in cubes:
        q.put(cube)
    tower = {}
    
    while not q.empty():
        cube = q.get()
        maxZ = 0
        overlapped = []
        # Pour tous les cubes déjà placés
        for otherCube in tower:
            # Si le nouveau sur x,y s'overlap avec un cube déjà placé
            # Si l'overlap est plus haut ou egal au maxZ
            if tower[otherCube]['maxZ'] > maxZ and isOverlapping(cube, otherCube):
                overlapped.clear()
                maxZ = tower[otherCube]['maxZ']
                overlapped.append(otherCube)
            elif tower[otherCube]['maxZ'] == maxZ and isOverlapping(cube, otherCube):
                overlapped.append(otherCube)
        tower[tuple(cube)] = {'maxZ': maxZ + (cube[1][2] - cube[0][2] + 1), 'overlapped': overlapped}
    return tower

def part1(content):
    content = [line.replace('\n', '') for line in content]
    cubes = getSortedCubes(content)
    tower = createTower(cubes)
    
    safelyRemoved = len(cubes)    
    for cube in cubes:
        for otherCube in tower:
            if cube in tower[otherCube]['overlapped'] and len(tower[otherCube]['overlapped']) == 1:
                safelyRemoved -= 1
                break
    return safelyRemoved

def part2(content):
    content = [line.replace('\n', '') for line in content]
    cubes = getSortedCubes(content)
    tower = createTower(cubes)
    result = 0
    for cube in cubes:
        copyTower = copy.deepcopy(tower)
        q = queue.Queue()
        q.put(cube)
        while not q.empty():
            current = q.get()
            del copyTower[current]
            for otherCube in copyTower:
                if current in copyTower[otherCube]['overlapped']:
                    copyTower[otherCube]['overlapped'].remove(current)
                    if len(copyTower[otherCube]['overlapped']) == 0:
                        q.put(otherCube)
        result += len(tower) - len(copyTower) - 1          
    return result