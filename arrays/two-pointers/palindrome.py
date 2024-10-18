# Check if an array is a palindrome.

# Time: O(n)
def isPalindrome(nums: list) -> bool:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        if nums[l] != nums[r]:
            return False
        l += 1
        r -= 1
    return True 

def main():
    nums1 = [1, 2, 7, 7, 2, 1] # true
    nums2 = [1, 2, 7, 6, 2, 1] # false

    print(isPalindrome(nums1))
    print(isPalindrome(nums2))


if __name__ == "__main__":
    main()