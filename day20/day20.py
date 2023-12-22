from shapely.geometry import Polygon, LineString
import matplotlib.pyplot as plt
import math
import numpy as np
import queue
   

def part1(content):
    content = [line.replace('\n', '') for line in content]
    modules = {}
    for line in content:
        split = line.split(" -> ")
        modules[split[0][1:]] = {'type': split[0][0], 'childs': split[1].split(', '), 'inputs': {}, 'outputs': {}, 'state': {}}
    
    for moduleKey in modules:
        module = modules[moduleKey]
        for child in module['childs']:
            if child in modules and modules[child]['type'] == '&':
                modules[child]['state'][moduleKey] = -1
        if module['type'] == '%':
            module['state'][moduleKey] = -1    
    
    count = {}
    count[-1] = 0
    count[1] = 0
    
    for i in range(1000):
        print("button => -1 => broadcaster")
        count[-1] += 1
        q = queue.Queue()
        q.put('roadcaster')
        while not q.empty():
            next = q.get()
            print(f'state before: {modules[next]["state"]}')
            module = modules[next]
            if module['type'] == 'b':
                module['inputs']['button'] = -1
                for child in module['childs']:
                    module['outputs'][child] = -1
                    modules[child]['inputs'][next] = -1
                    print(f"{next} => -1 => {child}")
                    count[-1] += 1
                    q.put(child)
            elif module['type'] == '%':
                if ('roadcaster' in module['inputs'] and module['inputs']['roadcaster']) or sum(module['inputs'].values()) <= -1:
                    module['state'][next] = -module['state'][next]
                    for child in module['childs']:
                        module['outputs'][child] = module['state'][next]
                        modules[child]['inputs'][next] = module['state'][next]
                        print(f"{next} => {module['state'][next]} => {child}")
                        count[module['state'][next]] += 1
                        q.put(child)
                    if 'roadcaster' in module['inputs']:
                        del module['inputs']['roadcaster']
            elif module['type'] == '&':
                for input in module['inputs']:
                    module['state'][input] = module['inputs'][input]
                nextSignal = 1
                if sum(module['state'].values()) == len(module['state']):
                    nextSignal = -1
                for child in module['childs']:
                    module['outputs'][child] = nextSignal
                    if child in modules:
                        modules[child]['inputs'][next] = nextSignal
                        q.put(child)
                    print(f"{next} => {nextSignal} => {child}")
                    count[nextSignal] += 1
            print(f'state after: {modules[next]["state"]}')
    return count[-1] * count[1]

    

def part2(content):
   return 0
