#This code Reads a .txt file. Extracts each line as a float (temperature reading). Then Prints: Total readings, Min, Max, Averageand Alerts for any reading > 30°C

#The Following reads the excact file path to get the file on a mac and floats the readings
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
def number_of_readings(sensor_readings):
    return len(sensor_readings)

def min_reading(sensor_readings):
    return min(sensor_readings)

def max_reading(sensor_readings):
    return max(sensor_readings)

def average_reading(sensor_readings):
    return sum(sensor_readings) / len(sensor_readings) if sensor_readings else 0

def alert(sensor_readings, threshold=30):
    return any(reading > threshold for reading in sensor_readings)

def count_above_threshold(sensor_readings, threshold=30):
    count = 0
    for reading in sensor_readings:
        if reading > threshold:
            count += 1
    return count

def main():
    print("Sensor Readings Analysis")
    print("----------------------------")
    print(f"Total number of readings: {number_of_readings(sensor_readings)}")
    print(f"Minimum reading: {min_reading(sensor_readings)}°C")
    print(f"Maximum reading: {max_reading(sensor_readings)}°C")
    print(f"Average reading: {average_reading(sensor_readings):.2f}°C")
    
    if alert(sensor_readings):
        print("ALERT: One or more readings are above 30°C!")
        print(f"Number of readings above 30°C: {count_above_threshold(sensor_readings)}")
  
    else:
        print("All readings are within the normal range.")
if __name__ == "__main__":
    main()




