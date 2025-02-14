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

#anagram check
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

#find max in array
def find_max(nums):
    return max(nums)

print(find_max([1,5,3,9,2]))

#counting vowles in string
def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

print(count_vowels("Hello World"))

#reverse words in a sentence
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverse_words("hello world this is python"))

#unique char check
def all_unique(s):
    return len(set(s)) == len(s)

print(all_unique("abcde"))
print(all_unique("hello"))

#finding first non repeating char
from collections import Counter

def first_non_repeating_char(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

print(first_non_repeating_char("leetcode"))
print(first_non_repeating_char("aabbcc"))

#classic fizzbuzz
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(15)

#count words in a string
def count_words(s):
    return len(s.split())

print(count_words("Hello world this is Python"))

#check balanced parentheses 
def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

print(is_balanced("()[]{}"))
print(is_balanced("([)]"))
