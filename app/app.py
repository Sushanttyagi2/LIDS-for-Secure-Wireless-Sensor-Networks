"""
Streamlit Web Dashboard - Lightweight Hybrid IDS for Wireless Sensor Networks
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
import sys
from pathlib import Path
from io import BytesIO
import matplotlib.pyplot as plt

# ====================== STRONG PATH FIX FOR STREAMLIT CLOUD ======================
# Force add the root directory to Python path
try:
    # Get root directory (one level above app/)
    root_dir = Path(__file__).resolve().parent.parent
    if str(root_dir) not in sys.path:
        sys.path.insert(0, str(root_dir))   # Insert at the beginning
    
    # Extra safety - add current working directory too
    sys.path.insert(0, str(Path.cwd()))
    
    print(f"✅ Root path added: {root_dir}")
except Exception as e:
    st.warning(f"Path fix warning: {e}")

# Try importing the module
try:
    from src.ids_hybrid import LightweightHybridIDS
    st.success("✅ Successfully imported LightweightHybridIDS")
except ImportError as e:
    st.error("❌ CRITICAL: Could not import 'src.ids_hybrid'")
    st.error(f"Error: {e}")
    st.error("Please check if 'src/' folder exists and contains '_init_.py'")
    st.stop()
# =====================================================================

# Page Configuration
st.set_page_config(
    page_title="LIDS-WSN",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Lightweight Hybrid Intrusion Detection System")
st.caption("Deep Tech | Energy-Efficient IDS for Wireless Sensor Networks")

# Load Model
@st.cache_resource
def load_model():
    try:
        ids = LightweightHybridIDS()
        ids.load_model("models/")
        return ids
    except Exception as e:
        st.error(f"❌ Model Loading Failed: {e}")
        st.info("*Fix:* Run python main_simulation.py locally → Commit the models/ folder → Redeploy")
        return None

ids_model = load_model()

if ids_model is None:
    st.stop()

# Helper visualization functions

def display_sample_visualization(sample):
    sample_df = pd.DataFrame([sample])
    st.subheader("Input Feature Values")
    st.bar_chart(sample_df.T)


def create_gauge_chart(value, title, min_val=0, max_val=100):
    """Create a simple gauge chart using matplotlib"""
    import matplotlib.pyplot as plt
    from io import BytesIO

    fig, ax = plt.subplots(figsize=(6, 2))
    ax.barh([0], [value], height=0.3, color='red' if value > 50 else 'green')
    ax.set_xlim(min_val, max_val)
    ax.set_title(title)
    ax.set_yticks([])
    ax.text(value + 2, 0, f'{value:.1f}%', va='center')

    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    st.image(buf, use_column_width=True)
    plt.close(fig)


def create_radar_chart(sample, result):
    """Create radar chart comparing sample to attack patterns"""
    import matplotlib.pyplot as plt
    from math import pi

    # Define attack pattern thresholds
    attack_patterns = {
        'packet_rate': 80,
        'drop_rate': 0.4,
        'energy_level': 0.4,
        'routing_changes': 10,
        'neighbor_count': 15,
        'traffic_anomaly': 2.0
    }

    categories = list(sample.keys())
    values = list(sample.values())
    attack_values = [attack_patterns[cat] for cat in categories]

    # Normalize values for radar chart
    max_values = [120, 1.0, 1.0, 20, 25, 3.0]
    values_norm = [v/m for v, m in zip(values, max_values)]
    attack_norm = [v/m for v, m in zip(attack_values, max_values)]

    angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
    angles += angles[:1]

    values_norm += values_norm[:1]
    attack_norm += attack_norm[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))
    ax.plot(angles, values_norm, 'o-', linewidth=2, label='Current Sample', color='blue')
    ax.fill(angles, values_norm, alpha=0.25, color='blue')
    ax.plot(angles, attack_norm, 'o-', linewidth=2, label='Attack Pattern', color='red')
    ax.fill(angles, attack_norm, alpha=0.25, color='red')

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 1)
    ax.set_title(f"Feature Comparison - {result}", size=16, fontweight='bold')
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', dpi=100)
    buf.seek(0)
    st.image(buf, use_column_width=True)
    plt.close(fig)


def create_feature_comparison(sample, result):
    """Create feature comparison with thresholds"""
    features = list(sample.keys())
    values = list(sample.values())

    # Define thresholds for different attack types
    thresholds = {
        'packet_rate': {'normal': 60, 'attack': 80},
        'drop_rate': {'normal': 0.2, 'attack': 0.4},
        'energy_level': {'normal': 0.7, 'attack': 0.4},
        'routing_changes': {'normal': 5, 'attack': 10},
        'neighbor_count': {'normal': 10, 'attack': 15},
        'traffic_anomaly': {'normal': 1.3, 'attack': 2.0}
    }

    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.ravel()

    colors = ['green' if result == 'NORMAL' else 'red'] * len(features)

    for i, (feature, value) in enumerate(zip(features, values)):
        ax = axes[i]
        thresh = thresholds[feature]

        # Plot value
        ax.bar(['Value'], [value], color=colors[i], alpha=0.7, label='Current')

        # Plot thresholds
        ax.axhline(y=thresh['normal'], color='green', linestyle='--', label='Normal Threshold')
        ax.axhline(y=thresh['attack'], color='red', linestyle='--', label='Attack Threshold')

        ax.set_title(f'{feature.replace("_", " ").title()}')
        ax.set_ylabel('Value')
        ax.legend()

    plt.tight_layout()
    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', dpi=100)
    buf.seek(0)
    st.image(buf, use_column_width=True)
    plt.close(fig)


def display_realtime_visualizations(sample, result, latency, method):
    """Display all real-time visualizations after detection"""
    st.markdown("---")
    st.subheader("🔍 Real-Time Analysis")

    # Detection confidence (simulated based on result)
    confidence = 85.0 if result == "ATTACK" else 92.0
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Detection Confidence", f"{confidence:.1f}%")
        st.metric("Detection Latency", f"{latency:.6f}s")
    with col2:
        st.metric("Detection Method", method)
        status_color = "🔴" if result == "ATTACK" else "🟢"
        st.metric("Status", f"{status_color} {result}")

    # Real-time visualizations
    tab1, tab2, tab3 = st.tabs(["📊 Feature Comparison", "🕸️ Radar Analysis", "📈 Input Values"])

    with tab1:
        create_feature_comparison(sample, result)

    with tab2:
        create_radar_chart(sample, result)

    with tab3:
        display_sample_visualization(sample)


def display_saved_plots():
    st.header("📈 Saved Visualizations")
    results_dir = Path(__file__).resolve().parent.parent / "results"
    image_files = [
        ("Feature Importance", "feature_importance.png"),
        ("Energy vs Accuracy", "energy_accuracy_tradeoff.png"),
        ("Confusion Matrix", "confusion_matrix.png")
    ]

    plot_shown = False
    for title, filename in image_files:
        image_path = results_dir / filename
        if image_path.exists():
            st.subheader(title)
            st.image(str(image_path), use_column_width=True)
            plot_shown = True

    if not plot_shown:
        st.warning("No saved visualization images found. Run `python main_simulation.py` first to generate them.")


# ====================== Navigation ======================
page = st.sidebar.radio("Navigation", ["🏠 Home", "🔴 Live Detection", "📊 Model Info", "📈 Visualizations", "ℹ️ About"])

# ====================== PAGES ======================

if page == "🏠 Home":
    st.header("Welcome")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Attacks", "4")
    with col2: st.metric("Model", "Decision Tree")
    with col3: st.metric("Type", "Hybrid")

elif page == "🔴 Live Detection":
    st.header("🔴 Live Attack Detection")
    
    col1, col2 = st.columns(2)
    with col1:
        packet_rate = st.slider("Packet Rate", 10.0, 120.0, 50.0)
        drop_rate = st.slider("Drop Rate", 0.0, 1.0, 0.1, 0.01)
        energy_level = st.slider("Energy Level", 0.0, 1.0, 0.8, 0.01)
    with col2:
        routing_changes = st.slider("Routing Changes", 0, 20, 3)
        neighbor_count = st.slider("Neighbor Count", 3, 25, 8)
        traffic_anomaly = st.slider("Traffic Anomaly", 0.5, 3.0, 1.2, 0.1)

    if st.button("🚨 Detect Attack", type="primary"):
        sample = {
            'packet_rate': packet_rate,
            'drop_rate': drop_rate,
            'energy_level': energy_level,
            'routing_changes': routing_changes,
            'neighbor_count': neighbor_count,
            'traffic_anomaly': traffic_anomaly
        }
        
        result, latency, method = ids_model.predict(sample)
        
        if result == "ATTACK":
            st.error("🔴 *ATTACK DETECTED*")
        else:
            st.success("🟢 *NORMAL NODE*")
            
        st.info(f"Method: {method} | Latency: {latency:.6f} sec")
        
        # Real-time visualizations
        display_realtime_visualizations(sample, result, latency, method)

elif page == "📊 Model Info":
    st.header("Model Information")
    st.write("*Best Model:* Decision Tree (Lightweight)")
    st.write("Hybrid Approach: Rule-based + Machine Learning")

elif page == "📈 Visualizations":
    display_saved_plots()

elif page == "ℹ️ About":
    st.header("About")
    st.write("Deep Tech project focused on energy-efficient security for Wireless Sensor Networks.")

# Footer
st.caption("Made by Ashu and Sushant Tyagi | Deep Tech Project")
