#This is filer prectice
temperatures = [
    30.2, 25.9, 27.2, 27.4, 24.6,
    31.2, 33.3, 26.3, 28.1, 32.3,
    28.0, 26.6, 31.8, 34.5, 24.1
]
#last 5 readings
print(f'Last 5 readings {temperatures[-5:]}')

# list of readings over 30, version 1
highs = []
for temperature in temperatures:
    temp = temperature
    if temp > 30:
        highs.append(temp)
print(f'This are the readings over 30 {highs}')

# list of readings over 30, version 2
highs2 = [temperature for temperature in temperatures if temperature > 30]
print(f'This are the readings over 30 based code version 2 {highs2}')

#This are the average of the readings over 30
average = sum(highs2) / len(highs2) if highs2 else 0
print(f'The avaverage of the readings over 30 is {average:.2f}')

#This is a filter example
filtered = [temperature for temperature in temperatures if temperature > 30]
print(f'This are the filtered readings over 30 {filtered}')
