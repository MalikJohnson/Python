def is_palindrome(word):
    return word == word[::-1]

if __name__ == "__main__":
    input_word = input("Enter a word to check: ")
    if is_palindrome(input_word):
        print(f"'{input_word}' is a palindrome.")
    else:
        print(f"'{input_word}' is not a palindrome.")
