import os.path
import re

var_file = "two_cities_ascii.txt"
if not os.path.isfile(var_file):
    print("File not found.")
else:

    words = []
    for i in range(20): # we need only 20 different groups since the maximum sum is 20
        words.append([])

    print(words)

    f1 = open(var_file, "r")

    flag = 1
    while flag:

        line = f1.readline()
        clean_line = re.sub(r"[^a-zA-Z]+", " ", line) # useful technique in order to get rid of non-letter characters.
        flag = clean_line != "" # if the clean_line variable is not empty then we continue reading the file
        if flag:
            y = clean_line.split() # split the lines into words.
            for item in y:
                if len(item) < 20:
                    words[len(item)].append(item) # append the word to its corresponding group

    f1.close()

    print('len words:', len(words))

    for i in range(len(words)):
        print(i, " - ", words[i])

    for i in range(1, 11): # there 10 different 20-sum pairings, 1-19,2-18,3-17...,10-10
        while len(words[i]) > 0 and len(words[20 - i]) > 0 and len(words[10]) > 1:
            if i != 10: # in each loop pop the pair 1-19 until there  are no words left and continue to the next pairing of 2-18 etc.
                print(words[i][0], " - ", words[20 - i][0], " - ", i, 20 - i)
                words[i].pop(0)
                words[20 - i].pop(0)

            elif i == 10 and len(words[i]) > 1: # with the same logic do this for the 10-10 pairing.
                print(words[i][0], " - ", words[i][1], " - ", i, 20 - i)
                words[i].pop(0)
                words[i].pop(0)
