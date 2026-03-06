import numpy as np

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

    """ Computes mean shortest path length """



### Wrapper ###

def compute_metrics(V, E):

    """ Return a dictionary of all required metrics, 
        degrees, clustering, path length, edges etc. """
    
    # return dict
