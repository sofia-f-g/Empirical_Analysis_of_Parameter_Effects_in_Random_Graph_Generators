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
    
    return np.random.default_rng(seed)


### Vertex sampling ###
def sample_vertices_fixed_n(n, d, space_cfg, age_cfg, rng):
    """ Samples n vertices with positions in our chosen spatial window/torus
        and birth times (0, 1) returning a vertex table/array """
    
    if n < 0:
        raise ValueError('n must be non-negative')
    if d <= 0:
        raise ValueError('d must be a positive integer')
    
    space_cfg = {} if space_cfg is None else dict(space_cfg)
    age_cfg = {} if age_cfg is None else dict(age_cfg)
    
    # --- Sample spatial positions --- # 
    # Default to the d-dimensional torus [-0.5, 0.5)^d unless explicit bounds are given

    bounds = space_cfg.get('bounds')
    if bounds is None:
        low = np.full(d, -0.5, dtype=float)
        high = np.full(d, 0.5, dtype=float)
    else:
        bounds = np.asarray(bounds, dtype=float)
        if bounds.shape != (d,2):
            raise ValueError('space_cfg[bounds] must have shape (d,2)')

        low = bounds[:, 0]
        high = bounds[:,1]

        if np.any(high <= low):
            raise ValueError('Each spatial interval must have high > low')
        
    # --- Uniformly distributes vertices within space_cfg --- #
    positions = rng.uniform(low=low, high=high, size=(n,d))

    # --- Sample ages / 'birth times' --- #
    age_distribution = 'uniform'  # Kan ändras till age_cfg.get('distribution', 'uniform')

    t_min = float(age_cfg.get('min', 0.0))
    t_max = float(age_cfg.get('max', 1.0))

    if not (t_max > t_min):
        raise ValueError('age_cfg must have max > min')
    
    birth_times = rng.uniform(t_min, t_max, size=n)

    # Sort to simplify edge-generation later
    order = np.argsort(birth_times)
    birth_times = birth_times[order]
    positions = positions[order]

    V = {
        'id': np.arange(n, dtype=int),
        'pos': positions,
        'birth_time': birth_times
    }
    
    return V

def sample_vertices_ppp(lambda_param, x, y, z, d, rng):

    """ Samples vertices from a Poisson point process in space x time,
        closer method to the original paper """

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

