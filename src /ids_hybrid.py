"""
Lightweight Hybrid Intrusion Detection System for WSN
Contains Rule-based + Decision Tree (Best Model)
"""

import numpy as np
import joblib
import time
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class LightweightHybridIDS:
    def __init__(self):
        self.dt_model = None
        self.iso_model = None
        self.scaler = None
        
        # Rule-based thresholds (very lightweight)
        self.thresholds = {
            'drop_rate': 0.35,
            'energy_level': 0.35,
            'routing_changes': 8
        }
    
    def rule_based_detection(self, sample):
        """Fast rule-based check - first line of defense"""
        if (sample['drop_rate'] > self.thresholds['drop_rate'] or
            sample['energy_level'] < self.thresholds['energy_level'] or
            sample['routing_changes'] > self.thresholds['routing_changes']):
            return True  # Attack detected
        return False
    
    def train(self, X_train, y_train, X_test=None, y_test=None):
        """Train the best lightweight model - Decision Tree"""
        print("Training Decision Tree (Best lightweight model for WSN)...")
        
        self.dt_model = DecisionTreeClassifier(max_depth=6, random_state=42)
        self.dt_model.fit(X_train, y_train)
        
        # Optional: Train Isolation Forest for anomaly detection
        self.iso_model = IsolationForest(n_estimators=80, contamination=0.25, random_state=42)
        self.iso_model.fit(X_train)
        
        print("✅ Training completed!")
        
        if X_test is not None and y_test is not None:
            from sklearn.metrics import classification_report, accuracy_score
            y_pred = self.dt_model.predict(X_test)
            print("\nDecision Tree Performance:")
            print(classification_report(y_test, y_pred, target_names=['Normal', 'Attack']))
            print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    
    def predict(self, sample_dict):
        """Hybrid Prediction: Rule-based first → Decision Tree"""
        start_time = time.time()
        
        # Step 1: Fast Rule-based check
        if self.rule_based_detection(sample_dict):
            latency = time.time() - start_time
            return "ATTACK", latency, "Rule-Based"
        
        # Step 2: If rule says normal, use Decision Tree
        features = ['packet_rate', 'drop_rate', 'energy_level', 
                   'routing_changes', 'neighbor_count', 'traffic_anomaly']
        
        sample_array = np.array([[sample_dict[f] for f in features]])
        sample_scaled = self.scaler.transform(sample_array)
        
        prediction = self.dt_model.predict(sample_scaled)[0]
        latency = time.time() - start_time
        
        result = "ATTACK" if prediction == 1 else "NORMAL"
        return result, latency, "Decision Tree (Best Model)"
    
    def save_model(self, path='models/'):
        """Save the best model and scaler"""
        import os
        os.makedirs(path, exist_ok=True)
        joblib.dump(self.dt_model, f'{path}lids_decision_tree.pkl')
        joblib.dump(self.scaler, f'{path}scaler.pkl')
        print(f"✅ Best Model saved in {path}")
    
    def load_model(self, path='models/'):
        """Load the saved best model"""
        self.dt_model = joblib.load(f'{path}lids_decision_tree.pkl')
        self.scaler = joblib.load(f'{path}scaler.pkl')
        print("✅ Best Model loaded successfully!")
