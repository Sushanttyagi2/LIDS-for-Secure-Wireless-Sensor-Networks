# ===============================
# Premium UI - Lightweight IDS
# ===============================

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# ===============================
# Page Config
# ===============================
st.set_page_config(page_title="WSN IDS", layout="wide")


# ===============================
# Title
# ===============================
st.title("🔐 Lightweight IDS for WSN")
st.markdown("### Real-time Intrusion Detection using ML + Rule-Based System")

# ===============================
# Sidebar
# ===============================
st.sidebar.header("⚙️ Settings")

num_nodes = st.sidebar.slider("Training Data Size", 100, 1000, 700)

st.sidebar.markdown("---")
st.sidebar.info("Hybrid IDS: Decision Tree + Rule-Based Detection")

# ===============================
# Data Simulation
# ===============================
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

# ===============================
# Train Model
# ===============================
@st.cache_resource
def train_model(n):
    normal = generate_data(n, False)
    attack = generate_data(int(n*0.4), True)
    df = pd.concat([normal, attack])

    X = df[["packet_rate", "drop_rate", "energy"]]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    return model, df

model, df = train_model(num_nodes)

# ===============================
# Layout (2 columns)
# ===============================
col1, col2 = st.columns(2)

# ===============================
# INPUT SECTION
# ===============================
with col1:
    st.subheader("📥 Enter Node Parameters")

    packet_rate = st.slider("Packet Rate", 0.0, 100.0, 50.0)
    drop_rate = st.slider("Drop Rate", 0.0, 1.0, 0.1)
    energy = st.slider("Energy Level", 0.0, 1.0, 0.8)

    detect_btn = st.button("🚨 Detect Attack")

# ===============================
# DETECTION LOGIC
# ===============================
def rule_based_detection(packet_rate, drop_rate, energy):
    if drop_rate > 0.3 or energy < 0.3:
        return 1
    return 0

# ===============================
# OUTPUT SECTION
# ===============================
with col2:
    st.subheader("📊 Detection Result")

    if detect_btn:
        sample = [packet_rate, drop_rate, energy]

        ml_pred = model.predict([sample])[0]
        rule_pred = rule_based_detection(*sample)

        if ml_pred == 1 or rule_pred == 1:
            st.error("⚠️ ATTACK DETECTED")
        else:
            st.success("✅ NORMAL NODE")

        # Metrics
        st.metric("Drop Rate", f"{drop_rate:.2f}")
        st.metric("Energy Level", f"{energy:.2f}")

# ===============================
# GRAPH SECTION
# ===============================
st.subheader("📈 Network Traffic Visualization")

fig, ax = plt.subplots()
ax.scatter(df["packet_rate"], df["drop_rate"], c=df["label"])
ax.set_xlabel("Packet Rate")
ax.set_ylabel("Drop Rate")

st.pyplot(fig)