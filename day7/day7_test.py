import day7
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day7/ressources/test') as f:
        content = f.readlines()
        result = day7.part1(content)
        assert result == 6440

def test_part1():
    # Open file test and read lines
    with open('./day7/ressources/input') as f:
        content = f.readlines()
        result = day7.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day7/ressources/test') as f:
        content = f.readlines()
        result = day7.part2(content)
        assert result == 5905

def test_part2():
    # Open file test and read lines
    with open('./day7/ressources/input') as f:
        content = f.readlines()
        result = day7.part2(content)
        print(result)