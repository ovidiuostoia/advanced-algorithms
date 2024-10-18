# Find the minimum length subarray where the sum is greater
# than or equal to the target. Assume all values are positive.

# Time: O(n^2)
def minLengthSubarraySumBruteForce(nums: list, target: int) -> int:
    length = float("inf")

    for l in range(len(nums)):
        sum = 0
        for r in range(l, len(nums)):
            sum += nums[l] + nums[r] if l != r else nums[l]
            if sum >= target:
                length = min(length, r - l + 1)
    return 0 if length == float("inf") else length

# Time: O(n)
def minLengthSubarraySum(nums: list, target: int) -> int:
    length = float("inf")
    sum, l = 0, 0

    for r in range(len(nums)):
        sum += nums[r]
        while sum >= target:
            length = min(length, r - l + 1)
            sum -= nums[l]
            l += 1
    return 0 if length == float("inf") else length


def main():
    target = 6
    nums = [2, 3, 1, 2, 4, 3]
    print(minLengthSubarraySumBruteForce(nums, target))
    print(minLengthSubarraySum(nums, target))

if __name__ == "__main__":
    main()