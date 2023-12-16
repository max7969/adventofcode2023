import day16
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day16/ressources/test') as f:
        content = f.readlines()
        result = day16.part1(content)
        assert result == 46
        
def test_part1():
    # Open file test and read lines
    with open('./day16/ressources/input') as f:
        content = f.readlines()
        result = day16.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day16/ressources/test') as f:
        content = f.readlines()
        result = day16.part2(content)
        assert result == 51

def test_part2():
    # Open file test and read lines
    with open('./day16/ressources/input') as f:
        content = f.readlines()
        result = day16.part2(content)
        print(result)