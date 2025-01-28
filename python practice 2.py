# python practice 2.py practicing python once again. Getting the basics back after using java for so long.
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.append(6)
print(my_list)
print(f"Length: {len(my_list)}")


#Basic dictionary testing
my_dict = {"apple": 3, "banana": 5, "cherry": 2}
print(my_dict)
print(my_dict["banana"])
my_dict["date"] = 7
print(my_dict)

#Some set usage for testing
my_set = {1, 2, 3, 2, 1}
print(my_set)
my_set.add(4)
print(my_set)
print(f"Is 3 in set? {'Yes' if 3 in my_set else 'No'}")

#More list testing
squares = [x**2 for x in range(10)]
print(squares)
evens = [x for x in squares if x % 2 == 0]
print(evens)

#range and a loop
for i in range(1, 6):
    print(f"Number: {i}")

#Some tuble basics
my_tuple = (1, 2, 3)
print(my_tuple)
print(my_tuple[1])

#using len and slciing 
my_list = [10, 20, 30, 40, 50]
print(len(my_list))
print(my_list[1:4])

#min max sum
numbers = [5, 10, 15, 20]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#enumerate test
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

#Test using zip
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

#Teesting out map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)

#Using filter for example
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

#Learning about any and all
nums = [2, 4, 6]
print(any(n % 2 != 0 for n in nums))  # False
print(all(n % 2 == 0 for n in nums))  # True

#Easy sorting check
numbers = [5, 3, 9, 1]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

#collections test
from collections import Counter
letters = ['a', 'b', 'a', 'c', 'b', 'a']
counter = Counter(letters)
print(counter)

#another sort test
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)

#learning about is instance? never used this one before
print(isinstance(5, int))
print(isinstance("hello", str))

#testing out help method
def add(a, b):
    """Return the sum of a and b."""
    return a + b

help(add)


#Learning about sleep in python
import time

print("Waiting for 2 seconds...")
time.sleep(2)
print("Done!")

#learning about random in python
import random

print(random.randint(1, 10))
