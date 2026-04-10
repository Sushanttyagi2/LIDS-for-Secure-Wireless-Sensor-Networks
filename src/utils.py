# src/utils.py
"""
Utility functions for Lightweight IDS for WSN Project
"""

import os
import numpy as np
import pandas as pd
import joblib
from datetime import datetime

def create_project_folders():
    """Create all necessary folders for the project"""
    folders = ['models', 'results', 'Dataset']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("✅ All project folders created successfully!")


def save_model_summary(model, scaler, accuracy=None):
    """Save model information and summary"""
    summary = {
        'model_type': 'Decision Tree (Best Lightweight Model)',
        'max_depth': model.max_depth if hasattr(model, 'max_depth') else None,
        'n_features': model.n_features_in_ if hasattr(model, 'n_features_in_') else None,
        'saved_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'accuracy': accuracy
    }
    
    with open('results/model_summary.txt', 'w') as f:
        f.write("Lightweight Hybrid IDS Model Summary\n")
        f.write("="*50 + "\n")
        for key, value in summary.items():
            f.write(f"{key.replace('_', ' ').title()}: {value}\n")
    
    print("✅ Model summary saved in 'results/model_summary.txt'")


def simulate_energy_consumption(num_detections=500, rule_based_ratio=0.75):
    """
    Simulate energy consumption for hybrid detection
    Rule-based = low energy, ML = higher energy
    """
    energy = 100.0
    energy_history = []
    
    for i in range(num_detections):
        # 75% cases use only rule-based (very low energy)
        if np.random.random() < rule_based_ratio:
            energy -= np.random.uniform(0.008, 0.015)   # Rule-based cost
        else:
            energy -= np.random.uniform(0.025, 0.045)   # ML cost
        
        energy = max(5.0, energy)  # Minimum 5% battery
        energy_history.append(energy)
    
    return energy_history


def print_detection_summary(results):
    """Print summary of detection results"""
    attacks_detected = sum(1 for r in results if r == "ATTACK")
    total = len(results)
    
    print(f"\n📋 Detection Summary:")
    print(f"Total detections : {total}")
    print(f"Attacks detected : {attacks_detected}")
    print(f"Detection Rate   : {(attacks_detected/total)*100:.2f}%")
