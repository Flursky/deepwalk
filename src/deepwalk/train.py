# -*- coding: utf-8 -*-
import networkx as nx
import pandas as pd


def build_graph(edges_file: str, is_oriented = False) -> nx.Graph:
    _type = nx.Graph() if is_oriented == False else nx.DiGraph()
    G = nx.read_edgelist(edges_file, create_using=_type)
    
    return G