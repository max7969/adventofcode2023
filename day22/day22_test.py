import day22
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day22/ressources/test') as f:
        content = f.readlines()
        result = day22.part1(content)
        assert result == 5
        
def test_part1():
    # Open file test and read lines
    with open('./day22/ressources/input') as f:
        content = f.readlines()
        result = day22.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day22/ressources/test') as f:
        content = f.readlines()
        result = day22.part2(content)
        assert result == 7

def test_part2():
    # Open file test and read lines
    with open('./day22/ressources/input') as f:
        content = f.readlines()
        result = day22.part2(content)
        print(result)