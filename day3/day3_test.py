import day3
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day3/ressources/test') as f:
        content = f.readlines()
        result = day3.part1(content)
        assert result == 4361

def test_part1():
    # Open file test and read lines
    with open('./day3/ressources/input') as f:
        content = f.readlines()
        result = day3.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day3/ressources/test') as f:
        content = f.readlines()
        result = day3.part2(content)
        assert result == 467835

def test_part2():
    # Open file test and read lines
    with open('./day3/ressources/input') as f:
        content = f.readlines()
        result = day3.part2(content)
        print(result)