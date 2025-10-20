# AI-Powered Network Intrusion Detection System (NIDS)

Yeh ek AI-powered Network Intrusion Detection System (NIDS) ka proof-of-concept hai.

Yeh project `IsolationForest` (ek anomaly detection algorithm) ka istemaal karke network traffic mein hone waale attacks ya anomalies ko pehchaanne ke liye train kiya gaya hai.

---

## How It Works (Kaise Kaam Karta Hai)

Is project ke do mukhya bhaag hain:

1.  **`NIDS_Model_Training.ipynb`**: Yeh Jupyter Notebook CICIDS2017 dataset ko process karti hai. Yeh model ko sirf "Normal" (Benign) traffic par train karti hai aur do files save karti hai:
    * `nids_anomaly_detector_model.pkl` (Trained AI model)
    * `combined_real_traffic_features.csv` (Simulation ke liye test data)

2.  **`realtime_detector.py`**: Yeh script trained model (`.pkl`) ko load karti hai aur `combined_real_traffic_features.csv` file se data ko ek-ek karke padhti hai. Yeh real-time network traffic ka simulation karti hai aur jaise hi koi anomaly (attack) detect hota hai, yeh terminal par ek `[!!! ANOMALY ALERT !!!]` print karti hai.

---

## Installation & Setup (Kaise Run Karein)

Is project ko run karne ke liye neeche diye gaye steps follow karein.

### 1. Prerequisites (Zaroori Cheezein)

* Python 3.7+
* [CICIDS2017 Dataset](https://www.unb.ca/cic/datasets/ids-2017.html)

### 2. Step-by-Step Installation

1.  **Project ko Clone/Download karein:**
    ```bash
    git clone [https://github.com/KreeDox/ai-nids-project.git](https://github.com/KreeDox/ai-nids-project.git)
    cd ai-nids-project
    ```

2.  **Python Virtual Environment Banayein:**
    ```bash
    python -m venv venv
    ```
    *Windows par activate karein:*
    ```bash
    .\venv\Scripts\activate
    ```
    *Mac/Linux par activate karein:*
    ```bash
    source venv/bin/activate
    ```

3.  **Zaroori Libraries Install Karein:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Step-by-Step Run Karein

1.  **Data Taiyaar Karein (Sabse Zaroori Step):**
    * CICIDS2017 dataset (CSV files) ko download karein.
    * Project folder ke andar ek naya folder banayein jiska naam `MachineLearningCVE` ho.
    * Saari dataset CSV files ko uss `MachineLearningCVE` folder ke andar daal dein.

2.  **Model ko Train Karein:**
    * Apne terminal mein Jupyter Notebook chalaayein:
        ```bash
        jupyter notebook
        ```
    * Aapke browser mein, `NIDS_Model_Training.ipynb` file ko kholein.
    * Upar menu mein **Cell** -> **Run All** par click karein.
    * Isse aapke folder mein `.pkl` aur `.csv` files ban jaayengi.
    * Notebook ko band karein aur terminal par `Ctrl+C` daba kar server band kar dein.

3.  **Detector ko Activate Karein:**
    * Ab aap aakhiri script chala sakte hain:
        ```bash
        python realtime_detector.py
        ```
    * Aapka AI-NIDS ab active ho jaayega aur simulation shuru kar dega.

---

## Future Upgrades (Naye Ideas)

* **Attack Classification**: `IsolationForest` ki jagah `RandomForestClassifier` ka istemaal karke attack ka naam (DDoS, PortScan) batana.
* **Real-Time Alerts**: Telegram ya Discord bot integrate karna taaki attack detect hone par phone par notification aaye.
* **Live Sniffing**: `scapy` library ka istemaal karke CSV simulation ki jagah live network traffic ko monitor karna.
