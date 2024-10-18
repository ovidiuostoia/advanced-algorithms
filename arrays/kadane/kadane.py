# Leetcode 53: https://leetcode.com/problems/maximum-subarray
# Find a non-empty subarray with the largest sum.

# Time: O(n^2)
# Space: O(n)
def kadaneBruteForce(nums: list) -> int:
    maxSum = nums[0]

    for i in range(len(nums)):
        currSum = 0
        for j in range(i, len(nums)):
            currSum += nums[j]
            maxSum = max(maxSum, currSum)
    return maxSum

# Time: O(n)
# Space: O(n)
def kadane(nums: list) -> list:
    maxSum = nums[0]
    currSum = 0

    for n in nums:
        currSum = max(currSum, 0)
        currSum += n
        maxSum = max(maxSum, currSum)
    return maxSum

def main():
    a = [4, -1, 2, -7, 3, 4]

    print(kadaneBruteForce(a))  # 7
    print(kadane(a))            # 7

if __name__ == "__main__":
    main()