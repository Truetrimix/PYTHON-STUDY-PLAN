temperatures = [32, 35, 28, 30, 31, 29, 33, 34, 36, 37]
# Calculate the number of readings
num_readings = len(temperatures)
#sum the readings
sum_ = sum(temperatures)
# Calculate the highest reading
highest = max(temperatures)
# Calculate the lowest reading
lowest = min(temperatures)
# Calculate the average reading
average = sum(temperatures) / num_readings if num_readings > 0 else 0
# Check if the readings exceed a threshold
threshold = 30
alarm = any(reading > threshold for reading in temperatures)
# Print the statistics
print(f"Number of readings: {num_readings}")
print(f"Sum of readings: {sum_}")
print(f"Highest reading: {highest}")
print(f"Lowest reading: {lowest}")
print(f"Average reading: {average:.2f}")
for reading in temperatures:
    if reading > threshold:
        print(f"⚠️ ALERT: {reading} exceeds {threshold}")

#This code calculates the number of readings, the sum of readings, the highest reading, the lowest reading, and the average reading from a list of temperatures. It also checks if any reading exceeds a specified threshold and prints an alert if it does.