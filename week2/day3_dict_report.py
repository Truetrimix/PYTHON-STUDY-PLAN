#Regional data
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

# Code will print the region and its corresponding temperature
print('Region temperatures:')
print('------------------')
for region, temperature in region_data.items():
    print(f"{region}, Temperature: {temperature}°C")

print('------------------')
print('Analysing high temperatues:')

#The following alerts if one or more regions in region_data is bigger then a given threshold and only prints the regions that exceeds the threshold
threshold = 30
for region, temperature in region_data.items():
    if temperature > threshold:
        print(f"⚠️ ALERT: {region} has high temperatures of {temperature}°C!")
   
print('------------------')

#The following function calculates the average temperature of all regions in region_data
def average_temperature(region_data):
    total_temperature = sum(region_data.values())
    num_regions = len(region_data)
    return total_temperature / num_regions if num_regions > 0 else 0

print(f'The average temperature today is: {average_temperature(region_data)}°C')
print('------------------')

#The following function tells the ragion with the highest temperature and the temperature
def highest_temperature(region_data):
    highest_region = max(region_data, key=region_data.get)
    highest_temp = region_data[highest_region]
    return highest_region, highest_temp
print(f'The highest temperature today is in {highest_temperature(region_data)[0]} with {highest_temperature(region_data)[1]}°C')