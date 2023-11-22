def maxScore(cardPoints, k):
    n = len(cardPoints)
    max_score = 0

    for i in range(k + 1):
        left_sum = sum(cardPoints[:i])
        right_sum = sum(cardPoints[n - k + i:])
        max_score = max(max_score, left_sum + right_sum)
    return max_score

cardPoints = [1,2,3,4,5,6,1]
k = 3
result = maxScore(cardPoints, k)
print("Maximum points:", result)
