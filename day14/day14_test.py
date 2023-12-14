import day14
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day14/ressources/test') as f:
        content = f.readlines()
        result = day14.part1(content)
        assert result == 136
        
def test_part1():
    # Open file test and read lines
    with open('./day14/ressources/input') as f:
        content = f.readlines()
        result = day14.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day14/ressources/test') as f:
        content = f.readlines()
        result = day14.part2(content)
        assert result == 64

def test_part2():
    # Open file test and read lines
    with open('./day14/ressources/input') as f:
        content = f.readlines()
        result = day14.part2(content)
        print(result)