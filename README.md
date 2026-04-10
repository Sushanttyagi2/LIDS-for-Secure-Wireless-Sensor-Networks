# Lightweight Hybrid Intrusion Detection System for Wireless Sensor Networks (LIDS-WSN)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5+-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)

A **lightweight and energy-efficient** Hybrid Intrusion Detection System designed specifically for resource-constrained **Wireless Sensor Networks (WSNs)**.

It combines **Rule-based detection** (fast & low-energy) with **Decision Tree** (accurate & interpretable) to detect common WSN attacks while minimizing battery consumption.

## 🚀 Try the Interactive Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://your-app-name.streamlit.app](https://lids-for-secure-wireless-sensor-networks-p6jq.onrender.com/))

**Live Demo:** [Open Interactive Dashboard]([https://your-app-name.streamlit.app](https://lids-for-secure-wireless-sensor-networks-p6jq.onrender.com/))

Click the badge above or the link to test the **Live Attack Detection** directly in your browser!
---

## 🌟 Project Overview

This project addresses a critical challenge in IoT and WSN systems:

> **How to detect attacks efficiently while consuming minimum battery and computational resources?**

It uses a smart **Hybrid Approach**:
- **Rule-based detection** (very fast & low energy)
- **Decision Tree** (lightweight ML model) as intelligent fallback

---

## ✨ Key Features

- Realistic simulation of WSN traffic with **4 major attack types**:
  - Sinkhole Attack
  - Selective Forwarding
  - Sybil Attack
  - Spoofing Attack
- **Hybrid Detection Engine**: Rule-based (first) + Decision Tree (fallback)
- Energy-aware design with battery consumption simulation
- Feature importance analysis
- Interactive **Streamlit Web Dashboard**
- Modular, clean, and well-documented code
- Ready for GitHub, research, and academic projects

---

## 📂 Project Structure

```bash
LIDS-for-Secure-Wireless-Sensor-Networks/
├── Dataset/                          # Synthetic and real datasets
├── models/                           # Trained models (.pkl files)
├── results/                          # Plots, confusion matrix, reports
├── src/                              # Core modular Python code
│   ├── __init__.py
│   ├── data_generator.py
│   ├── ids_hybrid.py                 # Hybrid IDS class (Main Logic)
│   ├── evaluation.py                 # Metrics and visualizations
│   └── utils.py                      # Helper functions
├── app/
│   └── app.py                        # Streamlit Web Dashboard
├── main_simulation.py                # Full training & simulation
├── use_best_model.py                 # Quick model testing
├── wsn_ids_colab.py                  # Google Colab version
├── requirements.txt
├── README.md
└── .gitignore
```

## 🛠 Installation & Setup
# 1. Clone the repository
git clone https://github.com/Sushanttyagi2/LIDS-for-Secure-Wireless-Sensor-Networks.git
cd LIDS-for-Secure-Wireless-Sensor-Networks

# 2. Create virtual environment (Recommended)
```
# Clone the repository
git clone https://github.com/Sushanttyagi2/LIDS-for-Secure-Wireless-Sensor-Networks.git
cd LIDS-for-Secure-Wireless-Sensor-Networks

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac

# Install dependencies
pip install -r requirements.txt

```

## 🚀 How to Run
1. Full Simulation & Training (Must Run First)
   ```
   python main_simulation.py
   ```
This command:

. Generates synthetic WSN dataset
. Trains the hybrid IDS model
. Saves lids_decision_tree.pkl and scaler.pkl
. Creates evaluation plots in results/ folder

2. Test the Best Model
   ```
   python use_best_model.py
   ```

4. Launch Web Dashboard (Interactive)
   ```
   streamlit run app/app.py
   ```

6. Google Colab Version
   ```
   Open wsn_ids_colab.py in Google Colab and run all cells.
   ```

---

📊 Expected Results

Accuracy: 92–96% (on synthetic data)
Low latency using Rule-based first approach
Visualizations saved in results/ folder:
Confusion Matrix
Feature Importance
Energy vs Accuracy Trade-off

---

## 🔬 Supported Attack Types

| Attack Type               | Description                                      | Key Indicators Detected By                          | Detection Method Used          |
|---------------------------|--------------------------------------------------|-----------------------------------------------------|--------------------------------|
| **Sinkhole**              | Attacker attracts all traffic towards itself     | High packet rate + Very high drop rate              | Rule-based + Decision Tree     |
| **Selective Forwarding**  | Drops selected packets instead of forwarding     | Moderate to high packet drop rate                   | Rule-based (Primary)           |
| **Sybil**                 | Creates multiple fake identities                 | Sudden increase in neighbor count + Routing changes | Decision Tree                  |
| **Spoofing**              | Forges identity of legitimate nodes              | Very low energy level + High routing changes        | Rule-based (Primary)           |

---

📊 Results Highlights

. High detection accuracy with low computational cost
. Rule-based detection used in most cases to save energy
. Clear visualization of energy-security trade-off
. Interactive dashboard for real-time testing

---
🖥️ Web Dashboard Features

Real-time attack detection by adjusting sensor parameters
Live prediction with latency display
Model information and dataset overview
Clean and user-friendly interface

---

🛠 Technologies Used

Python 3.8+
scikit-learn (Decision Tree + Isolation Forest)
pandas, numpy
matplotlib & seaborn
Streamlit (Web UI)
joblib (Model persistence)

---

📌 Use Cases

. Smart Agriculture
. Healthcare IoT Monitoring
. Industrial IoT (IIoT)
. Environmental Sensor Networks
. Border Surveillance Systems

---

📌 Future Enhancements (Planned)

Integration with NS-3 / Cooja simulator
ONNX / TensorFlow Lite export for edge devices
Real packet capture support
Docker support
Advanced ML models with hyperparameter tuning


👨‍💻 Author
Ashu
Sushant Tyagi
If you like this project, feel free to ⭐ star the repository!

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

---

# problem statement

Lightweight Intrusion Detection System for Secure Wireless Sensor Networks.

#1 Overview
Wireless Sensor Networks (WSNs) are widely used in environmental monitoring, healthcare, military surveillance, and smart cities. However, due to limited computational power, battery constraints, and open wireless communication, WSNs are highly vulnerable to security threats.

#2 Wireless Sensor Networks (WSN)
A typical WSN consists of:
Sensor nodes
Cluster heads
Sink/base station
Wireless communication links

 #3 Problem Statement
WSNs are vulnerable to multiple attacks such as:
Sinkhole attacks
Selective forwarding attacks
Sybil attacks
Spoofing attacks
Traditional security mechanisms like heavy cryptographic systems and centralized IDS frameworks are not suitable due to:
Limited battery life.

#4 Objectives
Understand WSN security threats
Design IDS architecture for constrained devices
Apply lightweight ML models for anomaly detection
Analyze detection accuracy and false positive rate
Evaluate security–energy trade-offs

#5 Proposed Solutions 
The project follows a structured approach:

1️⃣ Threat & Attack Modeling
Define WSN attack types
Simulate adversarial behaviors

2️⃣ Lightweight IDS Framework
Feature extraction from:
Traffic patterns
Packet drop rates
Routing changes
Node energy usage
Hybrid detection.
Rule-based detection
Decision Tree / Isolation Forest

3️⃣ Simulation-Based Attack Scenarios
Normal traffic simulation
Attack injection
Data collection

4️⃣ Detection & Performance Analysis
Accuracy
Precision & Recall
False Positive Rate
Detection Latency
Energy Consumption

#6 Technology Stack
Programming Language
Python 
Libraries
NumPy
Pandas
Scikit-learn
Matplotlib

## 📊 Dataset
The models are trained using the **WSN-DS Dataset**. 
Due to file size limits, the full dataset is not included in this repo.
- **Download Link:** [[Link to your Kaggle dataset here](https://www.kaggle.com/datasets/azalhowaide/iot-dataset-for-intrusion-detection-systems-ids)]
- **Format:** CSV
- **Size:** ~550 MB
NetworkX (for network modeling) new
Tools
## 📊 Dataset
This project uses the **IoT dataset for Intrusion Detection Systems (IDS)**
- **Source:** [Kaggle - IoT IDS Dataset](https://www.kaggle.com/datasets/azalhowaide/iot-dataset-for-intrusion-detection-systems-ids)
- **Description:** It contains 23 statistically engineered features (mean, variance, count, etc.) extracted over 10-second windows.
- **Target Labels:** `0` for Attacks (Mirai, Gafgyt) and `1` for Normal samples.
Jupyter Notebook
VS Code
Git & GitHub
