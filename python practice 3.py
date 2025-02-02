#classic reverse string
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

#another palindrome check using reverse
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
