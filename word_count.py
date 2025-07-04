def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def find_most_common_word(word_count):
    max_count = -1
    most_common_word = None
    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_common_word = word
    return most_common_word

if __name__ == "__main__":
    words_list = ["apple", "banana", "apple", "orange", "banana", "banana"]
    word_count = count_words(words_list)
    most_common_word = find_most_common_word(word_count)
    print(f"The most common word is: {most_common_word}")
