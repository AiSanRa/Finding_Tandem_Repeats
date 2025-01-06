def find_tandem_repeats(s):
    n = len(s)
    repeats = []
    
    # Iterate over possible repeat lengths (from 1 to n//2)
    for length in range(1, n//2 + 1):
        # Slide through the string, checking pairs of substrings of 'length'
        for i in range(n - 2 * length + 1):
            first = s[i:i + length]
            second = s[i + length:i + 2 * length]
            if first == second:
                repeats.append((i, length))
    
    return repeats


input_string = "ABAABAABBBA"
repeats = find_tandem_repeats(input_string)
print(f"Tandem repeats found: {repeats}")
