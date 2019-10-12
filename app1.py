import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    
    """function for translation"""
    w = w.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys()))>0:
        yn = input ("Did you mean %s instead?Enter Y if yes,or N if no:" % get_close_matches(w, data.keys())[0])
        if yn == "Y": return data[get_close_matches(w, data.keys())[0]]

        elif yn == "N":
            return "Word does not exist,please double check it"

        else:
            return "We didn't understand your entry"
             

               #we can put n=1,2,3,4,5,....(any number) instead of [0]

    else:
        print("Word is not exist")

"""Taking input fom the user and then displaying the result"""
word = input("Enter Word:")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

