import pytest

import networkx as nx
from deepwalk.train import build_graph, train
from deepwalk.model import DeepWalk

__author__ = "Flursky"
__copyright__ = "Flursky"
__license__ = "mit"

def test_build_graph():
    g = build_graph(r"C:\Users\khairi\Workspace\deepwalk\data\g1-edges.txt", is_oriented=True)
    assert type(g) == nx.DiGraph
    assert len(g.edges()) == 19
    assert len(g.nodes()) == 8

    g = build_graph(r"C:\Users\khairi\Workspace\deepwalk\data\g1-edges.txt", is_oriented=False)
    assert type(g) == nx.Graph
    assert len(g.edges()) == 16
    assert len(g.nodes()) == 8
    
def test_train_model():
    dw_model = train(r"C:\Users\khairi\Workspace\deepwalk\data\g1-edges.txt", is_oriented=False, num_walks=5, walk_length=3)

    assert isinstance(dw_model, DeepWalk)