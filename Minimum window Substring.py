from collections import Counter

def min_window_substring(s, t):
    if not s or not t:
        return ""
    
    # Function to check if a window contains all characters of 't'
    def contains_all_chars(window):
        for char, count in t_count.items():
            if window[char] < count:
                return False
        return True
    
    t_count = Counter(t)
    min_window = ""
    min_window_length = float('inf')
    
    for i in range(len(s)):
        for j in range(i + len(t), len(s) + 1):
            window = Counter(s[i:j])
            if contains_all_chars(window) and j - i < min_window_length:
                min_window = s[i:j]
                min_window_length = j - i
    
    return min_window

# Test case
s = "ADOBECODEBANC"
t = "ABC"
print(min_window_substring(s, t))  # Output: "BANC"
