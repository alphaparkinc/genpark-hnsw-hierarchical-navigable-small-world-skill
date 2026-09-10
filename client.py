import math

class HNSWGraph:
    """
    Hierarchical Navigable Small World (HNSW) Graph Engine
    for high-dimensional vector search.
    """
    def __init__(self, m=4, ef_construction=16):
        self.m = m
        self.ef = ef_construction
        self.nodes = {}
        self.edges = {}
        self.entry_point = None

    def _cosine_dist(self, u, v):
        dot = sum(a * b for a, b in zip(u, v))
        norm_u = math.sqrt(sum(a * a for a in u))
        norm_v = math.sqrt(sum(b * b for b in v))
        if norm_u == 0 or norm_v == 0:
            return 1.0
        return 1.0 - (dot / (norm_u * norm_v))

    def insert(self, node_id, vector):
        self.nodes[node_id] = vector
        self.edges[node_id] = []
        if self.entry_point is None:
            self.entry_point = node_id
            return

        curr = self.entry_point
        curr_dist = self._cosine_dist(vector, self.nodes[curr])
        while True:
            changed = False
            for nb in self.edges[curr]:
                d = self._cosine_dist(vector, self.nodes[nb])
                if d < curr_dist:
                    curr_dist = d
                    curr = nb
                    changed = True
            if not changed:
                break

        self.edges[node_id].append(curr)
        self.edges[curr].append(node_id)
        if len(self.edges[curr]) > self.m:
            self.edges[curr].pop(0)

    def search_knn(self, query_vec, k=1):
        if self.entry_point is None:
            return []
        curr = self.entry_point
        curr_dist = self._cosine_dist(query_vec, self.nodes[curr])
        while True:
            changed = False
            for nb in self.edges[curr]:
                d = self._cosine_dist(query_vec, self.nodes[nb])
                if d < curr_dist:
                    curr_dist = d
                    curr = nb
                    changed = True
            if not changed:
                break
        return [(curr, curr_dist)]
