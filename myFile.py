print("Welcome to Dictionary")
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def returnMeaning(word):
    word = word.lower()
    if word in data:
        printOutput(word)
    elif word.title() in data:
        printOutput(word.title())
    elif word.upper() in data:
        printOutput(word.upper())
    elif len(get_close_matches(word,data.keys())) > 0:
        print("Did you mean %s instead?" %get_close_matches(word,data.keys())[0])
        ans = input("Press 'Y' if Yes else 'N' : ")
        ans = ans.lower()
        if ans == "y":
            output = data[get_close_matches(word,data.keys())[0]]
            for item in output:
                print(item)
        elif ans == "n":
            print("Word not found in Dictionary")
        else:
            print("We didn't understnd your query")
    else:
        print("Word not found in Dictionary")

def printOutput(word):
    output = data[word]
    for item in output:
        print(item)
word = input("Enter Word : ")
returnMeaning(word)
