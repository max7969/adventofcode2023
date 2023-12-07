import re
import math

values = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
valuesJ = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
patterns = {'fiveOfAKind': 60000000000, 'fourOfAKind': 50000000000, 'fullHouse': 40000000000, 'threeOfAKind': 30000000000, 'twoPairs': 20000000000, 'pair': 10000000000, 'highCard': 0}


def compute_score(hand):
    result = determine_pattern(hand)
    
    multiples = [100000000, 1000000, 10000, 100, 1]
    sum = 0
    for (index, char) in enumerate(list(hand)):
        val = (values[char] * multiples[index]) 
        sum += val
    result = result + sum
    return result

def compute_score_with_jokers(hand):
    max = 0
    for value in valuesJ:
        result = determine_pattern(hand.replace("J", value))
        if result > max:
            max = result
    multiples = [100000000, 1000000, 10000, 100, 1]
    sum = 0
    for (index, char) in enumerate(list(hand)):
        val = (valuesJ[char] * multiples[index]) 
        sum += val
    return max + sum

def determine_pattern(hand):
    result = 0
    length = len(set(list(hand)))
    if(length == 1):
        result = patterns['fiveOfAKind']
    elif(length == 2) and (hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4):
        result = patterns['fourOfAKind']
    elif(length == 2):
        result = patterns['fullHouse']
    elif(length == 3) and (hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3):
        result = patterns['threeOfAKind']
    elif(length == 3):
        result = patterns['twoPairs']
    elif(length == 4):
        result = patterns['pair']
    else: 
        result = patterns['highCard']
    return result


def part1(content):
    hands = {}
    for line in content:
        line = line.replace("\n","")
        split = line.split(" ")
        hands[split[0]] = int(split[1])

    keys = hands.keys()
    sortedKeys = sorted(keys, key=compute_score)
    result = 0
    for index, key in enumerate(sortedKeys):
        result += hands[key] * (index + 1)
    return result

def part2(content):
    hands = {}
    for line in content:
        line = line.replace("\n","")
        split = line.split(" ")
        hands[split[0]] = int(split[1])

    keys = hands.keys()
    sortedKeys = sorted(keys, key=compute_score_with_jokers)
    result = 0
    for index, key in enumerate(sortedKeys):
        result += hands[key] * (index + 1)
    return result