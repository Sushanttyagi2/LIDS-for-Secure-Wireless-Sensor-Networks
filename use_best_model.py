"""
How to use the Best Saved Model (Decision Tree)
Easy script to load and test the Lightweight IDS
"""

import numpy as np
import joblib
from src.ids_hybrid import LightweightHybridIDS

# Initialize and load the best model
ids = LightweightHybridIDS()

try:
    ids.load_model()
    print("✅ Best Model (Decision Tree) loaded successfully!\n")
except:
    print("❌ Model not found. Please train first using main_simulation.py")
    exit()

# Test Samples
print("🔍 Testing Best Model:\n")

# Normal Node Example
normal_sample = {
    'packet_rate': 45.3,
    'drop_rate': 0.06,
    'energy_level': 0.87,
    'routing_changes': 2,
    'neighbor_count': 7,
    'traffic_anomaly': 1.1
}

result, latency, method = ids.predict(normal_sample)
print(f"Normal Node   → Result: {result} | Latency: {latency:.6f}s | Method: {method}")

# Attack Node Example (Sinkhole-like)
attack_sample = {
    'packet_rate': 102.5,
    'drop_rate': 0.71,
    'energy_level': 0.19,
    'routing_changes': 13,
    'neighbor_count': 8,
    'traffic_anomaly': 2.45
}

result, latency, method = ids.predict(attack_sample)
print(f"Attack Node   → Result: {result} | Latency: {latency:.6f}s | Method: {method}")

print("\n✅ You can now use this model for real-time detection!")
