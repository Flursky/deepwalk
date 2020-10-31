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
            nodes = list(self.G.nodes())
            random.shuffle(nodes)

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

    def __init__(self, g: nx.Graph, num_walks, walk_length):
        """
        """
        self.g = g
        self.walker = Walker(g, num_walks, walk_length)
        
        self.walks = None
        self.w2v = None
        self._embeddings = None

    def fit(self, embed_size=128, window_size=5, workers=1, iters=10, **kwargs):
        self.walks = self.walker.simulate_walks()

        ### Word2Vec params ###
        kwargs['sentences'] = self.walks
        kwargs['hs'] = 1
        kwargs['sg'] = 1
        kwargs['size'] = embed_size
        kwargs['window'] = window_size
        kwargs['workers'] = workers
        kwargs['iter'] = iters

        model = Word2Vec(**kwargs)

        self.w2v = model

        return model


    def embeddings(self):
        if self.w2v is None:
            raise ValueError('Model Not trained')

        if self._embeddings is None:
            embeddings = {}
            for node in list(self.g.nodes()):
                embeddings[node] = self.w2v.wv[str(node)]
            self._embeddings = embeddings
        return self._embeddings