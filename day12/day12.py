import re
import math
from itertools import combinations
from functools import lru_cache

# Je laisse mes archives cracra de la première version
# Merci @tavash pour le cache de la solution recursive

# def generate_strings(size, num_hashes):
#     indices = list(range(size))
#     for combo in combinations(indices, num_hashes):
#         s = ['.' for _ in range(size)]
#         for i in combo:
#             s[i] = '#'
#         yield ''.join(s)

# def generate_regex(disposition):
#     verificationRegex = "^\.*"
#     for index,element in enumerate(disposition):
#         verificationRegex += "#{" + str(element) + "}"
#         if index != len(disposition) - 1:
#             verificationRegex += "\.+"
#     verificationRegex += "\.*$"
#     return verificationRegex

# def compute(line):
#     split = line.split(' ')
#     toCheck = split[0]
#     disposition = [int(element) for element in split[1].split(',')]
#     verificationRegex = ".*"
#     for index,element in enumerate(disposition):
#         verificationRegex += "#{" + str(element) + "}"
#         if index != len(disposition) - 1:
#             verificationRegex += ".+"
#     verificationRegex += ".*"

#     alreadyPositioned = toCheck.count('#')
#     possibilities = toCheck.count('?')
#     toPlace = sum(disposition) - alreadyPositioned
#     if toPlace < 0:
#         return 0
#     exemples = generate_strings(possibilities,toPlace)
#     count = 0
#     matches = []
#     verificationRegex_compiled = re.compile(verificationRegex)
    
#     for exemple in exemples:
#         copyToCheck = toCheck
#         for element in list(exemple):
#             copyToCheck = copyToCheck.replace('?',element,1)
#         if verificationRegex_compiled.match(copyToCheck):
#             count += 1
#     return count

@lru_cache
def compute_recursively(line, target):
    line = line.lstrip('.')
    
    # Si on a fini le traitement
    if len(line) == 0:
        if len(target) == 0:
            return 1
        return 0
    
    # Si on a plus de groupe à trouver mais qu'il reste des # ou pas
    if len(target) == 0:
        if '#' not in line:
            return 1
        return 0
    
    if line.startswith('#'):
        current_target = target[0]
        
        # Si la longueur restante est inferieure à la taille du groupe => pas possible
        if len(line) < current_target:
            return 0
        
        # Si le prochain groupe n'est pas de la bonne taille
        if '.' in line[:current_target]:
            return 0
        
        if len(line) == current_target:
            if len(target) == 1:
                return 1
            return 0
        
        # Si le separateur après le groupe n'est pas un "." ou un "?" => pas possible
        if line[current_target] == '#':
            return 0
        
        return compute_recursively(line[current_target+1:], target[1:])
    
    return compute_recursively(line.replace("?", "#", 1), target) + compute_recursively(line[1:], target)

def part1(content):
    count = 0
    for line in content:
        line = line.replace('\n', '')
        split = line.split(' ')
        
        initialDisposition = tuple([int(element) for element in split[1].split(',')])
        initial = compute_recursively(split[0], initialDisposition)
        count += initial
    return count

def part2(content):
    result = 0
    count = 0
    for line in content:
        line = line.replace('\n', '')
        split = line.split(' ')
    
        fullLine = '?'.join([split[0]] * 5) + " " + ','.join([split[1]] * 5)
        disposition = tuple([int(element) for element in (','.join([split[1]] * 5)).split(',')])
        firstPart = fullLine.split(' ')[0]
        full = compute_recursively(firstPart, disposition)
        
        result += full
    return result
