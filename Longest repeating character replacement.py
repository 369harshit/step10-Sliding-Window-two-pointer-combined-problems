def character_replacement(s, k):
    max_length = 0
    n = len(s)

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            max_count = max(substring.count(char) for char in set(substring))

            if (j - i + 1 - max_count) <= k:
                max_length = max(max_length, j - i + 1)

    return max_length

# Example usage:
s = "ABAB"
k = 2
result = character_replacement(s, k)
print("Length of the longest substring:", result)
