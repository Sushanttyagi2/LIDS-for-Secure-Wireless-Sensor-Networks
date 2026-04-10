import numpy as np
import pandas as pd

def generate_wsn_data(n_samples=1500, attack_ratio=0.28, seed=42):
    """Generate realistic WSN data with multiple attack types"""
    np.random.seed(seed)
    
    data = {
        'node_id': np.arange(1, n_samples + 1),
        'packet_rate': np.random.uniform(10, 120, n_samples),
        'drop_rate': np.zeros(n_samples),
        'energy_level': np.random.uniform(0.4, 1.0, n_samples),
        'routing_changes': np.random.poisson(2, n_samples),
        'neighbor_count': np.random.randint(3, 15, n_samples),
        'traffic_anomaly': np.random.uniform(0.5, 2.0, n_samples),
        'label': np.zeros(n_samples, dtype=int)
    }
    
    n_attacks = int(n_samples * attack_ratio)
    attack_idx = np.random.choice(n_samples, n_attacks, replace=False)
    
    for idx in attack_idx:
        attack_type = np.random.choice(['sinkhole', 'selective_forwarding', 'sybil', 'spoofing'])
        data['label'][idx] = 1
        
        if attack_type == 'sinkhole':
            data['drop_rate'][idx] = np.random.uniform(0.45, 0.85)
            data['packet_rate'][idx] *= 1.8
        elif attack_type == 'selective_forwarding':
            data['drop_rate'][idx] = np.random.uniform(0.35, 0.75)
        elif attack_type == 'sybil':
            data['neighbor_count'][idx] *= 2.5
            data['routing_changes'][idx] += np.random.randint(5, 12)
        elif attack_type == 'spoofing':
            data['energy_level'][idx] = np.random.uniform(0.05, 0.35)
            data['routing_changes'][idx] += np.random.randint(6, 15)
    
    normal_idx = np.setdiff1d(np.arange(n_samples), attack_idx)
    data['drop_rate'][normal_idx] = np.random.uniform(0.0, 0.12, len(normal_idx))
    
    return pd.DataFrame(data)
