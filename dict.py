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
    #word = word.lower()
    if word in data:
        meanings = data[word]
        return "\n".join(meanings)
    elif word.title() in data:
        meanings = data[word.title()]
        return "\n".join(meanings)
    elif word.upper() in data:
        meanings = data[word.upper()]
        return "\n".join(meanings)
    else:
        matches = get_matches(word)
        if len(matches) == 0:
            return f"The word {word} doesn't exist. Please double check it."
        else:
            answer = input(f"Did you mean {matches[0]} instead? Yes (y) or No (n): ")
            if answer.lower() == "y":
                return definition(matches[0])
            elif answer.lower() == "n":
                return f"The word {word} doesn't exist. Please double check it."
            else:
                return "I don't understand that"
            
while True:    
    user_word = input("Enter your word:\n")
    print(definition(user_word))
