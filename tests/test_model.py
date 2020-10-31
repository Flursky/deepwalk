# -*- coding: utf-8 -*-
import pytest

from gensim.models import Word2Vec
from deepwalk.train import build_graph
from deepwalk.model import Walker
from deepwalk.model import DeepWalk


__author__ = "Flursky"
__copyright__ = "Flursky"
__license__ = "mit"

def test_walker():
    g = build_graph(r"C:\Users\khairi\Workspace\deepwalk\data\g1-edges.txt", is_oriented=False)
    walker = Walker(g, 3, 2)

    walks = walker.simulate_walks()

    assert len(walks) == 3 * len(g.nodes())
    assert len(walks[0]) == 2

def test_deepwalk():
    g = build_graph(r"C:\Users\khairi\Workspace\deepwalk\data\g1-edges.txt", is_oriented=False)
    
    with pytest.raises(ValueError):
        deepwalk = DeepWalk(g, 2, 3)
        deepwalk.embeddings()
    
    deepwalk = DeepWalk(g, 2, 3)
    model = deepwalk.fit(window_size=1)
    embs = deepwalk.embeddings()

    assert len(embs.keys()) == len(g.nodes())
    assert len(embs['1']) == 128 # default embedding size
    assert isinstance(model, Word2Vec) is True