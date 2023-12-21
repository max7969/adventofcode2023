from shapely.geometry import Polygon, LineString
import matplotlib.pyplot as plt
import math
import numpy as np
import re
import copy

def readValue(line):
    line = line[1:-1]
    split = line.split(',')
    return {'x': split[0].split('=')[1], 'm': split[1].split('=')[1], 'a': split[2].split('=')[1], 's': split[3].split('=')[1]}


def evaluateRule(rule, value, rules):
    splits = rule.split(',')
    for split in splits:
        if ':' in split:
            newSplit = split.split(':')
            transformedRule = newSplit[0].replace('x', value['x']).replace('m', value['m']).replace('a', value['a']).replace('s', value['s'])
            if eval(transformedRule):
                if newSplit[1] == 'A':
                    return 1
                elif newSplit[1] == 'R':
                    return 0
                return evaluateRule(rules[newSplit[1]], value, rules)
            else:
                continue
        else:
            if split == 'A':
                return 1
            elif split == 'R':
                return 0
            return evaluateRule(rules[split], value, rules)
    return 0

def part1(content):
    content = [line.replace('\n', '') for line in content]
    
    rules = {}
    values = []
    for line in content:
        if line == '':
            continue
        elif line.startswith('{'):
            values.append(readValue(line))
        else:
            rules[line.split('{')[0]] = line.split('{')[1][:-1]
    result = 0
    for value in values:
        if(evaluateRule(rules['in'], value, rules) == 1):
            result += int(value['x']) + int(value['m']) + int(value['a']) + int(value['s'])
    return result

def buildTree(rules, currentRule, node):
    splits = rules[node['key']].split(',')
    childs = []
    for split in splits:
        if ':' in split:
            newSplit = split.split(':')
            childs.append({'key': newSplit[1], 'rule': currentRule + " and " + newSplit[0], 'childs': []})
            currentRule += " and not " + newSplit[0]
        else:
            childs.append({'key': split, 'rule': currentRule, 'childs': []})
    
    for child in childs: 
        if child['key'] == 'A' or child['key'] == 'R':
            continue
        else:
            child = buildTree(rules, child['rule'], child)
    node['childs'] = childs
    return node

def computeSolutions(node, intervals):
    if node['key'] == 'A':
        return (intervals['x'][1] - intervals['x'][0] + 1) * (intervals['m'][1] - intervals['m'][0] + 1) * (intervals['a'][1] - intervals['a'][0] + 1) * (intervals['s'][1] - intervals['s'][0] + 1)
    elif node['key'] != 'R':
        result = 0        
        for child in node['childs']:
            currentIntervals = copy.deepcopy(intervals)
            for newRule in child['rule'].split(' and '):
                if newRule != '1==1':
                    newRule = child['rule'].split(' and ')[-1]
                    key = newRule.split('<')[0][-1]
                    value = ''
                    if key != 'x' and key != 'm' and key != 'a' and key != 's':
                        key = newRule.split('>')[0][-1]
                        value = int(newRule.split('>')[1])
                    else:
                        value = int(newRule.split('<')[1])
                        
                    if 'not' in newRule:
                        if '<' in newRule:
                            currentIntervals[key][0] = value
                        else:
                            currentIntervals[key][1] = value
                    else:
                        if '<' in newRule:
                            currentIntervals[key][1] = value - 1
                        else:
                            currentIntervals[key][0] = value + 1
            result += computeSolutions(child, currentIntervals)
        return result
    return 0

def part2(content):
    content = [line.replace('\n', '') for line in content]
    rules = {}
    values = []
    for line in content:
        if line == '':
            continue
        elif line.startswith('{'):
            values.append(readValue(line))
        else:
            rules[line.split('{')[0]] = line.split('{')[1][:-1]
    node = buildTree(rules, "1 == 1", {'key': "in", 'rule': '', 'childs': []})
    result = computeSolutions(node, {'x': [1,4000], 'm': [1,4000], 'a': [1,4000], 's': [1,4000]})
    return result