def cascade_through_slots(passed_number, slots, slot_idx, number_of_slots):
    if slot_idx >= number_of_slots:
        return
    
    if passed_number >= slots[slot_idx]:
        cascade_through_slots(slots[slot_idx], slots, slot_idx + 1, number_of_slots)
        slots[slot_idx] = passed_number
        

def analyze_line(line, number_of_slots=2):
    # Initialize slots with the last number_of_slots digits from the line
    # slots[0] = next-to-last (d1), slots[1] = last (d2), etc.
    slots = []
    for i in range(number_of_slots - 1, -1, -1):
        slots.append(int(line[-(i + 1)]))
    
    # Iterate from end to start, omitting the last number_of_slots digits
    for i in range(len(line) - number_of_slots - 1, -1, -1):
        cascade_through_slots(int(line[i]), slots, 0, number_of_slots)
            
    # Calculate result: slots[0] * 10^(n-1) + slots[1] * 10^(n-2) + ... + slots[n-1]
    result = 0
    for i, slot_value in enumerate(slots):
        result += slot_value * (10 ** (number_of_slots - 1 - i))
    
    return result

def main():
    total_sum = 0
    
    # Read input file
    with open('input.txt', 'r') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if line:  # Skip empty lines
                result = analyze_line(line, 12)
                print(f"Line {line_num}: {result}")
                total_sum += result
    
    print(f"\nTotal sum: {total_sum}")


if __name__ == "__main__":
    main()
