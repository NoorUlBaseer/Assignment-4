"""
Question-2: Word Frequency Counter

Create a program that reads a text input from the user and then calculates the frequency of each word in the
input. You need to create a function that takes the text as input, processes it, and returns a dictionary with
the word frequencies.

Requirements:

1. Create a function named word frequency that takes a string (text input) as an argument.
2. Inside the function, tokenize the input string into words (split by spaces and punctuation).
3. Count the frequency of each word and store the results in a dictionary.
4. The keys of the dictionary should be the unique words, and the values should be the corresponding frequencies.
5. Ignore the case of the words (convert all words to lowercase) to treat "Word" and "word" as the same word.
6. Display the word frequencies to the user in a clear and organized format.
"""

def word_frequency(text):
    text = text.lower()
    words = text.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def display_word_freq(word_freq):
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

text = input("Enter text: ")
word_freq = word_frequency(text)
display_word_freq(word_freq)