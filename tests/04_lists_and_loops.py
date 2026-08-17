"""
Part 4: Lists and Loops

A list is an ordered collection of items.
Loops let you process each item without writing code for each one.

Run: python tests/04_lists_and_loops.py
"""

print("\n" + "="*70)
print("LISTS AND LOOPS")
print("="*70)

# Create a list
temperatures = [25.5, 22.3, 28.1, 24.0, 26.5]

print("\nExample 1: Create and access a list")
print(f"  List: {temperatures}")
print(f"  First temperature: {temperatures[0]}")
print(f"  Last temperature: {temperatures[-1]}")
print(f"  Number of items: {len(temperatures)}")

print("\n" + "-"*70)
print("WORKING WITH LISTS")
print("-"*70)

# Add items
print("\nAdding items:")
temperatures.append(27.0)
print(f"  After append: {temperatures}")

# Remove items
print("\nRemoving items:")
temperatures.remove(22.3)
print(f"  After remove: {temperatures}")

# Sort items
print("\nSorting:")
sorted_temps = sorted(temperatures)
print(f"  Sorted: {sorted_temps}")

print("\n" + "-"*70)
print("LOOPING THROUGH LISTS")
print("-"*70)

# Simple for loop
print("\nSimple loop through temperatures:")
for temp in temperatures:
    print(f"  {temp}°C")

# Loop with index
print("\nLoop with index:")
for index, temp in enumerate(temperatures):
    print(f"  Index {index}: {temp}°C")

# Loop with range
print("\nLoop with range:")
for i in range(3):
    print(f"  Iteration {i}")

print("\n" + "-"*70)
print("LIST OF DICTIONARIES (Common in IoT)")
print("-"*70)

sensor_readings = [
    {"sensor_id": "sensor-01", "temperature_c": 25.5},
    {"sensor_id": "sensor-02", "temperature_c": 22.3},
    {"sensor_id": "sensor-03", "temperature_c": 28.1},
]

print("\nLoop through list of dictionaries:")
for reading in sensor_readings:
    print(f"  {reading['sensor_id']}: {reading['temperature_c']}°C")

print("\n" + "-"*70)
print("FINDING ITEMS IN LISTS")
print("-"*70)

# Find maximum
print("\nFind maximum temperature:")
max_temp = max(temperatures)
print(f"  Max: {max_temp}°C")

# Find minimum
print("\nFind minimum temperature:")
min_temp = min(temperatures)
print(f"  Min: {min_temp}°C")

# Sum and average
print("\nCalculate statistics:")
total = sum(temperatures)
average = total / len(temperatures)
print(f"  Sum: {total}°C")
print(f"  Average: {average:.2f}°C")

# Filter items
print("\nFilter temperatures above 25°C:")
high_temps = [t for t in temperatures if t > 25]
print(f"  {high_temps}")

print("\n" + "-"*70)
print("WHY LOOPS?")
print("-"*70)

print("""
✓ Handle multiple items without repeating code
✓ Work with unknown number of items
✓ Clean, readable code
✓ Easy to maintain changes
""")

print("\n" + "="*70)
print("EXERCISES")
print("="*70)

print("""
1. Create a list of 5 sensor readings (floats)
   - Print each one with its index

2. Find and print:
   - The highest temperature
   - The lowest temperature
   - The average temperature

3. Create a list of sensor dictionaries:
   [{"id": "sensor-01", "temp": 25}, ...]
   - Loop through and print formatted data

4. Filter the list to show only sensors with temp > 26°C

5. Count how many sensors have temperature > 25°C
""")
