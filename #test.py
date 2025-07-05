#test

word = "my string"
word2 = "5 dollar"
word3 = "6 cents"

def remove_whitespace_and_digits(text):
    new_list = []

    for char in text:
        if char.isspace() or char.isdigit():
            continue
        new_list.append(char)

    return new_list

    

print(remove_whitespace_and_digits(word))   
print(remove_whitespace_and_digits(word2))  
print(remove_whitespace_and_digits(word3)) 