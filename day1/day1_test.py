import day1
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day1/ressources/test') as f:
        content = f.readlines()
        result = day1.calibrate(content)
        assert result == 142

def test_part1():
    # Open file test and read lines
    with open('./day1/ressources/input') as f:
        content = f.readlines()
        result = day1.calibrate(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day1/ressources/test2') as f:
        content = f.readlines()
        result = day1.calibrate(content, True)
        assert result == 281

def test_part2():
    # Open file test and read lines
    with open('./day1/ressources/input') as f:
        content = f.readlines()
        result = day1.calibrate(content, True)
        print(result)