### Graph Generation ###

def generate_graph(params, n, seed=None): 
    
    """ Main wrapper:
        samples vertices and then samples edges according to our model """
    
    # return (V,E) 
    return None


### Parameter + RNG utilities ###
def validate_params(params):
    
    """ Checks that parameters are in valid ranged ranges
        and raises clear error if not """
    
    return None #raises error if wrong 

def set_seed(seed):

    """ Creates and returns reproducible RNG object used by all sampling steps """
    
    # return np.random.Generator


### Vertex sampling ###
def sample_vertices_fixed_n(n, d, space_cfg, age_cfg, rng):

    """ Samples n vertices with positions in our chosen spatial window/torus
        and birth times (0, 1) returning a vertex table/array """
    
    # return V

def sample_vertices_ppp(lambda_param, x, y, z, d, rng):

    """ Samples vertices from a Poisson point process in space x time,
        closer adherence to the original paper """

    # return V


### Connection rule

def phi_profile_function(r, profile_cfg):

    """ Computes the profile value as a function of distance-like input """

    # return a float in the interval [0,1]

def connection_prob(v_i, v_j, params):

    """ Implements the model's connection probability for a directed edge i -> j,
        using ages, distance and parameters like beta, gamma and phi """
    


### Edge Generation ### 

def generate_edges(V, params, rng):

    """ Builds the edge list by iterating over candidate vertex pairs and
        sampling Bernoulli edges with function connection_prob """

