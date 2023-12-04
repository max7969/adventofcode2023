import day4
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day4/ressources/test') as f:
        content = f.readlines()
        result = day4.part1(content)
        assert result == 13

def test_part1():
    # Open file test and read lines
    with open('./day4/ressources/input') as f:
        content = f.readlines()
        result = day4.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day4/ressources/test') as f:
        content = f.readlines()
        result = day4.part2(content)
        assert result == 30

def test_part2():
    # Open file test and read lines
    with open('./day4/ressources/input') as f:
        content = f.readlines()
        result = day4.part2(content)
        print(result)