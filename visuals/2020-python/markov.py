import re
import random
import nltk

# importing, lower-casing and removing punctuation from text, tokenizing
text = open('example.txt').read()
text = text.lower()
text = re.sub(r"[,.';\"?!]+\ *", " ", text)
text = re.sub("\n", " ", text)
words_tokens = nltk.word_tokenize(text)

# creating empty dictionary for ngrams, and using variable to decide length of ngrams
ngrams = {}
words = 3

# looping through words to create ngrams
for i in range(len(words_tokens)-words):
    sequence = ' '.join(words_tokens[i:i+words])
    # create
    if sequence not in ngrams.keys():
        ngrams[sequence] = [words_tokens[i+words]]
    else:
        ngrams[sequence].append(words_tokens[i+words])

# picking a random start point
start_point = random.randint(0, len(words_tokens)-words)
curr_sequence = ' '.join(words_tokens[start_point:start_point + words])

output = curr_sequence

for i in range(100):
    possible_words = ngrams[curr_sequence]
    # picking out the most likely word
    possible_words = sorted(possible_words, key = possible_words.count, reverse = True)
    next_word = possible_words[0]
    # adding the most likely word onto the list
    output += ' ' + next_word
    seq_words = nltk.word_tokenize(output)
    curr_sequence = ' '.join(seq_words[len(seq_words)-words:len(seq_words)])

print(output)