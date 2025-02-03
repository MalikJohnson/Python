#classic reverse string
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

#another palindrome check using reverse
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))

#another twosum test this time with python and using hashmap
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

print(two_sum([2,7,11,15], 9))
