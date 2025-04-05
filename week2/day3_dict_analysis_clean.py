# 🌍 Regional Temperature Analysis - Clean Structure Version
# Separates logic into functions and keeps main() as the control panel.

region_data = {
    "North": 30.5,
    "South": 25.4,
    "East": 29.8,
    "West": 22.8,
    "Central": 30.5,
    "Northeast": 31.7,
    "Southwest": 20.8,
    "Coastal": 24.5
}

# 🔍 Print all region data
def print_region_data(data):
    print("📍 Region Temperatures:")
    for region, temp in data.items():
        print(f"{region}: {temp}°C")
    print('------------------')

# 🚨 Check for high temperatures and print alerts
def print_temperature_alerts(data, threshold):
    print(f"🚨 Analyzing temperatures over {threshold}°C:")
    for region, temp in data.items():
        if temp > threshold:
            print(f"⚠️ ALERT: {region} is hot at {temp}°C!")
    print('------------------')

# 📈 Calculate the average temperature
def average_temperature(data):
    total_temp = sum(data.values())
    count = len(data)
    return total_temp / count if count > 0 else 0

# 🔥 Find the region with the highest temperature
def highest_temperature(data):
    highest_region = max(data, key=data.get)
    return highest_region, data[highest_region]

# 🎛 Main controller
def main():
    print_region_data(region_data)
    
    print_temperature_alerts(region_data, threshold=30)

    avg = average_temperature(region_data)
    print(f"🌡️ Average Temperature: {avg:.2f}°C")

    hottest_region, hottest_temp = highest_temperature(region_data)
    print(f"🔥 Hottest Region: {hottest_region} at {hottest_temp}°C")

# Entry point for the program
if __name__ == "__main__":
    main()
