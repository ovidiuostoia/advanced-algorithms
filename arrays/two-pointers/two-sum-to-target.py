# Given a sorted input array, return the two indices of two elements
# which sum up to the target value. Assume there's exactly one solution.

def twoSum(nums: list, target: int) -> tuple:
    l, r = 0, len(nums) - 1

    while l < r:
        curr = nums[l] + nums[r]
        if curr < target:
            l += 1
        elif curr > target:
            r -= 1
        else:
            return (l, r)
    return None

def main():
    target = 7
    nums = [-1, 2, 3, 4, 8, 9]
    print(twoSum(nums, target)) # (0, 4)


if __name__ == "__main__":
    main()