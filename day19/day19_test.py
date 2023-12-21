import day19
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day19/ressources/test') as f:
        content = f.readlines()
        result = day19.part1(content)
        assert result == 19114
        
def test_part1():
    # Open file test and read lines
    with open('./day19/ressources/input') as f:
        content = f.readlines()
        result = day19.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day19/ressources/test') as f:
        content = f.readlines()
        result = day19.part2(content)
        assert result == 167409079868000

def test_part2():
    # Open file test and read lines
    with open('./day19/ressources/input') as f:
        content = f.readlines()
        result = day19.part2(content)
        print(result)