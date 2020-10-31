# -*- coding: utf-8 -*-
import logging
import networkx as nx
from deepwalk.model import DeepWalk

_logger = logging.getLogger(__name__)

def build_graph(edges_file: str, is_oriented = False) -> nx.Graph:
    _logger.info('Building Graph')
    _type = nx.Graph() if is_oriented == False else nx.DiGraph()
    G = nx.read_edgelist(edges_file, create_using=_type)

    return G

def train_deepwalk(g, num_walks, walk_length, epochs=10, embed_size=128, window_size=5, workers=1):
    _logger.info('Start Training DeepWalk')
    deepwalk = DeepWalk(g, num_walks, walk_length)
    deepwalk.fit(embed_size, window_size, workers, epochs)
    _logger.info('Finished')

    return deepwalk


def train(edge_file: str, is_oriented: bool, num_walks: int, walk_length: int, epochs: int = 10, embed_size: int = 128, window_size: int = 5, workers: int = 1):
    G = build_graph(edge_file, is_oriented)
    
    dw_model = train_deepwalk(G, num_walks, walk_length, epochs, embed_size, window_size, workers)
    
    return dw_model

def save_model(model: DeepWalk, file):
    w2v_model = model.w2v
    w2v_model.wv.save_word2vec_format(file)