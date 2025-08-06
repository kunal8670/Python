sentence = "apple banana apple orange banana mango"

words = sentence.split()  # ['apple', 'banana', 'apple', 'orange', 'banana', 'mango']
unique_words = list(set(words))

print("Unique Words:", unique_words)
