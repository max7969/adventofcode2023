import day15
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day15/ressources/test') as f:
        content = f.readlines()
        result = day15.part1(content)
        assert result == 52
        
def test_example2_part1():
    # Open file test and read lines
    with open('./day15/ressources/test2') as f:
        content = f.readlines()
        result = day15.part1(content)
        assert result == 1320
        
def test_part1():
    # Open file test and read lines
    with open('./day15/ressources/input') as f:
        content = f.readlines()
        result = day15.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day15/ressources/test2') as f:
        content = f.readlines()
        result = day15.part2(content)
        assert result == 145

def test_part2():
    # Open file test and read lines
    with open('./day15/ressources/input') as f:
        content = f.readlines()
        result = day15.part2(content)
        print(result)