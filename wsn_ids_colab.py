"""
Lightweight Hybrid Intrusion Detection System (LIDS) for Wireless Sensor Networks
Clean version for GitHub + Google Colab
Author: Ashu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
import time
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print("="*60)
print("Lightweight Hybrid IDS for Secure Wireless Sensor Networks")
print("="*60)

# ===============================
# 1. Realistic WSN Data Generation
# ===============================
def generate_wsn_data(n_samples=1500, attack_ratio=0.28, seed=42):
    """Generate synthetic WSN data with 4 types of attacks"""
    np.random.seed(seed)
    
    data = {
        'node_id': np.arange(1, n_samples + 1),
        'packet_rate': np.random.uniform(10, 120, n_samples),
        'drop_rate': np.zeros(n_samples),
        'energy_level': np.random.uniform(0.4, 1.0, n_samples),
        'routing_changes': np.random.poisson(2, n_samples),
        'neighbor_count': np.random.randint(3, 15, n_samples),
        'traffic_anomaly': np.random.uniform(0.5, 2.0, n_samples),
        'label': np.zeros(n_samples, dtype=int)  # 0: Normal, 1: Attack
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
            data['neighbor_count'][idx] = int(data['neighbor_count'][idx] * 2.5)
            data['routing_changes'][idx] += np.random.randint(5, 12)
        elif attack_type == 'spoofing':
            data['energy_level'][idx] = np.random.uniform(0.05, 0.35)
            data['routing_changes'][idx] += np.random.randint(6, 15)
    
    # Normal nodes
    normal_idx = np.setdiff1d(np.arange(n_samples), attack_idx)
    data['drop_rate'][normal_idx] = np.random.uniform(0.0, 0.12, len(normal_idx))
    
    df = pd.DataFrame(data)
    return df


# Generate dataset
df = generate_wsn_data(n_samples=1500)
print(f"✅ Dataset generated: {len(df)} samples")
print(f"   Normal: {len(df[df['label']==0])} | Attack: {len(df[df['label']==1])}")
print(df.head())

# ===============================
# 2. Feature Selection & Preprocessing
# ===============================
features = ['packet_rate', 'drop_rate', 'energy_level', 
            'routing_changes', 'neighbor_count', 'traffic_anomaly']

X = df[features]
y = df['label']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.25, random_state=42, stratify=y
)

print("\n✅ Data prepared and split successfully")

# ===============================
# 3. Train Lightweight Models
# ===============================
print("\nTraining models...")

# Best model for WSN: Decision Tree (lightweight + fast)
dt_model = DecisionTreeClassifier(max_depth=6, random_state=42)
dt_model.fit(X_train, y_train)

# Additional models for comparison
rf_model = RandomForestClassifier(n_estimators=50, max_depth=7, random_state=42)
rf_model.fit(X_train, y_train)

iso_model = IsolationForest(n_estimators=80, contamination=0.25, random_state=42)
iso_model.fit(X_train)

print("✅ Models trained: DecisionTree (Best), RandomForest, IsolationForest")

# ===============================
# 4. Rule-Based Detection (Very Lightweight)
# ===============================
def rule_based_detection(row):
    """Fast rule-based check - saves energy on sensor nodes"""
    if (row['drop_rate'] > 0.35 or 
        row['energy_level'] < 0.35 or 
        row['routing_changes'] > 8):
        return 1  # Attack
    return 0  # Normal

# ===============================
# 5. Hybrid Detection Function
# ===============================
def hybrid_detect(sample_dict, model=dt_model):
    """Hybrid: Rule-based first → ML only if needed"""
    start_time = time.time()
    
    # Rule-based (fastest)
    rule_result = rule_based_detection(sample_dict)
    if rule_result == 1:
        latency = time.time() - start_time
        return "ATTACK", latency, "Rule-Based"
    
    # ML fallback
    sample_array = np.array([[sample_dict[f] for f in features]])
    sample_scaled = scaler.transform(sample_array)
    
    prediction = model.predict(sample_scaled)[0]
    latency = time.time() - start_time
    
    result = "ATTACK" if prediction == 1 else "NORMAL"
    return result, latency, "Decision Tree"


print("✅ Hybrid IDS ready!\n")

# ===============================
# 6. Model Evaluation
# ===============================
y_pred = dt_model.predict(X_test)

print("📊 Performance of Best Model (Decision Tree):")
print(classification_report(y_test, y_pred, target_names=['Normal', 'Attack']))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# ===============================
# 7. Save Best Model & Scaler
# ===============================
os.makedirs('models', exist_ok=True)

joblib.dump(dt_model, 'models/lids_decision_tree.pkl')
joblib.dump(scaler, 'models/scaler.pkl')

print("\n✅ Best Model and Scaler saved in 'models/' folder")
print("   → models/lids_decision_tree.pkl")
print("   → models/scaler.pkl")

# ===============================
# 8. Test Hybrid Detection
# ===============================
print("\n🔍 Testing Hybrid Detection:")

# Normal sample
normal_sample = {
    'packet_rate': 42.5, 'drop_rate': 0.05, 'energy_level': 0.85,
    'routing_changes': 2, 'neighbor_count': 6, 'traffic_anomaly': 1.05
}
result, lat, method = hybrid_detect(normal_sample)
print(f"Normal Node  → {result} | Latency: {lat:.6f}s | Method: {method}")

# Attack sample
attack_sample = {
    'packet_rate': 98.7, 'drop_rate': 0.68, 'energy_level': 0.22,
    'routing_changes': 11, 'neighbor_count': 9, 'traffic_anomaly': 2.4
}
result, lat, method = hybrid_detect(attack_sample)
print(f"Attack Node  → {result} | Latency: {lat:.6f}s | Method: {method}")

# ===============================
# 9. Visualizations
# ===============================
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
sns.scatterplot(data=df, x='packet_rate', y='drop_rate', hue='label', palette=['green', 'red'])
plt.title('Packet Rate vs Drop Rate')

plt.subplot(2, 2, 2)
sns.histplot(data=df, x='energy_level', hue='label', bins=20)
plt.title('Energy Level Distribution')

plt.subplot(2, 2, 3)
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Normal', 'Attack'], yticklabels=['Normal', 'Attack'])
plt.title('Confusion Matrix - Decision Tree')
plt.xlabel('Predicted')
plt.ylabel('Actual')

plt.subplot(2, 2, 4)
sns.boxplot(data=df, x='label', y='routing_changes')
plt.title('Routing Changes: Normal vs Attack')
plt.xticks([0, 1], ['Normal', 'Attack'])

plt.tight_layout()
plt.savefig('results/ids_visualization.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n🎉 Script completed successfully!")
print("You can now use 'use_best_model.py' to load and test the saved model.")
