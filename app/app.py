"""
Streamlit Web Dashboard - Lightweight Hybrid IDS for Wireless Sensor Networks
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
import sys
from pathlib import Path

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
        display_sample_visualization(sample)

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
