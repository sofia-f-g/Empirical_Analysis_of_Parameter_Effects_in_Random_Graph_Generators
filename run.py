import io  # local io.py — save/load raw and summary CSVs
from datetime import datetime
import generator
import metrics



### Running Simulations ###

def run_one_simulation(params, n, seed):
    generator.validate_params(params)

    (V, E) = generator.generate_graph(params, n, seed)
    metric_row = metrics.compute_metrics(V, E)

    # Attach which parameters generated the results
    metric_row.update({
        "seed": seed,
        "beta": params["beta"],
        "gamma": params["gamma"],
        "dim": params["dim"],
    })
    
    return metric_row

def run_replicates(params, n, R, base_seed):

    """ Repeats run_one_simulation many times with controlled
        seeding to estimate variability """


### Sweeps + Aggregation ###

def make_param_grid(ranges_dict):

    """ Creates a list of parameter setting for sweeps """
    params = {
        'beta': 0.5,
        'gamma': 0.8,
        'd': 2,
        'space_cfg'
        'profile_cfg': {
            'kind': 'hard_cutoff',
            'limit': 0.7
        }
    }

    # return list[params]

def parameter_sweep(param_grid):

    """ Runs replicates for each parameter setting and collects
        results into a table suitable for plots """

    run_label = "sweep_" + datetime.now().strftime("%Y%m%d_%H%M%S")

    # result_table = []
    # for each params in param_grid:
    #     rows = run_replicates(params, ...)
    #     result_table.extend(rows)

    # io.save_raw_results(result_table, run_label)

    # return result_table, run_label


### Output and plotting
def summarise_over_replicates(result_table, run_label=None):

    """ Aggregates replicate rows into means/stds etc
        grouped by parameter setting """

    # summary_table = ...

    # if run_label is not None:
    #     io.save_summary(summary_table, run_label)

    # return summary_table

def plot_metric_vs_param(summary_table, x_param, y_metric):

    """ Produces your key empirical plots (metric vs parameter) """
