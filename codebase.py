import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Simulated function to generate or load data (replace with real data acquisition logic)
def get_smart_plug_data():
    # Simulate voltage and current data
    time = np.linspace(0, 10, 100)  # 10 seconds sampled at 100 points
    voltage = 230 + 5 * np.sin(2 * np.pi * 0.5 * time)  # Simulated voltage with noise
    current = 10 + 2 * np.sin(2 * np.pi * 0.5 * time + np.pi / 4)  # Simulated current with noise

    # Create a DataFrame to mimic smart plug data
    data = pd.DataFrame({
        'Time (s)': time,
        'Voltage (V)': voltage,
        'Current (A)': current
    })
    return data

# Load data (replace this with your real smart plug data source)
data = get_smart_plug_data()

# Extract voltage and current
time = data['Time (s)'].values
voltage = data['Voltage (V)'].values
current = data['Current (A)'].values

# Load pre-trained TensorFlow model (replace 'model_path' with your actual model path)
def load_model():
    try:
        model = tf.keras.models.load_model('model_path')  # Update with the correct path to your model
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

model = load_model()

# Prepare data for prediction
if model:
    features = np.column_stack((voltage, current))  # Combine voltage and current as input features
    predictions = model.predict(features)

    # Simulate mapping predictions to appliance types
    appliance_types = ['Fan', 'Bulb', 'Toaster', 'Blender']  # Example appliance types
    predicted_appliances = [appliance_types[np.argmax(pred)] for pred in predictions]

    # Append predictions to the data
    data['Predicted Appliance'] = predicted_appliances

    print("Predicted appliances:")
    print(data[['Time (s)', 'Voltage (V)', 'Current (A)', 'Predicted Appliance']])

# Plot voltage and current
plt.figure(figsize=(12, 6))

# Voltage plot
plt.subplot(2, 1, 1)
plt.plot(time, voltage, label='Voltage (V)', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Voltage over Time')
plt.grid(True)
plt.legend()

# Current plot
plt.subplot(2, 1, 2)
plt.plot(time, current, label='Current (A)', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Current over Time')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()