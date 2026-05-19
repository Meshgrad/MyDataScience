import numpy as np

rng = np.random.default_rng(seed=1701)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output 

values = rng.integers(1, 10, size=5)
compute_reciprocals(values)