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


def test_gather_nodes():
    assert helper.gather_nodes('testerfile.py') == ['sys', 'typing.List', 'loguru.logger', 'typing_extensions.Literal',
 'tiktok_bot.api.TikTokAPI', 'tiktok_bot.models.feed.ListFeedRequest', 'tiktok_bot.models.post.Post',
 'tiktok_bot.models.search.ChallengeInfo', 'pandas', 'numpy.linspace', 'numpy.diagonal', 'pandas.dataframe',
 'pandas.series', 'tensorflow', 'pytorch', 'keras', 'tiktok_bot.models.category.Category', 
 'tiktok_bot.models.category.ListCategoriesRequest', 'tiktok_bot.models.feed_enums.FeedType', 
 'tiktok_bot.models.feed_enums.PullType', 'tiktok_bot.models.user.CommonUserDetails',
 'tiktok_bot.models.user.UserProfile']


def test_find_subgraph():
    # TODO: do some error checking in the future. For now aassume
    # correct input
    
    # A is the full graph
    A = nx.Graph()
    A.add_edge("top", "blue1")
    A.add_edge("top", "blue2")
    A.add_edge("blue1", "1")
    A.add_edge("blue1", "2")
    A.add_edge("blue1", "3")
    A.add_edge("blue2", "4")
    A.add_edge("1", "6")
    A.add_edge("3", "5")
    A.add_edge("5", "7")
    A.add_edge("5", "8")

    # B is a subgraph
    B = nx.Graph()
    B.add_edge("5", "7")
    B.add_edge("5", "8")

    # C is another subgraph
    C = nx.Graph()
    C.add_node('2')

    # D is another subgraph
    D = nx.Graph()
    D.add_edge("blue1", "1")
    D.add_edge("blue1", "2")
    D.add_edge("blue1", "3")
    D.add_edge("1", "6")
    D.add_edge("3", "5")
    D.add_edge("5", "7")
    D.add_edge("5", "8")
    
    assert list(helper.find_subgraph("top", A, False, True).edges()) == list(A.edges())
    assert list(helper.find_subgraph("5", A, False, True).edges()) == list(B.edges()) 
    assert list(helper.find_subgraph("2", A, False, True).edges()) == list(C.edges()) 
    assert list(helper.find_subgraph("blue1", A, False, True).edges()) == list(D.edges())
