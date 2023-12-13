import day13
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day13/ressources/test') as f:
        content = f.readlines()
        result = day13.part1(content)
        assert result == 405
        
def test_example2_part1():
    # Open file test and read lines
    with open('./day13/ressources/test2') as f:
        content = f.readlines()
        result = day13.part1(content)
        assert result == 400
        
def test_part1():
    # Open file test and read lines
    with open('./day13/ressources/input') as f:
        content = f.readlines()
        result = day13.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day13/ressources/test') as f:
        content = f.readlines()
        result = day13.part2(content)
        assert result == 400

def test_example2_part2():
    # Open file test and read lines
    with open('./day13/ressources/test3') as f:
        content = f.readlines()
        result = day13.part2(content)
        assert result == 200

def test_part2():
    # Open file test and read lines
    with open('./day13/ressources/input') as f:
        content = f.readlines()
        result = day13.part2(content)
        print(result)