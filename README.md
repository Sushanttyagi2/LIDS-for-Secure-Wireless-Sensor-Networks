# Lightweight Hybrid Intrusion Detection System for Wireless Sensor Networks (LIDS-WSN)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5+-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)

A **lightweight and energy-efficient** Hybrid Intrusion Detection System designed specifically for resource-constrained **Wireless Sensor Networks (WSNs)**.

It combines **Rule-based detection** (fast & low-energy) with **Decision Tree** (accurate & interpretable) to detect common WSN attacks while minimizing battery consumption.

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
python -m venv venv

# Windows:
venv\Scripts\activate
# Linux / Mac:
# source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

## 🚀 How to Run
1. Full Simulation (Recommended)
   python main_simulation.py
   
   What it does:
   
. Generates synthetic WSN dataset with attacks
. Trains the Lightweight Hybrid IDS
. Saves the best model (lids_decision_tree.pkl)
. Generates evaluation plots and energy trade-off analysis

2. Test the Best Model
   python use_best_model.py

3. Launch Web Dashboard (Interactive)
   streamlit run app/app.py

4. Google Colab Version
   Open wsn_ids_colab.py in Google Colab and run all cells.

s.

📊 Expected Results

Accuracy: 92–96% (on synthetic data)
Low latency using Rule-based first approach
Visualizations saved in results/ folder:
Confusion Matrix
Feature Importance
Energy vs Accuracy Trade-off



🔬 Supported Attacks

Attack Type,Main Indicators Detected By
Sinkhole,High packet rate + High drop rate
Selective Forwarding,Moderate to high packet drop rate
Sybil,Sudden increase in neighbor count
Spoofing,Very low energy + High routing changes

🖥️ Web Dashboard Features

Real-time attack detection by adjusting sensor parameters
Live prediction with latency display
Model information and dataset overview
Clean and user-friendly interface


🛠 Technologies Used

Python 3.8+
scikit-learn (Decision Tree + Isolation Forest)
pandas, numpy
matplotlib & seaborn
Streamlit (Web UI)
joblib (Model persistence)


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
https://grok.com/share/c2hhcmQtMg_c2f1c860-2870-4757-a579-d43a048a6bb8
Tools
## 📊 Dataset
This project uses the **IoT dataset for Intrusion Detection Systems (IDS)**
- **Source:** [Kaggle - IoT IDS Dataset](https://www.kaggle.com/datasets/azalhowaide/iot-dataset-for-intrusion-detection-systems-ids)
- **Description:** It contains 23 statistically engineered features (mean, variance, count, etc.) extracted over 10-second windows.
- **Target Labels:** `0` for Attacks (Mirai, Gafgyt) and `1` for Normal samples.
Jupyter Notebook
VS Code
Git & GitHub
