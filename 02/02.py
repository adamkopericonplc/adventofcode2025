def fulfills_rule(num, repetitions=2):
    num_str = str(num)
    length = len(num_str)
    
    # Check if number of digits splits evenly into repetitions
    if length % repetitions != 0:
        return False
    
    # Calculate segment length
    segment_length = length // repetitions
    
    # Split number into segments
    segments = []
    for i in range(repetitions):
        start_idx = i * segment_length
        end_idx = start_idx + segment_length
        segments.append(num_str[start_idx:end_idx])
    
    # Check if all segments are equal (as numbers)
    first_segment = int(segments[0])
    for segment in segments[1:]:
        if int(segment) != first_segment:
            return False
    
    return True


def main():
    # Read the input file
    with open('02/input.txt', 'r') as f:
        data = f.read().strip()
    
    # Parse comma-separated ranges
    ranges = data.split(',')
    
    total_count = 0
    numbers_summary = 0
    
    # Process each range
    for range_str in ranges:
        print(range_str)
        start, stop = map(int, range_str.split('-'))
        
        # Loop through each number in the range
        for num in range(start, stop + 1):
            num_str = str(num)
            length = len(num_str)
            
            for repetitions in range(2, length+1):
                if fulfills_rule(num, repetitions):
                    print(num)
                    numbers_summary += num
                    total_count += 1
                    break  # Count each number only once
    
    print(f"\nTotal count: {total_count}")
    print(f"Numbers summary: {numbers_summary}")

if __name__ == "__main__":
    main()
