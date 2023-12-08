import day8
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day8/ressources/test') as f:
        content = f.readlines()
        result = day8.part1(content)
        assert result == 2

def test_example2_part1():
    # Open file test and read lines
    with open('./day8/ressources/test2') as f:
        content = f.readlines()
        result = day8.part1(content)
        assert result == 6

def test_part1():
    # Open file test and read lines
    with open('./day8/ressources/input') as f:
        content = f.readlines()
        result = day8.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day8/ressources/test3') as f:
        content = f.readlines()
        result = day8.part2(content)
        assert result == 6

def test_part2():
    # Open file test and read lines
    with open('./day8/ressources/input') as f:
        content = f.readlines()
        result = day8.part2(content)
        print(result)