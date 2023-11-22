def countGoodSubarrays(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = nums[i:j+1]
            unique_integers = set(subarray)
            if len(unique_integers) == k:
                count += 1
    return count

# Example usage:
nums = [1,2,1,2,3]
k = 2
result = countGoodSubarrays(nums, k)
print("Output:", result)
