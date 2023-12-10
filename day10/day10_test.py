import day10
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day10/ressources/test') as f:
        content = f.readlines()
        result = day10.part1(content)
        assert result == 4
        
def test_example2_part1():
    # Open file test and read lines
    with open('./day10/ressources/test2') as f:
        content = f.readlines()
        result = day10.part1(content)
        assert result == 8

def test_part1():
    # Open file test and read lines
    with open('./day10/ressources/input') as f:
        content = f.readlines()
        result = day10.part1(content)
        print(result)
        
def test_example_part2():
    # Open file test and read lines
    with open('./day10/ressources/test') as f:
        content = f.readlines()
        result = day10.part2(content)
        assert result == 1

def test_example2_part2():
    # Open file test and read lines
    with open('./day10/ressources/test3') as f:
        content = f.readlines()
        result = day10.part2(content)
        assert result == 4

def test_example3_part2():
    # Open file test and read lines
    with open('./day10/ressources/test4') as f:
        content = f.readlines()
        result = day10.part2(content)
        assert result == 8

def test_example4_part2():
    # Open file test and read lines
    with open('./day10/ressources/test5') as f:
        content = f.readlines()
        result = day10.part2(content)
        assert result == 10

def test_part2():
    # Open file test and read lines
    with open('./day10/ressources/input') as f:
        content = f.readlines()
        result = day10.part2(content)
        print(result)