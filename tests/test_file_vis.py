import module_visualizer.file_vis as fv
import networkx as nx
import pytest


def test_switch_to_color_key_dict():
    test_dict = {'one': 'green', 'two': 'green', 'three': 'red',
                 'four': 'yellow', 'five': 'yellow', 'six': 'red'}
    test_dict_2 = {1: 'green', 2: 'green', 3: 'green', 4: 'green',
                   5: 'purple', 6: 'purple', 7: 'blue', 8: 'blue',
                   9: 'purple'}
    ans_dict_1 = {'green': ['one', 'two'], 'yellow': ['four', 'five'],
                  'red': ['three', 'six']}
    ans_dict_2 = {'green': ['two', 'one'], 'yellow': ['five', 'four'],
                  'red': ['six', 'three']}
    ans_dict_3 = {'green': [1, 2, 3, 4], 'purple': [5, 6, 9], 'blue': [7, 8]}
    assert fv.switch_to_color_key_dict(test_dict) == ans_dict_1
    assert fv.switch_to_color_key_dict(test_dict) == ans_dict_2
    assert fv.switch_to_color_key_dict(test_dict_2) == ans_dict_3


def test_switch_to_color_val_dict():
    test_dict = {'green': ['one', 'two'], 'yellow': ['four', 'five'],
                 'red': ['three', 'six']}
    ans_dict = {'one': 'green', 'two': 'green', 'three': 'red',
                'four': 'yellow', 'five': 'yellow', 'six': 'red'}
    test_dict_2 = {'green': [1, 2, 3, 4], 'blue': [9, 7], 'purple': [5, 6, 8]}
    ans_dict_2 = {1: 'green', 2: 'green', 3: 'green', 4: 'green',
                  5: 'purple', 6: 'purple', 8: 'purple', 9: 'blue', 7: 'blue'}
    assert fv.switch_to_color_val_dict(test_dict) == ans_dict
    assert fv.switch_to_color_val_dict(test_dict_2) == ans_dict_2
