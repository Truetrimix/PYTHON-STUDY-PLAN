#The Following makes reports from the sensor readings
sensor_readings = []
with open("/Users/simonlintu/Documents/Github/week2/day5_sensor_log.txt", "r") as file:
    for line in file:
        try:
            sensor_readings.append(float(line.strip()))
        except ValueError:
            print(f"Invalid reading: {line.strip()}")
if not sensor_readings:
    print("No valid sensor readings found.")

#The follwing functions are used to analyze the sensor readings and return the results
def date_time():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_number_of_readings(sensor_readings):
    return len(sensor_readings)

def get_min_reading(sensor_readings):
    return min(sensor_readings)

def get_max_reading(sensor_readings):
    return max(sensor_readings)

def get_average_reading(sensor_readings):
    return sum(sensor_readings) / len(sensor_readings) if sensor_readings else 0

def get_alert(sensor_readings, threshold=30):
    return any(reading > threshold for reading in sensor_readings)

def count_above_threshold(sensor_readings, threshold=30):
    count = 0
    for reading in sensor_readings:
        if reading > threshold:
            count += 1
    return count

#The main code: TheFollowing function generates a report from the sensor readings and saves it as a .txt file. If the file already exists, it will be overwritten.
def main():
    report_file_path = "/Users/simonlintu/Documents/Github/week2/reports/day6_sensor_log_report.txt"
    
    with open(report_file_path, "w") as report_file:
        report_file.write("Sensor Readings Analysis Report\n")
        report_file.write(f"Generated on: {date_time()}\n")
        report_file.write("----------------------------\n")
        report_file.write(f"Total number of readings: {get_number_of_readings(sensor_readings)}\n")
        report_file.write(f"Minimum reading: {get_min_reading(sensor_readings)}°C\n")
        report_file.write(f"Maximum reading: {get_max_reading(sensor_readings)}°C\n")
        report_file.write(f"Average reading: {get_average_reading(sensor_readings):.2f}°C\n")
        
        if get_alert(sensor_readings):
            report_file.write("ALERT: One or more readings are above 30°C!\n")
            report_file.write(f"Number of readings above 30°C: {count_above_threshold(sensor_readings)}\n")
        else:
            report_file.write("All readings are within the normal range.\n")
    print(f"Report generated and saved to {report_file_path}")
if __name__ == "__main__":
    main()