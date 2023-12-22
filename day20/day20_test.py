import day20
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day20/ressources/test') as f:
        content = f.readlines()
        result = day20.part1(content)
        assert result == 11687500

def test_example2_part1():
    # Open file test and read lines
    with open('./day20/ressources/test2') as f:
        content = f.readlines()
        result = day20.part1(content)
        assert result == 32000000
        
def test_part1():
    # Open file test and read lines
    with open('./day20/ressources/input') as f:
        content = f.readlines()
        result = day20.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day20/ressources/test') as f:
        content = f.readlines()
        result = day20.part2(content)
        assert result == 952408144115

def test_part2():
    # Open file test and read lines
    with open('./day20/ressources/input') as f:
        content = f.readlines()
        result = day20.part2(content)
        print(result)