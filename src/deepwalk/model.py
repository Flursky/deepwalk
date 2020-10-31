import random
import networkx as nx
from gensim.models import Word2Vec
from tqdm import tqdm


class Walker(object):
    """
    """
    def __init__(self, g: nx.Graph, num_walks: int, walk_length: int):
        """
        Args:
            g (nx.Graph): graph
            num_walk (int): number of walk per node
            walk_length: walk length
        """
        self.G = g
        self.num_walks = num_walks
        self.walk_length = walk_length

    def simulate_walks(self) -> list:
        pbar = tqdm(len(self.G.nodes()) * self.num_walks, desc='Generating Random Walks')
        walks = []

        for _ in range(self.num_walks):
            nodes = self.G.nodes()
            # random.shuffle(nodes)

            for node in nodes:
                walks.append(self._walk(node))
                pbar.update(1)

        return walks
            
    def _walk(self, start: int) -> list:
        t = self.walk_length
        walk = [start]

        while len(walk) < t:
            current = walk[-1]
            neighbors = list(self.G.neighbors(current))
            if len(neighbors) > 0:
                walk.append(random.choice(neighbors))
            else:
                break
        return walk



class DeepWalk(object):

    def __init__(self, g: nx.Graph, num_walks, walk_length, window_size=5):
        """
        """
        self.embeddings = {}
        self.walker = Walker(g, num_walks, walk_length)

    
    def fit(self, g):
        pass