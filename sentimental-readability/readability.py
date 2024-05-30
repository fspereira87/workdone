# TODO

from cs50 import get_string

phrase = get_string("Text: ")
letters = 0
words = 1
sentences = 0

for i in range(len(phrase)):

    if phrase[i].isalpha():
        letters += 1

    elif phrase[i] == " ":
        words += 1

    elif phrase[i] == "." or phrase[i]== "!" or phrase[i]== "?":
        sentences += 1



L = (letters/words)*100
S = (sentences/words)*100

score = 0.0588*L-0.296*S-15.8
score = round(score)

if score < 1:

    print ("Before Grade 1")

elif score > 16:

    print ("Grade 16+")

else:

    print ("Grade", score)





