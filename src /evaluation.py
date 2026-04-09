# src/evaluation.py
"""
Evaluation and Visualization functions for Lightweight Hybrid IDS for WSN
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

def plot_confusion_matrix(y_true, y_pred, save_path='results/confusion_matrix.png'):
    """Plot and save confusion matrix"""
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Normal', 'Attack'],
                yticklabels=['Normal', 'Attack'])
    plt.title('Confusion Matrix - Lightweight Hybrid IDS')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Confusion Matrix saved at {save_path}")


def plot_feature_importance(model, feature_names, save_path='results/feature_importance.png'):
    """Plot feature importance for Decision Tree"""
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=importances, y=feature_names)
        plt.title('Feature Importance - Decision Tree')
        plt.xlabel('Importance Score')
        plt.ylabel('Features')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"✅ Feature Importance plot saved at {save_path}")
    else:
        print("Feature importance not available for this model.")


def plot_energy_vs_accuracy(energy_levels, accuracies, save_path='results/energy_accuracy_tradeoff.png'):
    """Plot Energy vs Accuracy Trade-off"""
    plt.figure(figsize=(8, 6))
    plt.plot(energy_levels, accuracies, marker='o', linewidth=2, markersize=8)
    plt.title('Security vs Energy Trade-off')
    plt.xlabel('Remaining Energy (%)')
    plt.ylabel('Detection Accuracy (%)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Energy-Accuracy Trade-off plot saved at {save_path}")


def print_model_performance(y_true, y_pred, model_name="Decision Tree"):
    """Print detailed performance metrics"""
    print(f"\n📊 {model_name} Performance Report:")
    print("-" * 50)
    print(classification_report(y_true, y_pred, target_names=['Normal', 'Attack']))
    
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    
    print(f"Accuracy  : {acc:.4f} ({acc*100:.2f}%)")
    print(f"Precision : {prec:.4f} ({prec*100:.2f}%)")
    print(f"Recall    : {rec:.4f} ({rec*100:.2f}%)")
    print(f"F1-Score  : {f1:.4f} ({f1*100:.2f}%)")
    print("-" * 50)


def evaluate_hybrid_model(ids_model, X_test, y_test):
    """Full evaluation of the hybrid model"""
    y_pred = ids_model.dt_model.predict(X_test)
    
    print_model_performance(y_test, y_pred, "Lightweight Hybrid IDS")
    
    # Generate plots
    plot_confusion_matrix(y_test, y_pred)
    plot_feature_importance(ids_model.dt_model, 
                           ['packet_rate', 'drop_rate', 'energy_level', 
                            'routing_changes', 'neighbor_count', 'traffic_anomaly'])
    
    return y_pred
