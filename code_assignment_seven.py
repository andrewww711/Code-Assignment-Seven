# Open the file for reading
rfile = open("numbers.txt", "r")

# Initialize variables for the max value, min value, and running sum of all the numbers
maxvalue = float('-inf')
minvalue = float('inf')
runsum = 0
numbers = []

# View the first number listed in the number.txt file
data = rfile.readline()

# Loop through every line inside of the numbers.txt file
while data:
    # Convert the data to an integer
    data = int(data)

    # Check if the data is greater than the current max value
    if data > maxvalue:
        # If so, update the max value
        maxvalue = data

    # Check if the data is less than the current min value
    if data < minvalue:
        # If so, update the min value
        minvalue = data

    # Add the data to the running sum and list of numbers
    runsum += data
    numbers.append(data)

    # Read the next line of data from the file
    data = rfile.readline()

# Close the file
rfile.close()

# Print the results
print("Input Numbers:", numbers)
print("Max value:", maxvalue)
print("Min value:", minvalue)
print("Sum of values:", runsum)
