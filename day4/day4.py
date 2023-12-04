import re
import math

def part1(content):
    sum = 0
    for line in content:
        line = line.replace("\n","")
        split = line.split(": ")
        secondSplit = split[1].split(" | ")
        winningNumbers = set(secondSplit[0].split(" "))
        myNumbers = set(secondSplit[1].split(" "))
        res = 0
        for myNumber in myNumbers:
            if myNumber != "":
                if myNumber in winningNumbers:
                    res += 1
        if res >= 1:
            sum += math.pow(2, res - 1)
    return sum

def part2(content):
    cards = {}
    copyOfCards = {}
    for line in content:
        line = line.replace("\n","")
        split = line.split(": ")
        card = int(split[0].split(" ")[-1])
        secondSplit = split[1].split(" | ")
        winningNumbers = set(secondSplit[0].split(" "))
        myNumbers = set(secondSplit[1].split(" "))
        res = 0
        for myNumber in myNumbers:
            if myNumber != "":
                if myNumber in winningNumbers:
                    res += 1
        if res >= 1:
            cards[card] = res
        copyOfCards[card] = 1
    for card in cards:
        for id in range(card + 1, card + 1 + cards[card]):
            copyOfCards[id] += copyOfCards[card]
    return sum(copyOfCards.values())