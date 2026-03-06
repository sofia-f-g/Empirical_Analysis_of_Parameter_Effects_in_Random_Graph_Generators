import numpy as np
from collections import deque


### Basic Graph Helpers ###

def build_adjacency(V, E, directed=False):
    """ Converts edge list into adjacency representaion to make
        metric computation efficient """
    
    vertex_ids = V.get('id')
    if vertex_ids is None:
        raise ValueError("V must contain an id entry with vertex identifiers")

    id_array = np.asarray(vertex_ids)
    n_vertices = len(id_array)

    # Map each original vertex id to a 0..n-1 slot in the adjacency structure
    # adjacency[idx] corresponds to vertex id V["id"][idx]
    index_of = {int(v_id): idx for idx, v_id in enumerate(id_array)}

    adjacency = [[] for _ in range(n_vertices)]

    if E is None:
        return adjacency

    edges = np.asarray(E, dtype=int)
    if edges.ndim != 2 or edges.shape[1] != 2:
        raise ValueError("E must be of shape (m, 2) containing (src, dst) pairs")

    for v_i, v_j in edges:
        if v_i not in index_of or v_j not in index_of:
            raise ValueError("Edge references unknown vertex id")

        # Double edges represent undirected 
        adjacency[index_of[v_i]].append(int(v_j))
        adjacency[index_of[v_j]].append(int(v_i))

    return adjacency


def compute_degree_sequences(V, E):
    """ Computes in- and out-degree arrays for all vertices from 
        the undirected edge list """
    
    adjacency = build_adjacency(V, E)
    degrees = np.array([len(neigh) for neigh in adjacency], dtype=int)
    dict = {'id': np.asarray(V['id']), 'degree': degrees}
    return dict
    


### Degree Distribution ###

def degree_histogram(deg):

    """ Produces degree frequency counts used for plots 
        and comparisions across parameter settings """
    
    # return (k, counts)

def estimate_powerlaw_exponent(deg, method='mle'):
    """ Estimates the tail exponent so we can compare how 
        parameters influence 'scale-freeness' """
    
    # return result


### Clustering ###

def clustering_coefficient(V, E):

    """ Computes global or average local clustering """

    adj = build_adjacency(V, E, directed=False)
    adj_sets = [set(neighbors) for neighbors in adj]

    n = len(adj)
    local_coeffs = []
    triangle_sum = 0
    triplet_sum = 0

    for v in range(n):
        deg = len(adj[v])
        if deg < 2:
            local_coeffs.append(0.0)
            continue

        possible = deg * (deg - 1) / 2
        edges_between = 0
        neighbors = adj[v]
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if neighbors[j] in adj_sets[neighbors[i]]:
                    edges_between += 1

        local_coeffs.append(edges_between / possible)
        triangle_sum += edges_between
        triplet_sum += possible

    avg_local = sum(local_coeffs) / n if n > 0 else 0.0
    global_cc = triangle_sum / triplet_sum if triplet_sum > 0 else 0.0

    return {'avg_local': float(avg_local), 'global': float(global_cc)}


### Paths / Distances ###

def average_shortest_path_length(V, E):
    """ Average shortest-path length over all connected 
        vertex pairs in an undirected graph """

    adjacency = build_adjacency(V, E)
    n = len(adjacency)
    
    total_dist = 0
    total_pairs = 0

    for v in range(n):
        # The shortest distance to all other vertices
        distances = bfs_distances(adjacency, v)

        # Add all 'connected' pairs and their distance
        for i in range (v+1, n):
            d = distances[i]
            if d >= 0:  # -1 if there is no path between vertices
                total_dist += d
                total_pairs += 1

    if total_pairs == 0:
        raise ValueError('No connected vertices - graph is totally disconnected')
    
    return total_dist / total_pairs

# Helper function
def bfs_distances(adjacency, start):
    n = len(adjacency)
    distances = [-1] * n
    distances[start] = 0

    # Create a double-ended queue with the first vertex as starting point
    q = deque([start])

    while q:
        v = q.popleft()

        # Go to direct neighbours
        for neighbour in adjacency[v]:
            # If unvisited 
            if distances[neighbour] == -1:
                distances[neighbour] = distances[v] + 1
                # Add neighbours to queue so we check next layer of vertices
                q.append(neighbour)
    
    return distances


### Wrapper ###

def compute_metrics(V, E):

    """ Return a dictionary of all required metrics, 
        degrees, clustering, path length, edges etc. """
    
    # return dict
