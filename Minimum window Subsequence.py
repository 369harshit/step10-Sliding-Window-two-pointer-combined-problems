def min_window_subsequence(s, t):
    min_len = float('inf')
    min_window = ""
    
    for i in range(len(s)):
        if s[i] == t[0]:
            t_index = 0
            for j in range(i, len(s)):
                if s[j] == t[t_index]:
                    t_index += 1
                    if t_index == len(t):
                        window_len = j - i + 1
                        if window_len < min_len:
                            min_len = window_len
                            min_window = s[i:j+1]
                        break
    return min_window

# Example usage:
S = "abcdebdde"
T = "bde"
result = min_window_subsequence(S, T)
print("Minimum window subsequence:", result)
