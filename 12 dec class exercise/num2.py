# Opening and reading the file
myFile1 = open('text2.txt', 'r')
lines = myFile1.readlines()

# Defining a list of punctuation characters
punctuation = ".","?","!"

# Defining a list of words that are always at the start of a sentence
first = ["Mr.", "Mrs", "r.","ms.", "i.e."]

# Iterating over the lines in the file
for line in lines:
    # Splitting each line into words
    words = line.split()
    
    # Iterating over the words in the line
    for word in words:
        # If the word is in the first list, print it without a line break
        if word.lower() in first:
            print(word + " ", end='')
        # If the word ends with a punctuation character, print it with a line break
        elif word[-1] in punctuation:
            print(word + "\n", end='')
        # Otherwise, print the word without a line break
        else:
            print(word + " ", end='')
