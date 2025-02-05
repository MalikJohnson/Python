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

#removing duplicates from array
def remove_duplicates(nums):
    return list(set(nums))

print(remove_duplicates([1,2,2,3,4,4,5]))

#merge two sorted arays
def merge_sorted(arr1, arr2):
    return sorted(arr1 + arr2)

print(merge_sorted([1,3,5], [2,4,6]))
