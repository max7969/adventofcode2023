import day12
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day12/ressources/test') as f:
        content = f.readlines()
        result = day12.part1(content)
        assert result == 21
        
def test_part1():
    # Open file test and read lines
    with open('./day12/ressources/input') as f:
        content = f.readlines()
        result = day12.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day12/ressources/test') as f:
        content = f.readlines()
        result = day12.part2(content)
        assert result == 525152

def test_example2_part2():
    # Open file test and read lines
    with open('./day12/ressources/test2') as f:
        content = f.readlines()
        result = day12.part2(content)
        assert result == 80049468

def test_part2():
    # Open file test and read lines
    with open('./day12/ressources/input') as f:
        content = f.readlines()
        result = day12.part2(content)
        print(result)