sentence = "Data science is fun and insightful"

# Write a dictionary comprehension that maps each word to its length.

word_length = {
    word : len(word) for word in sentence.strip().split(" ")
}

print(word_length)