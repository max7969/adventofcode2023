import day11
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day11/ressources/test') as f:
        content = f.readlines()
        result = day11.compute(content,2)
        assert result == 374
        
def test_part1():
    # Open file test and read lines
    with open('./day11/ressources/input') as f:
        content = f.readlines()
        result = day11.compute(content,2)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day11/ressources/test') as f:
        content = f.readlines()
        result = day11.compute(content,10)
        assert result == 1030

def test_example2_part2():
    # Open file test and read lines
    with open('./day11/ressources/test') as f:
        content = f.readlines()
        result = day11.compute(content,100)
        assert result == 8410

def test_part2():
    # Open file test and read lines
    with open('./day11/ressources/input') as f:
        content = f.readlines()
        result = day11.compute(content,1000000)
        print(result)