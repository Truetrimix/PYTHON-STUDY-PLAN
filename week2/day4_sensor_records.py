#Sensor Records
sensor_records = [
    {"sensor_id": "S1", "temp": 33.4, "status": "OK"},
    {"sensor_id": "S2", "temp": 30.0, "status": "HIGH"},
    {"sensor_id": "S3", "temp": 26.7, "status": "HIGH"},
    {"sensor_id": "S4", "temp": 34.0, "status": "OK"},
    {"sensor_id": "S5", "temp": 29.4, "status": "OK"},
    {"sensor_id": "S6", "temp": 24.3, "status": "HIGH"},
    {"sensor_id": "S7", "temp": 26.9, "status": "OK"},
    {"sensor_id": "S8", "temp": 30.5, "status": "OK"}
]

#Count how many sensors are above 30°C and store the count in a variable
def if_temp_above_30(records):
    count = 0
    for record in records:
        if record["temp"] > 30:
            count += 1
    return count

#Find HIGH status sensors
def find_high_status_sensors(records):
    high_status_sensors = []
    for record in records:
        if record["status"] == "HIGH":
            high_status_sensors.append(record)
    return high_status_sensors

#Calculate average temp of all "OK" sensors
def calculate_average_temp_ok_sensors(records):
    total_temp = 0
    count = 0
    for record in records:
        if record["status"] == "OK":
            total_temp += record["temp"]
            count += 1
    return total_temp / count if count > 0 else 0

#Main function to execute the tasks
def main():
   print("Sensor Records Analysis")
   print("----------------------------")
   print(f"Number of sensors above 30°C: {if_temp_above_30(sensor_records)}")
   print("Sensors with HIGH status:")
   for sensor in find_high_status_sensors(sensor_records):
       print(f"Sensor ID: {sensor['sensor_id']}, Temperature: {sensor['temp']}°C, Status: {sensor['status']}")
   print(f"Average temperature of OK sensors is: {calculate_average_temp_ok_sensors(sensor_records):.2f}°C")
if __name__ == "__main__":
    main()
