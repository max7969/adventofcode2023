import day9
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day9/ressources/test') as f:
        content = f.readlines()
        result = day9.part1(content)
        assert result == 114

def test_example2_part1():
    # Open file test and read lines
    with open('./day9/ressources/test2') as f:
        content = f.readlines()
        result = day9.part1(content)
        assert result == 114


def test_part1():
    # Open file test and read lines
    with open('./day9/ressources/input') as f:
        content = f.readlines()
        result = day9.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day9/ressources/test') as f:
        content = f.readlines()
        result = day9.part2(content)
        assert result == 2

def test_part2():
    # Open file test and read lines
    with open('./day9/ressources/input') as f:
        content = f.readlines()
        result = day9.part2(content)
        print(result)