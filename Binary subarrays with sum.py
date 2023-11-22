def numSubarraysWithSum(nums, goal):
    count = 0
    n = len(nums)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == goal:
                count += 1
            elif current_sum > goal:
                break
    return count

nums = [1, 0, 1, 0, 1]
goal = 2
result = numSubarraysWithSum(nums, goal)
print("Number of subarrays with sum equal to", goal, ":", result)
