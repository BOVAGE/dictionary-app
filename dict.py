import json
from difflib import get_close_matches

#opens the dictionary file
with open("data.json", "r") as file:
    #gets the file content as dict
    data = json.load(file)

def get_matches(word: str):
    """ returns list of strings word matches in data keys """
    matches = get_close_matches(word, data.keys(), cutoff = 0.85) 
    return matches

def definition(word: str):
    """ returns the definition of word """
    word = word.lower()
    try:
        meanings = data[word] 
    except KeyError:
        matches = get_matches(word)
        if len(matches) == 0:
            return f"The word {word} doesn't exist. Please double check it."
        else:
            answer = input(f"Did you mean {matches[0]} instead? Yes (y) or No (n): ")
            if answer.lower() == "y":
                return definition(matches[0])
            else:
                return "Bye"
    else:
        return "\n".join(meanings)

while True:
    userWord = input("Enter your word:\n")
    print(definition(userWord))
