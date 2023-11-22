def countSubstrings(s):
    count = 0
    n = len(s)

    # Iterate through all possible substrings
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            if 'a' in substring and 'b' in substring and 'c' in substring:
                count += 1

    return count

s = "abcabc"
result = countSubstrings(s)
print("Number of substrings:", result)
