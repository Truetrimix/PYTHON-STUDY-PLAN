# 🧠 Sensor Statistics Analyzer with Modular Design
# This script reads temperature readings from a file, analyzes them,
# and prints summary statistics with optional alerts.

def read_sensor_file(sensor_log):
    """Reads sensor values from a text file and converts them to float."""
    with open(sensor_log, 'r') as file:
        return [float(line.strip()) for line in file.readlines()]

def calculate_statistics(sensor_readings, threshold=30):
    """
    Calculates number of readings, min, max, and average.
    Also checks if any reading exceeds the given threshold.
    """
    num_readings = len(sensor_readings)
    highest = max(sensor_readings)
    lowest = min(sensor_readings)
    average = sum(sensor_readings) / num_readings if num_readings > 0 else 0
    alarm = any(reading > threshold for reading in sensor_readings)
    return num_readings, highest, lowest, average, alarm

def print_statistics(num_readings, highest, lowest, average, alarm, threshold=30):
    """Prints nicely formatted statistics and optional alert if threshold exceeded."""
    print(f"📊 Number of readings: {num_readings}")
    print(f"📈 Highest reading: {highest}")
    print(f"📉 Lowest reading: {lowest}")
    print(f"📊 Average reading: {average:.2f}")
    if alarm:
        print(f"⚠️ ALERT: One or more values exceeded the threshold of {threshold}!")
    else:
        print("✅ No alert triggered. All readings within normal range.")

def main():
    sensor_log = 'sensor_log.txt'  # 📂 Input file (should be in the same folder)
    sensor_readings = read_sensor_file(sensor_log)
    stats = calculate_statistics(sensor_readings, threshold=30)
    print_statistics(*stats, threshold=30)

if __name__ == "__main__":
    main()
