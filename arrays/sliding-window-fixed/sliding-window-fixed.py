# Given an array, return true if there are two elements within 
# a window of a size k that are equal.

# Time: O(n*k)
def closeDuplicatesBruteForce(nums: list, k: int) -> bool:
    for l in range(len(nums)):
        for r in range(l + 1, min(len(nums), l + k)):
            if nums[l] == nums[r]:
                return True
    return False

# Time: O(n)
def closeDuplicates(nums: list, k: int) -> bool:
    window = set()
    l = 0

    for r in range(len(nums)):
        if r - l + 1 > k:           # reached the window size
            window.remove(nums[l])  # remove from the set the value from the window's start
            l += 1                  # shift the window to the right
        if nums[r] in window:
            return True
        window.add(nums[r])
    return False

def main():
    nums = [1, 2, 3, 2, 3, 4]
    print(closeDuplicatesBruteForce(nums, 2)) # false
    print(closeDuplicatesBruteForce(nums, 3)) # true

    print(closeDuplicates(nums, 2)) # false
    print(closeDuplicates(nums, 3)) # true


if __name__ == "__main__":
    main()