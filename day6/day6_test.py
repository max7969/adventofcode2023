import day6
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day6/ressources/test') as f:
        content = f.readlines()
        result = day6.part1(content)
        assert result == 288

def test_part1():
    # Open file test and read lines
    with open('./day6/ressources/input') as f:
        content = f.readlines()
        result = day6.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day6/ressources/test') as f:
        content = f.readlines()
        result = day6.part2(content)
        assert result == 71503

def test_part2():
    # Open file test and read lines
    with open('./day6/ressources/input') as f:
        content = f.readlines()
        result = day6.part2(content)
        print(result)