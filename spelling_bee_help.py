import nltk
from nltk.corpus import words
import random
from wordfreq import top_n_list

def contains_only(word, allowed_letters):
    return set(word).issubset(set(allowed_letters))

words = [word for word in top_n_list("en", 50000) if len(word) >= 4]

game = True
while game == True:

    candidates = []

    optional_chars = input("Input optional letters (6): ")
    if optional_chars.isalpha() and len(optional_chars) == 6:

        necessary_char = input("Input necessary letter (1): ")
        if necessary_char.isalpha() and len(necessary_char) == 1:

            # subset words
            for word in words:
                if (necessary_char in word) and (contains_only(word, optional_chars+necessary_char) == True):
                    candidates.append(word)
            
            game = False
        
        else:
            print("Invalid input")
    
    else:
        print("Invalid input")


candidates = sorted(candidates, key=len, reverse=True)
print(candidates[0:14])