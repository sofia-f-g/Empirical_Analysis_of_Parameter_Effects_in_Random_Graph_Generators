
### Basic Graph Helpers ###

def build_adjacency(V, E, directed=True):

    """ Converts edge list into adjacency representaion to make
        metric computation efficient """
    
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