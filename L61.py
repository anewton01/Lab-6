#the authors names are Abby Newton and Mandy Guo
def too_long(string):
    if len(string)>140:
        print("This message is too long for SMS")
    else:
        print("This message can be sent!")

import unicodedata
unicodedata.lookup("snake")
unicodedata.lookup("dog")
unicodedata.lookup("rose")

unicodedata.lookup("sun")
unicodedata.lookup("cat")
unicodedata.lookup("two hearts")

print(unicodedata.lookup("two hearts"), "you")
print("Here comes the", unicodedata.lookup("sun"))
print("That was so funny!", unicodedata.lookup("rolling on the floor laughing"))
print("I can't look", unicodedata.lookup("face with peeking eye"))
print(unicodedata.lookup("balloon"),"Happy Birthday!")

print(unicodedata.name("&"))
print(unicodedata.name("["))
print(unicodedata.name("/"))

