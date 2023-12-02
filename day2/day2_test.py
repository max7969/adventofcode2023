import day2
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day2/ressources/test') as f:
        content = f.readlines()
        result = day2.part1(content)
        assert result == 8

def test_part1():
    # Open file test and read lines
    with open('./day2/ressources/input') as f:
        content = f.readlines()
        result = day2.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day2/ressources/test') as f:
        content = f.readlines()
        result = day2.part2(content)
        assert result == 2286

def test_part2():
    # Open file test and read lines
    with open('./day2/ressources/input') as f:
        content = f.readlines()
        result = day2.part2(content)
        print(result)