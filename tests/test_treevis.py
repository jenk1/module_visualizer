from module_visualizer.module_visualizer import treevis
import networkx as nx
import pytest

def test_gather_nodes():
    assert treevis.gather_nodes('testerfile.py') == ['sys', 'typing.List', 'loguru.logger', 'typing_extensions.Literal',
 'tiktok_bot.api.TikTokAPI', 'tiktok_bot.models.feed.ListFeedRequest', 'tiktok_bot.models.post.Post',
 'tiktok_bot.models.search.ChallengeInfo', 'pandas', 'numpy.linspace', 'numpy.diagonal', 'pandas.dataframe',
 'pandas.series', 'tensorflow', 'pytorch', 'keras', 'tiktok_bot.models.category.Category', 
 'tiktok_bot.models.category.ListCategoriesRequest', 'tiktok_bot.models.feed_enums.FeedType', 
 'tiktok_bot.models.feed_enums.PullType', 'tiktok_bot.models.user.CommonUserDetails',
 'tiktok_bot.models.user.UserProfile']

def test_find_subgraph():
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

    # TODO: do some error checking in the future. For now aassume
    # correct input
    

    pass
