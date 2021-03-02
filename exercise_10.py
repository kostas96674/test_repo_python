"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    Instructions to run program:
    Put the input file in the same directory as the python file.
    Run the program normally and give only the file name as the input.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import json


def find_depth(element): # helper method to initiate the recursion
    if len(element) == 0: # do not proceed if the element is empty and return 0
        return 0
    return dig(element)

"""
with recursion we check all possible nested paths, using the map() method,
and then we successively return the deepest path to be added until we reach
the top again. if the element is neither a list or a dict we have reached the
end of that path and we start going back.

"""
def dig(element):
    if isinstance(element, dict):
        return 1 + max(map(dig, element.values()))
    elif isinstance(element, list):
        return 1 + max(map(dig, element))
    else:
        return 0


if __name__ == '__main__':
    filename = str(input("Please insert the name of the file you want to analyze: "))
    f = open(f"{filename}.txt", "r")
    example_text = f.read()
    example = json.loads(example_text)
    print(f"The depth of the following dictionary {example_text}, extracted from {filename}.txt is: {find_depth(example)}")
    f.close()
