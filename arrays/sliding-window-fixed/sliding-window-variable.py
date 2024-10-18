# Find the length of the longest subarray, 
# with the same value in each position.

# Time: O(n^2)
def longestSubarrayBruteForce(nums: list) -> int:
    length = 0

    for l in range(len(nums)):
        for r in range(l, len(nums)):
            if nums[l] != nums[r]:
                break
            length = max(length, r - l + 1)
    return length

# Time: O(n)
def longestSubarray(nums: list) -> int:
    length = 0
    l = 0

    for r in range(len(nums)):
        if nums[l] != nums[r]:
            l = r
        length = max(length, r - l + 1)
    return length

def main():
    nums = [4, 2, 2, 3, 3, 3, 2, 2]
    print(longestSubarray(nums)) # 3
    print(longestSubarrayBruteForce(nums)) # 3


if __name__ == "__main__":
    main()