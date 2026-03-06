import run

if __name__ == "__main__":
    """ Runs all relevant scripts and defines variables """

    params = {
    "beta": 0.5,
    "gamma": 0.8,
    "dim": 2,
    "space_cfg": {"bounds": [[-0.5, 0.5], [-0.5, 0.5]]},
    "age_cfg": {"min": 0.0, "max": 1.0},
    "profile_cfg": {"a": 0.5},
}

    metric_row = run.run_one_simulation(params=params, n=100, seed=42)
    print(metric_row)