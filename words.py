def find_long_words(word_list, n):
    
    long_words = [word for word in word_list if len(word) > n]
    return long_words

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
n = 5
result = find_long_words(words, n)

print(f"Words longer than {n} characters: {result}")
