# Initialize variables
modulo_result = 50
modulo_result_zero_count = 0
zero_rotations_count = 0
modificator1 = 0
modificator = 0

# Read input.txt file
with open('01/input.txt', 'r') as file:
    lines = file.readlines()

# Process each line
for index, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    
    # Parse the operation
    operation = line[0]  # 'R' or 'L'
    number = int(line[1:])  # Extract the number
    
    # Apply the operation
    if operation == 'R':
        modulo_result += number
        quotient, modulo_result = divmod(modulo_result, 100) # Get quotient and new modulo_result
        zero_rotations_count += quotient # Count full rotations
    elif operation == 'L':
        modificator = -1 if modulo_result == 0 else 0
        modulo_result -= number
        quotient, modulo_result = divmod(modulo_result, 100) # Get quotient and new modulo_result
        modificator1 = 1 if modulo_result == 0 else 0
        zero_rotations_count -= quotient # Count full rotations
        zero_rotations_count += modificator # Adjust for zero case
        zero_rotations_count += modificator1 # Adjust for zero case


    # Apply modulo 100
    # modulo_result = modulo_result % 100
    
    # Check if modulo_result is 0
    if modulo_result == 0:
        modulo_result_zero_count += 1
    
    # Print first 100 lines
    if index < 100:
        print(f"Line {index + 1}: {line} -> modulo_result: {modulo_result}, modulo_result_zero_count: {modulo_result_zero_count}, zero_rotations_count: {zero_rotations_count}")

# Print results
print(f"Final modulo_result: {modulo_result}")
print(f"modulo_result_zero_count: {modulo_result_zero_count}")
print (f"zero_rotations_count: {zero_rotations_count}")