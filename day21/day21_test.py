import day21
import pytest


def test_example_part1():
    # Open file test and read lines
    with open('./day21/ressources/test') as f:
        content = f.readlines()
        result = day21.part1(content, 6)
        assert result == 16
        
def test_part1():
    # Open file test and read lines
    with open('./day21/ressources/input') as f:
        content = f.readlines()
        result = day21.part1(content,64)
        print(result)
        
def test_part2():
    # Open file test and read lines
    with open('./day21/ressources/input') as f:
        content = f.readlines()
        result = day21.part2(content)
        print(result)