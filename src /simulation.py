import numpy as np
import pandas as pd

def generate_data(num_nodes=100, attack=False):
    data = []

    for i in range(num_nodes):
        packet_rate = np.random.uniform(10, 100)
        drop_rate = np.random.uniform(0, 0.1)
        energy = np.random.uniform(0.5, 1.0)

        label = 0

        if attack:
            drop_rate = np.random.uniform(0.3, 0.7)
            energy = np.random.uniform(0.1, 0.4)
            label = 1

        data.append([packet_rate, drop_rate, energy, label])

    return pd.DataFrame(data, columns=["packet_rate", "drop_rate", "energy", "label"])
