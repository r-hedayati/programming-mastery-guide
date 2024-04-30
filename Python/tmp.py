words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
scores = [88, 92, 78, 90, 89, 76, 61]

long_word = [word for word in words if len(word)>5]
print(long_word)

word_lenght = {word: len(word) for word in words}
print(word_lenght)