import pytest

import networkx as nx
from deepwalk.train import build_graph

__author__ = "Flursky"
__copyright__ = "Flursky"
__license__ = "mit"

def test_build_graph():
    g = build_graph(r"C:\Users\khairi\Workspace\deepwalk\data\g1-edges.txt", is_oriented=True)
    assert type(g) == nx.DiGraph
    assert len(g.edges()) == 17
    assert len(g.nodes()) == 8

    g = build_graph(r"C:\Users\khairi\Workspace\deepwalk\data\g1-edges.txt", is_oriented=False)
    assert type(g) == nx.Graph
    assert len(g.edges()) == 14
    assert len(g.nodes()) == 8
    