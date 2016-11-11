# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
import nltk
import random
from nltk.book import text2

# get first 150 tokens
tokens = text2.tokens[:150]
print("Original text tokens:")
print(tokens)

# get tagged tokens, create tag map
tagged_tokens = nltk.pos_tag(tokens)
tag_map = {"NN": "a noun", "NNP": "a singular proper noun", "VB": "a verb", "JJ": "an adjective",
           "VBD": "a past tense verb"}

# 15% for noun and proper noun, 10% for others
probabilities = {"NN": .15, "NNP": .15, "VB": .1, "JJ": .1, "VBD": .1}

final_words = []

# add spaces to non special characters -- taken from sample with added special characters in text2
def spaced(word_or_character):
    if word_or_character in [",", ".", "?", "!", ":", "[", "]"]:
        return word_or_character
    else:
        return " " + word_or_character


for (word, tag) in tagged_tokens:
    if tag not in probabilities or random.random() > probabilities[tag]:
        final_words.append(spaced(word))
    else:
        modified_word = input("Please enter %s (replacing %s):\n" % (tag_map[tag], word))
        final_words.append(spaced(modified_word))

print("New text:")
print("".join(final_words))
