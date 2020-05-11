# Program using external modules and API

from random import choice
from termcolor import colored
from pyfiglet import figlet_format
import requests


def display_joke(user_input):
    url = "https://icanhazdadjoke.com/search"

    data = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": user_input}
    ).json()

    results = data["results"]

    # 'total_jokes' is a key in dict data similar to 'results' and 'id'
    if data['total_jokes'] == 0:
        print("No result found! Try a different search term.")
    elif data['total_jokes'] == 1:
        print(f"I have got one joke about {user_input}. Here's one: ")
        print(results['joke'])
    else:
        print(
            f"I have got {len(results)} jokes about {user_input}. Here's one: ")
        print(choice(results)['joke'])


string_print = "Dad Joke 3000"
col = "magenta"

title = figlet_format(string_print)
print(colored(title, col), end="\n \n")


user_input = input("Let me tell you a joke! Give me a topic:  ")

display_joke(user_input)


"""
# Results is a list of dicts:

[{'id': 'iGJeVKmWDlb', 'joke': 'My cat was just sick on the carpet, I don’t think it’s feline well.'}, 
{'id': '8UnrHe2T0g', 'joke': '‘Put the cat out’ … ‘I didn’t realize it was on fire'}, 
{'id': 'daaUfibh', 'joke': 'Why was the big cat disqualified from the race? Because it was a cheetah.'}, 
{'id': 'BQfaxsHBsrc', 'joke': 'What do you call a pile of cats?  A Meowtain.'}, 
{'id': 'O7haxA5Tfxc', 'joke': 'Where do cats write notes?\r\nScratch Paper!'}, 
{'id': '0wcFBQfiGBd', 'joke': 'Did you hear the joke about the wandering nun? She was a roman catholic.'}, 
{'id': 'TS0gFlqr4ob', 'joke': 'What do you call a group of disorganized cats? A cat-tastrophe.'}, 
{'id': 'AQn3wPKeqrc', 'joke': 'It was raining cats and dogs the other day. I almost stepped in a poodle.'}, 
{'id': '39Etc2orc', 'joke': 'Why did the man run around his bed? Because he was trying to catch up on his sleep!'}, 
{'id': '1wkqrcNCljb', 'joke': "Did you know that protons have mass? I didn't even know they were catholic."}]
"""
