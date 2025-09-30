# Save this file as realtime_detector.py
import joblib
import pandas as pd
import time

# --- Configuration ---
MODEL_FILE = 'nids_anomaly_detector_model.pkl'
SIMULATED_TEST_DATA = 'simulated_traffic_data.csv' 
FLOW_RATE = 0.005 # Delay in seconds between flows for fast simulation

# --- 1. Load Model and Data ---
try:
    nids_model = joblib.load(MODEL_FILE)
    df_simulated = pd.read_csv(SIMULATED_TEST_DATA, low_memory=False)
except FileNotFoundError:
    print("Error: Model or Data file not found. Ensure you ran all Phase 1 & 2 steps in Jupyter.")
    exit()

# --- 2. Prepare Data for Streaming Simulation ---
# Prepare X (features) for streaming (dropping only the 'Binary_Label' used for testing)
X_simulated = df_simulated.drop(columns=['Binary_Label']).astype('float32')
print(f"Loaded {len(X_simulated)} flows for monitoring.")


# --- 3. The Detection Loop (Simulating Real-Time) ---
alert_count = 0
total_flows = len(X_simulated)

print("\n--- AI-Powered NIDS ACTIVATED (Simulated) ---")

for i in range(total_flows):
    flow_data = X_simulated.iloc[i:i+1] # Take one row (flow) at a time
    
    # Predict the anomaly score (1=Normal, -1=Anomaly)
    prediction = nids_model.predict(flow_data)
    
    if prediction[0] == -1:
        alert_count += 1
        print(f"\n[!!! ANOMALY ALERT !!!] Flow {i+1} flagged as Intrusion.")
        
    if i % 1000 == 0 and i != 0:
        print(f"[STATUS] Processed {i} flows. Total alerts: {alert_count}")

    time.sleep(FLOW_RATE)

print("\n--- SIMULATION COMPLETE ---")
print(f"Final Anomaly Alerts Detected: {alert_count}")
