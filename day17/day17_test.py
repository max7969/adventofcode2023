import day17
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day17/ressources/test') as f:
        content = f.readlines()
        result = day17.part1(content)
        assert result == 102
        
def test_part1():
    # Open file test and read lines
    with open('./day17/ressources/input') as f:
        content = f.readlines()
        result = day17.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day17/ressources/test') as f:
        content = f.readlines()
        result = day17.part2(content)
        assert result == 94

def test_example2_part2():
    # Open file test and read lines
    with open('./day17/ressources/test2') as f:
        content = f.readlines()
        result = day17.part2(content)
        assert result == 71

def test_part2():
    # Open file test and read lines
    with open('./day17/ressources/input') as f:
        content = f.readlines()
        result = day17.part2(content)
        print(result)