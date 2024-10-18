# Leetcode 918: https://leetcode.com/problems/maximum-sum-circular-subarray/description/
# Given a circular integer array nums of length n, 
# return the maximum possible sum of a non-empty subarray of nums.
def maxSubarraySumCircular(nums: list) -> int:
    maxSum = nums[0]
    currSum = 0
    laps = 0
    i = 0

    while laps < 2:
        if i == 0:
            laps += 1
        currSum = max(currSum, 0)
        currSum = max(nums[i], currSum + nums[i])
        maxSum = max(maxSum, currSum)
        i = (i + 1) % len(nums)
    return maxSum


def main():
    nums = [5,-3,5]
    print(maxSubarraySumCircular(nums)) # 10


if __name__ == "__main__":
    main()
