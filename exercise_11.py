import json

"""
this method simply takes all the key values given from the find_all_keys method
and with a loop finds the key with the most occurences.
"""
def find_most_popular(d):
    keys = []
    for k in find_all_keys(d):
        keys.append(k)
    counter = 0
    most_frequent = keys[0]
    for i in keys:
        curr_frequency = keys.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            most_frequent = i
    return most_frequent


"""
this method is responsible for finding all the key occurences of keys
in a nested dict or list. using yield we can expect continuous values without
stopping the execution and by using recursion we check the element in its
entirety. the only difference between logic of finding a list
or a dict is that in a dict we need to yield the dict's key
"""
def find_all_keys(d):
    if isinstance(d, dict):
        for key, value in d.items():
            if type(value) is dict or type(value) is list:
                yield key
                yield from find_all_keys(value)
            else:
                yield key
    elif isinstance(d, list):
        for v in d:
            yield from find_all_keys(v)


if __name__ == '__main__':
    filename = str(input("Please insert the name of the file you want to analyze: "))
    f = open(f"{filename}.txt", "r")
    example_text = f.read()
    example = json.loads(example_text)
    print(f"The most popular key in the following dictionary which was extracted from {filename}.txt : {example_text} is: {find_most_popular(example)}")
    f.close()
