# -*- coding: utf-8 -*-
import pytest

from deepwalk.train import build_graph
from deepwalk.model import Walker


def test_walker():
    g = build_graph(r"C:\Users\khairi\Workspace\deepwalk\data\g1-edges.txt", is_oriented=False)
    walker = Walker(g, 3, 2)

    walks = walker.simulate_walks()

    assert len(walks) == 3 * len(g.nodes())
    assert len(walks[0]) == 2