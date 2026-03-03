
### Running Simulations ###

def run_one_simulation(params, n, seed):

    # (V, E) = generator.generate_graph
    # dict = metrics.compute_metrics

    return None

def run_replicates(params, n, R, base_seed):

    """ Repeats run_one_simulation many times with controlled
        seeding to estimate variability """
    

### Sweeps + Aggregation ###

def make_param_grid(ranges_dict):

    """ Creates a list of parameter setting for sweeps """

    # return list[params]

def parameter_sweep(param_grid):

    """ Runs replicates for each parameter setting and collects 
        results into a table suitable for plots """
    
    # return result_table


### Output and plotting
def summarise_over_replicates(result_table):

    """ Aggregates replicate rows into means/stds etc
        grouped by parameter setting """
    
    # return summary_table

def plot_metric_vs_param(summary_table, x_param, y_metric):

    """ Produces your key empirical plots (metric vs parameter) """

