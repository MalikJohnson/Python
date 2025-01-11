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
