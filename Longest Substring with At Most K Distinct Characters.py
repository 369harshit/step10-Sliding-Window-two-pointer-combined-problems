def longest_substring_with_k_distinct_characters(s, k):
    max_length = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            distinct_chars = len(set(substring))
            if distinct_chars <= k:
                max_length = max(max_length, len(substring))
    return max_length

# Test cases
test_str_1 = 'abbbbbbc'
K_1 = 2
result_1 = longest_substring_with_k_distinct_characters(test_str_1, K_1)
print("Test 1 Result:", result_1)  # Output should be 7

test_str_2 = 'abcddefg'
K_2 = 3
result_2 = longest_substring_with_k_distinct_characters(test_str_2, K_2)
print("Test 2 Result:", result_2)  # Output should be 4
