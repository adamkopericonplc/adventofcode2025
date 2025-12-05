import time


def read_input(filename):
    ranges = []
    candidates = []
    parsing_ranges = True
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            
            if parsing_ranges:
                if not line:  # Empty line found
                    parsing_ranges = False
                    continue
                parts = line.split('-')
                ranges.append((int(parts[0]), int(parts[1])))
            else:
                candidates.append(int(line))
    
    ranges.sort(key=lambda x: x[0])
    return ranges, candidates


def optimize_ranges(ranges):
    optimized_ranges = []
    temp_range = None
    
    for current_range in ranges:
        if temp_range is None:
            temp_range = list(current_range)
            continue
        
        if current_range[0] > temp_range[1]:
            optimized_ranges.append(tuple(temp_range))
            temp_range = list(current_range)
        else:
            if current_range[1] > temp_range[1]:
                temp_range[1] = current_range[1]
    
    if temp_range is not None:
        optimized_ranges.append(tuple(temp_range))
    
    return optimized_ranges


def count_candidates_in_ranges(candidates, optimized_ranges):
    count = 0
    for candidate in candidates:
        for start, end in optimized_ranges:
            if start <= candidate <= end:
                count += 1
                break
    return count


def count_natural_numbers_in_ranges(optimized_ranges):
    total = 0
    for start, end in optimized_ranges:
        total += (end - start + 1)
    return total


def main():
    start_time = time.time()
    ranges, candidates = read_input('input.txt')
    read_time = time.time() - start_time
    
    print(f"Number of ranges: {len(ranges)}")
    print(f"First 5 ranges: {ranges[:5]}")
    print()
    print(f"Number of candidates: {len(candidates)}")
    print(f"First 5 candidates: {candidates[:5]}")
    print()
    
    start_time = time.time()
    optimized_ranges = optimize_ranges(ranges)
    optimize_time = time.time() - start_time
    
    print(f"Number of optimized ranges: {len(optimized_ranges)}")
    print(f"First 5 optimized ranges: {optimized_ranges[:5]}")
    print()
    
    start_time = time.time()
    count = count_candidates_in_ranges(candidates, optimized_ranges)
    count_candidates_time = time.time() - start_time
    
    print(f"Candidates contained in optimized ranges: {count}")
    print()
    
    start_time = time.time()
    total_natural_numbers = count_natural_numbers_in_ranges(optimized_ranges)
    count_natural_time = time.time() - start_time
    
    print(f"Total natural numbers in optimized ranges: {total_natural_numbers}")
    print()
    print("Execution times:")
    print(f"  Read input: {read_time:.6f}s")
    print(f"  Optimize ranges: {optimize_time:.6f}s")
    print(f"  Count candidates in ranges: {count_candidates_time:.6f}s")
    print(f"  Count natural numbers: {count_natural_time:.6f}s")
    print(f"  Total: {read_time + optimize_time + count_candidates_time + count_natural_time:.6f}s")


if __name__ == "__main__":
    main()