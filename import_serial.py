import os
import serial
from datetime import datetime
import time

# Arduino serial port, change it according to your system
ARDUINO_PORT = 'COM9'
BAUD_RATE = 9600
TIMEOUT = 1  # Seconds

def main():
    # Open serial connection to Arduino
    ser = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=TIMEOUT)

    # Create a folder to store data
    folder_name = 'arduino_data'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Display Maca3D pic at the start of each data log session
    print("\033[1;33m" + " " * 20 + "Maca3D\n" + "\033[0m")
    print("\033[1;33m" + " " * 16 + "0000000" + "\033[0m")
    print("\033[1;33m" + " " * 14 + "0000000000" + "\033[0m")
    print("\033[1;33m" + " " * 12 + "000000000000" + "\033[0m")
    print("\033[1;33m" + " " * 10 + "00000000000000" + "\033[0m")
    print("\033[1;33m" + " " * 9 + "0000000000000000" + "\033[0m")
    print("\033[1;33m" + " " * 9 + "0000000000000000" + "\033[0m")
    print("\033[1;33m" + " " * 9 + "0000000000000000" + "\033[0m")
    print("\033[1;33m" + " " * 10 + "00000000000000" + "\033[0m")
    print("\033[1;33m" + " " * 11 + "000000000000" + "\033[0m")
    print("\033[1;33m" + " " * 12 + "0000000000" + "\033[0m")
    print("\033[1;33m" + " " * 14 + "00000000" + "\033[0m")
    print("\033[1;33m" + " " * 16 + "000000" + "\033[0m")

    while True:
        # Print timestamp at the start of each data log session
        print("\nData log session started at:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        # Create a new file for data logging
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f"{folder_name}/data_{timestamp}.txt"
        with open(file_name, 'w') as file:
            file.write("Timestamp,Data\n")  # Writing header to the file

        # Record data for 5 minutes
        start_time = time.time()
        prev_data = None  # Initialize variable to store previous data
        while (time.time() - start_time) < 300:  # 5 minutes
            data = ser.readline().decode().strip()
            if data and data != prev_data:  # Check if data is received and different from previous data
                with open(file_name, 'a') as file:
                    file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{data}\n")
                print(data)
                prev_data = data  # Update previous data
        time.sleep(0.1)  # Sleep to avoid busy-waiting
        file.write("\nData log session started at:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == "__main__":
    main()
