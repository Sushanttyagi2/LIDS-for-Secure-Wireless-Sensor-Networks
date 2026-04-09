"""
Streamlit Web Dashboard - Lightweight Hybrid IDS for Wireless Sensor Networks
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
from pathlib import Path

# ======================
try:
    # Get the directory of the current file (app.py)
    current_file = Path(_file_).resolve()
    app_dir = current_file.parent          # app/ folder
    root_dir = app_dir.parent             # Project root folder
    
    # Add root directory to Python path
    if str(root_dir) not in sys.path:
        sys.path.append(str(root_dir))
    
    # Also try adding absolute path as backup
    sys.path.insert(0, str(root_dir))
    
    print(f"✅ Root directory added to path: {root_dir}")
    
except Exception as e:
    st.warning(f"Path setup warning: {e}")

# Now import from src
try:
    from src.ids_hybrid import LightweightHybridIDS
except ImportError as e:
    st.error(f"❌ Import Error: {e}")
    st.error("Could not import from 'src' folder. Make sure the folder structure is correct.")
    st.stop()
# =====================================================================

# Page Configuration
st.set_page_config(
    page_title="LIDS-WSN",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Lightweight Hybrid Intrusion Detection System for WSN")
st.caption("Deep Tech | Energy-Efficient Hybrid IDS for Wireless Sensor Networks")

# Load Model
@st.cache_resource
def load_model():
    try:
        ids = LightweightHybridIDS()
        ids.load_model('models/')
        st.success("✅ Model loaded successfully!")
        return ids
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        st.info("💡 *Solution*: Run python main_simulation.py locally first, then commit & redeploy.")
        return None

ids_model = load_model()

if ids_model is None:
    st.stop()

# ====================== Your Existing Pages ======================

# Sidebar
page = st.sidebar.radio("Navigation", ["Home", "Live Detection", "Model Info", "About"])

# ... (Keep all your previous page code here - Home, Live Detection, etc.)

# Example: Live Detection Page (shortened)
if page == "Live Detection":
    st.header("🔴 Live Attack Detection")
    
    col1, col2 = st.columns(2)
    with col1:
        packet_rate = st.slider("Packet Rate", 10.0, 120.0, 50.0)
        drop_rate = st.slider("Drop Rate", 0.0, 1.0, 0.1, 0.01)
        energy_level = st.slider("Energy Level", 0.0, 1.0, 0.8, 0.01)
    
    with col2:
        routing_changes = st.slider("Routing Changes", 0, 20, 2)
        neighbor_count = st.slider("Neighbor Count", 3, 25, 7)
        traffic_anomaly = st.slider("Traffic Anomaly", 0.5, 3.0, 1.2, 0.1)
    
    if st.button("🚨 Detect", type="primary"):
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
            st.error("🔴 ATTACK DETECTED!")
        else:
            st.success("🟢 NORMAL NODE DETECTED")
        
        st.info(f"*Method:* {method} | *Latency:* {latency:.6f} sec")
'''
# Import from src
from src.ids_hybrid import LightweightHybridIDS

# Page Configuration
st.set_page_config(
    page_title="LIDS-WSN",
    page_icon="🛡️",
    layout="wide"
)

# Title and Description
st.title("🛡️ Lightweight Hybrid Intrusion Detection System for WSN")
st.markdown("""
A **lightweight & energy-efficient** Intrusion Detection System for Wireless Sensor Networks  
using **Rule-based + Decision Tree** hybrid approach.
""")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Live Detection", "Model Info", "About"])

# Load the model once
@st.cache_resource
def load_model():
    try:
        ids = LightweightHybridIDS()
        ids.load_model('models/')
        return ids
    except Exception as e:
        st.error(f"❌ Could not load model: {e}")
        st.info("Please run `python main_simulation.py` first to train and save the model.")
        return None

ids_model = load_model()
'''

# ====================== HOME PAGE ======================
if page == "Home":
    st.header("Welcome to LIDS-WSN Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Attack Types", "4", "Sinkhole, Sybil, Spoofing, Selective")
    with col2:
        st.metric("Best Model", "Decision Tree", "Lightweight")
    with col3:
        st.metric("Detection Method", "Hybrid", "Rule + ML")
    
    st.image("https://via.placeholder.com/800x300/1E88E5/FFFFFF?text=Wireless+Sensor+Network+Security", 
             use_column_width=True)
    
    st.subheader("Key Features")
    st.markdown("""
    - Realistic WSN data simulation with multiple attacks
    - Fast Rule-based detection (energy efficient)
    - Decision Tree as fallback for higher accuracy
    - Energy consumption simulation & trade-off analysis
    - Real-time prediction dashboard
    """)

# ====================== LIVE DETECTION PAGE ======================
elif page == "Live Detection":
    st.header("🔴 Live Attack Detection")
    
    if ids_model is None:
        st.stop()
    
    st.subheader("Enter Sensor Node Parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        packet_rate = st.slider("Packet Rate", 10.0, 120.0, 50.0, 0.1)
        drop_rate = st.slider("Drop Rate", 0.0, 1.0, 0.1, 0.01)
        energy_level = st.slider("Energy Level", 0.05, 1.0, 0.8, 0.01)
    
    with col2:
        routing_changes = st.slider("Routing Changes", 0, 20, 2)
        neighbor_count = st.slider("Neighbor Count", 3, 25, 7)
        traffic_anomaly = st.slider("Traffic Anomaly Score", 0.5, 3.0, 1.2, 0.1)
    
    if st.button("🚨 Detect Attack", type="primary"):
        sample = {
            'packet_rate': packet_rate,
            'drop_rate': drop_rate,
            'energy_level': energy_level,
            'routing_changes': routing_changes,
            'neighbor_count': neighbor_count,
            'traffic_anomaly': traffic_anomaly
        }
        
        with st.spinner("Analyzing node..."):
            start_time = time.time()
            result, latency, method = ids_model.predict(sample)
            processing_time = time.time() - start_time
        
        if result == "ATTACK":
            st.error(f"🔴 **ATTACK DETECTED!**")
        else:
            st.success(f"🟢 **NORMAL NODE**")
        
        st.info(f"**Method Used:** {method} | **Latency:** {latency:.6f} seconds")
        
        # Show input values
        st.subheader("Input Parameters")
        st.json(sample)

# ====================== MODEL INFO PAGE ======================
elif page == "Model Info":
    st.header("📊 Model Information")
    
    if ids_model is None:
        st.stop()
    
    st.subheader("Best Model: Decision Tree")
    st.write("""
    - **Why Decision Tree?** Very lightweight, fast inference, interpretable, and suitable for constrained devices.
    - Hybrid approach: Rule-based detection is used first to save energy.
    """)
    
    try:
        df = pd.read_csv('Dataset/WSN_Synthetic_Dataset.csv')
        st.subheader("Dataset Overview")
        st.write(df.describe())
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Samples", len(df))
        with col2:
            st.metric("Attack Samples", df['label'].sum())
    except:
        st.warning("Dataset not found. Run main_simulation.py first.")

    st.subheader("Detection Methods")
    st.write("- **Rule-based**: Fast, low energy (used first)")
    st.write("- **Decision Tree**: Higher accuracy when needed")

# ====================== ABOUT PAGE ======================
elif page == "About":
    st.header("About This Project")
    st.write("""
    This project implements a **Lightweight Hybrid Intrusion Detection System** specifically designed 
    for Wireless Sensor Networks (WSNs) where computational power and battery life are limited.
    
    The system intelligently combines simple rule-based detection with a lightweight machine learning model 
    (Decision Tree) to achieve a good balance between **security** and **energy efficiency**.
    """)
    
    st.subheader("Project Goals")
    st.markdown("""
    - Detect common WSN attacks efficiently
    - Minimize energy consumption on sensor nodes
    - Provide interpretable and fast detection
    - Easy to deploy and test
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Made for Secure Wireless Sensor Networks Research")