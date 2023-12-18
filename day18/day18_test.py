import day18
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day18/ressources/test') as f:
        content = f.readlines()
        result = day18.part1(content)
        assert result == 62
        
def test_part1():
    # Open file test and read lines
    with open('./day18/ressources/input') as f:
        content = f.readlines()
        result = day18.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day18/ressources/test') as f:
        content = f.readlines()
        result = day18.part2(content)
        assert result == 952408144115

def test_part2():
    # Open file test and read lines
    with open('./day18/ressources/input') as f:
        content = f.readlines()
        result = day18.part2(content)
        print(result)