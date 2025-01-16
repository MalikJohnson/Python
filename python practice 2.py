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
