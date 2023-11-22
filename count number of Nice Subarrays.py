def countNiceSubarrays(nums, k):
    count = 0

    # Function to count odd numbers in a subarray
    def countOdds(arr):
        count = 0
        for num in arr:
            if num % 2 == 1:
                count += 1 
        return count

    # Iterate through all subarrays
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = nums[i:j + 1]
            if countOdds(subarray) == k:
                count += 1

    return count

# Example
nums = [1,1,2,1,1]
k = 3
result = countNiceSubarrays(nums, k)
print("Number of nice subarrays:", result)
