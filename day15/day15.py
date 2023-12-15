import re
import math
from itertools import combinations
from functools import lru_cache

def compute(code):
    current_value = 0
    for element in code:
        current_value += ord(element)
        current_value = (current_value * 17) % 256
    return current_value

def decode(code):
    sign = '='
    splitCode = code.split(sign)
    value = -1
    if (len(splitCode) == 1):
        sign = '-'
        splitCode = code.split(sign)
    else:
        value = int(splitCode[1])     
    hash_value = compute(splitCode[0])
    return hash_value, value, sign, splitCode[0]

        

def part1(content):
    result = 0   
    codes = content[0].replace('\n', '').split(',')
    for code in codes:
        result += compute(code)
    return result

def part2(content):
    result = 0
    codes = content[0].replace('\n', '').split(',')
    
    boxes = {}
    
    for code in codes:
        hash_value, value, sign, key = decode(code)
        if not hash_value in boxes.keys():
            boxes[hash_value] = []
        indexInTheBox = -1
        for i, element in enumerate(boxes[hash_value]):
            if element['key'] == key:
                indexInTheBox = i
                break
        if sign == '-' and indexInTheBox >= 0:
            boxes[hash_value].pop(indexInTheBox)
        else:
            if sign == '=':
                if indexInTheBox >= 0:
                    boxes[hash_value][indexInTheBox] = {'key': key, 'value': value}
                else:
                    boxes[hash_value].append({'key': key, 'value': value})
                    
    for key in boxes.keys():
        if len(boxes[key]) > 0:
            for i, element in enumerate(boxes[key]):
                result += (key + 1) * (i + 1) * element['value']
    return result
