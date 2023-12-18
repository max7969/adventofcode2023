from shapely.geometry import Polygon, LineString
import matplotlib.pyplot as plt
import math
import numpy as np
        
def extract_edges(content, rgbMode = False):
    edges = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (0, 0)
    for line in content:
        split = line.split(' ')
        direction = (0,0)
        steps = 0
        if rgbMode:
            test = split[2].replace('#', '').replace('(', '').replace(')', '').upper()
            direction = directions[int(test[-1])]
            steps = int(test[0:5], 16)
        else:
            steps = int(split[1])
            direction = directions[int(split[0].replace('R', '0').replace('D', '1').replace('L', '2').replace('U', '3'))]
        end = (start[0] + steps * direction[0], start[1] + steps * direction[1])
        edges.append([start, end])
        start = end
    return edges

# Thanks copilot, I was lazy to found that
def enlarge_polygon(points, enlarge_amount):
    enlarged_points = []
    n = len(points)

    for i in range(n):
        p0 = np.array(points[i-1])  # previous point
        p1 = np.array(points[i])    # current point
        p2 = np.array(points[(i+1)%n])  # next point

        # Calculate the directions of the two edges that meet at the current point
        edge_dir1 = p1 - p0
        edge_dir2 = p2 - p1

        # Calculate the normals of these edges
        normal1 = np.array([-edge_dir1[1], edge_dir1[0]])
        normal1 /= np.linalg.norm(normal1)
        normal2 = np.array([-edge_dir2[1], edge_dir2[0]])
        normal2 /= np.linalg.norm(normal2)

        # Calculate the average normal at the current point
        average_normal = (normal1 + normal2) / 2

        # Move the current point along the average normal
        moved_p1 = p1 + enlarge_amount * average_normal
        enlarged_points.append(moved_p1.tolist())

    return enlarged_points


def part1(content):
    content = [line.replace('\n', '') for line in content]
    edges = extract_edges(content)
    points = []
    for edge in edges:
        if edge[0] not in points: 
            points.append(edge[0])
        if edge[1] not in points:
            points.append(edge[1])

    points = [(float(x), float(y)) for x, y in points]
    points = enlarge_polygon(points, 1)
    polygon = Polygon(points)       
    return polygon.area


def part2(content):
    content = [line.replace('\n', '') for line in content]
    edges = extract_edges(content, rgbMode = True)
    points = []
    for edge in edges:
        if edge[0] not in points: 
            points.append(edge[0])
        if edge[1] not in points:
            points.append(edge[1])

    points = [(float(x), float(y)) for x, y in points]
    points = enlarge_polygon(points, 1)
    polygon = Polygon(points)       
    return polygon.area
