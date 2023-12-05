import re
import math

def convertSeeds(seeds, conversionTables):
    for conversion in conversionTables.keys():
        newSeeds = []
        for seed in seeds:
            newSeed = -1
            for conversionTable in conversionTables[conversion]:
                if seed >= conversionTable['fromStart'] and seed <= conversionTable['fromEnd']:
                    newSeed = seed + (conversionTable['toStart'] - conversionTable['fromStart'])
                    break
            if newSeed == -1:
                newSeed = seed
            newSeeds.append(newSeed)
        seeds = newSeeds
    return seeds

def extractConvertionTables(content):
    conversionTables = {}
    count = -1
    for line in content[1:]:
        line = line.replace('\n', '')
        if (line == ''):
            count += 1
            conversionTables[count] = []
        elif(re.match(r'^[a-z\-\:]+', line)):
            continue
        else:
            split = [int(element) for element in line.split(' ')]
            conversionTables[count].append({'fromStart': split[1], 'fromEnd': split[1] + split[2] - 1, 'toStart': split[0], 'toEnd': split[0] + split[2] - 1})
    return conversionTables

def part1(content):
    sum = 0
    seeds = [int(element) for element in content[0].split(' ')[1:]]
    conversionTables = extractConvertionTables(content)    
    seeds = convertSeeds(seeds, conversionTables)
    
    return min(seeds)

def part2(content):
    seeds = [int(element) for element in content[0].split(' ')[1:]]
    
    for i in range(len(seeds)):
        if (i%2 == 1):
            seeds[i] = seeds[i-1] + seeds[i] - 1
    originalSeeds = seeds.copy()
    conversionTables = extractConvertionTables(content)

    couples = []
    for i in range(len(seeds)):
        if (i%2 == 1):
            couples.append([originalSeeds[i-1], originalSeeds[i]])
    minimums = []
    for couple in couples:
        minCouple = couple.copy()
        while(minCouple[0] != minCouple[1]):
            seeds = [minCouple[0], minCouple[0] + int((minCouple[1] - minCouple[0]) / 2), minCouple[0] + int((minCouple[1] - minCouple[0]) / 2) + 1, minCouple[1]]
            originalSeeds = seeds.copy()
            seeds = convertSeeds(seeds, conversionTables)
            minCouple = []
            indexOfMin = seeds.index(min(seeds))
            if indexOfMin % 2 == 1:
                minCouple.append(originalSeeds[indexOfMin - 1])
                minCouple.append(originalSeeds[indexOfMin])
            else:
                minCouple.append(originalSeeds[indexOfMin])
                minCouple.append(originalSeeds[indexOfMin + 1])
        minimums.append(min(seeds))
        
    return min(minimums)