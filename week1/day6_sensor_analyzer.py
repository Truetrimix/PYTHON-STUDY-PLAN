print("Day 6: Sensor Analyzer")
print("========================\n")

def read_sensor_file(sensor_log):
    with open(sensor_log, 'r') as file:
        return [float(line.strip()) for line in file.readlines()]

def analyze_data(data):
    return min(data), max(data), sum(data) / len(data)

def check_thresholds(data, limit):
    for value in data:
        if value > limit:
            print(f"Warning: Sensor value {value} exceeds the limit of {limit}")

def main():
    data = read_sensor_file("sensor_log.txt")
    min_val, max_val, avg_val = analyze_data(data)
    print(f"Min: {min_val}, Max: {max_val}, Avg: {avg_val:.2f}")
    check_thresholds(data, 30.0)

if __name__ == "__main__":
    main()
