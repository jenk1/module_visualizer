import pytest
import util

# write out unit tests here

def test_clean_filename():
    assert util.clean_filename("testfile.py") == "testfile"

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
    assert util.clean_imports(the_imports) == ['sys', 'typing.List', 'loguru.logger', 'typing_extensions.Literal',
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
    pass

def test_color_val_dic():
    pass

def test_gather_nodes():
    assert util.gather_nodes('testerfile.py') == ['sys', 'typing.List', 'loguru.logger', 'typing_extensions.Literal',
 'tiktok_bot.api.TikTokAPI', 'tiktok_bot.models.feed.ListFeedRequest', 'tiktok_bot.models.post.Post',
 'tiktok_bot.models.search.ChallengeInfo', 'pandas', 'numpy.linspace', 'numpy.diagonal', 'pandas.dataframe',
 'pandas.series', 'tensorflow', 'pytorch', 'keras', 'tiktok_bot.models.category.Category', 
 'tiktok_bot.models.category.ListCategoriesRequest', 'tiktok_bot.models.feed_enums.FeedType', 
 'tiktok_bot.models.feed_enums.PullType', 'tiktok_bot.models.user.CommonUserDetails',
 'tiktok_bot.models.user.UserProfile']

def test_find_subgraph():
    pass
