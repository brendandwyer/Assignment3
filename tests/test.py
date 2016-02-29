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
    seater = Seater()
    res = seater.get_cmd("occupy 520,520 through 522,522")
    assert seater.number_occupied() == 9


def test_empty():
    seater = Seater()
    res = seater.get_cmd("empty 5, 5 through 20, 20")
    assert seater.number_occupied() == 5


def test_toggle():
    seater = Seater()
    res = seater.get_cmd("toggle 100, 100 through 110, 110")
    assert seater.number_occupied() ==

