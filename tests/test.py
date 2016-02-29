from src.seater import Seater
'''
Created on 24 Feb 2016

'''


def test_pattern():
    # test the pattern matching is parsing the line correctly
    seater = Seater()
    res = seater.get_cmd("occupy 957,736 through 977,890")
    assert res == ('occupy', 957, 736, 977, 890)


def test_occupy():
    # tests whether the occupy function gives the right number of 1's.
    seater = Seater()
    res = seater.get_cmd("occupy 520,520 through 522,522")
    assert seater.number_occupied() == 9


def test_empty():
    # tests whether the empty function removes occupied elements from the array. Not sure how to occupy them
    # locally, tried loop and .append method but doesn't work because seater is an instance of class Seater.
    seater = Seater()
    res = seater.get_cmd("empty 0, 0 through 20, 20")
    assert seater.number_occupied() == 0


def test_toggle():
    # tests whether the toggle function inverts the values of the seated list. Since all seats are by default empty,
    # toggle function should return 11*11 occupied seats. It doesn't, but it should!
    seater = Seater()
    res = seater.get_cmd("toggle 100, 100 through 110, 110")
    assert seater.number_occupied() == 121

