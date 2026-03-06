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
        the directed edge list """
    
    # return (in_deg, out_deg)


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


### Paths / Distances ###

def average_shortest_path_length(V, E):

    """ Computes mean shortest path length """



### Wrapper ###

def compute_metrics(V, E):

    """ Return a dictionary of all required metrics, 
        degrees, clustering, path length, edges etc. """
    
    # return dict
