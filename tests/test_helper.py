import module_visualizer.helper as helper
import networkx as nx
import pytest


def test_clean_filename():
    assert helper.clean_filename("testfile.py") == "testfile"


def test_clean_filepath():
    assert helper.clean_filepath("../documents/testfile.py") == "testfile.py"
    assert helper.clean_filepath("main.py") == "main.py"


def test_clean_imports():
    the_imports = ['import sys', 'from typing import List', 'from numpy import linspace, diagonal',
 'from pandas import dataframe,series', 'import tensorflow, pytorch,keras', 'from loguru import logger',
 'from typing_extensions import Literal', 'from tiktok_bot.api import TikTokAPI', 
 'from tiktok_bot.models.category import Category, ListCategoriesRequest',
 'from tiktok_bot.models.feed import ListFeedRequest',
 'from tiktok_bot.models.feed_enums import FeedType, PullType',
 'from tiktok_bot.models.post import Post',
 'from tiktok_bot.models.search import ChallengeInfo',
 'from tiktok_bot.models.user import CommonUserDetails, UserProfile',
 'from pandas import *']
    assert helper.clean_imports(the_imports) == ['sys', 'typing.List', 'loguru.logger', 'typing_extensions.Literal',
 'tiktok_bot.api.TikTokAPI', 'tiktok_bot.models.feed.ListFeedRequest', 'tiktok_bot.models.post.Post',
 'tiktok_bot.models.search.ChallengeInfo', 'pandas', 'numpy.linspace', 'numpy.diagonal', 'pandas.dataframe',
 'pandas.series', 'tensorflow', 'pytorch', 'keras', 'tiktok_bot.models.category.Category', 
 'tiktok_bot.models.category.ListCategoriesRequest', 'tiktok_bot.models.feed_enums.FeedType', 
 'tiktok_bot.models.feed_enums.PullType', 'tiktok_bot.models.user.CommonUserDetails',
 'tiktok_bot.models.user.UserProfile']


def test_create_color_key_dic():
    pass


def test_create_color_val_dic():
    pass


def test_color_key_dic():
    test_dict = {'green': [1,2,3,4], 'blue': [9,7], 'purple': [5,6,8]}
    ans_dict = {1: 'green', 2: 'green', 3: 'green', 4: 'green',
        5: 'purple', 6: 'purple', 8: 'purple', 9: 'blue', 7: 'blue'}
    assert helper.color_key_dic(test_dict) == ans_dict


def test_color_val_dic():
    test_dict = {1: 'green', 2: 'green', 3: 'green', 4: 'green',
        5: 'purple', 6: 'purple', 7: 'blue', 8: 'blue', 9:'purple'}
    ans_dict = {'green': [1,2,3,4], 'purple': [5,6,9], 'blue': [7,8]}
    assert helper.color_val_dic(test_dict) == ans_dict
