
from termcolor import colored
from pyfiglet import figlet_format

def ascii_art(text, col="Magenta"):
    try:
        result = figlet_format(text)
        final = colored(result, col)
    except:
        print("Enter a valid color!")
    else:
        print(final)


text = input("What message do you want to print? ")
col = input("What color? ")

ascii_art(text, col)





