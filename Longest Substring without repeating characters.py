def longest_substring_without_repeating(s):
    max_length = 0
    max_substring = ""

    for i in range(len(s)):
        substring = ""
        for j in range(i, len(s)):
            if s[j] not in substring:
                substring += s[j]
            else:
                break

        if len(substring) > max_length:
            max_length = len(substring)
            max_substring = substring

    return max_substring, max_length

# Example usage:
input_string = "abcabcbb"
result = longest_substring_without_repeating(input_string)
print("Longest substring without repeating characters:", result)
