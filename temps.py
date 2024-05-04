import wmi
import time

def get_cpu_temperature():
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_info = w.Sensor()
    for sensor in temperature_info:
        if sensor.SensorType == 'Temperature' and sensor.Name == 'CPU Package':
            return sensor.Value

while True:
    cpu_temp = get_cpu_temperature()
    print(f"CPU Temperature: {cpu_temp}°C")
    time.sleep(1)  # Adjust the delay as needed
