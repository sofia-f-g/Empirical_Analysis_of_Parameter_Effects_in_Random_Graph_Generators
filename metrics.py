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
    index_of = {int(v_id): idx for idx, v_id in enumerate(np.asarray(V['id']))}

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
                if neighbors[j] in adj_sets[index_of[neighbors[i]]]:
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

    adj = build_adjacency(V, E)
    id_array = np.asarray(V['id'])
    index_of = {int(v_id): idx for idx, v_id in enumerate(id_array)}
    n = len(adj)
    total, count = 0, 0
    for src in range(n):
        dist = [-1] * n
        dist[src] = 0
        queue = [src]
        head = 0
        while head < len(queue):
            u = queue[head]; head += 1
            for w_id in adj[u]:
                w = index_of[w_id]
                if dist[w] == -1:
                    dist[w] = dist[u] + 1
                    queue.append(w)
        for d in dist:
            if d > 0:
                total += d; count += 1
    return total / count if count > 0 else 0.0


### Wrapper ###

def compute_metrics(V, E):

    """ Return a dictionary of all required metrics,
        degrees, clustering, path length, edges etc. """

    n_vertices = len(V['id'])
    n_edges = 0 if E is None or len(E) == 0 else len(E)

    deg_seq = compute_degree_sequences(V, E)
    degrees = deg_seq['degree']

    cc = clustering_coefficient(V, E)
    aspl = average_shortest_path_length(V, E)

    return {
        'n_vertices': n_vertices,
        'n_edges': n_edges,
        'degree_mean': float(np.mean(degrees)),
        'degree_max': int(np.max(degrees)),
        'degree_min': int(np.min(degrees)),
        'avg_local_clustering': cc['avg_local'],
        'global_clustering': cc['global'],
        'avg_shortest_path_length': aspl,
    }
