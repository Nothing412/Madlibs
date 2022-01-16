from ursina import *
import random
app = Ursina(borderless=False)
text_test = Text(text = "Work in progress")
random_madlib_text_int = random.randint(1,10)
if random_madlib_text_int == 1:
    print("make stuff later")

if random_madlib_text_int == 2:
    print("I have ______ cat")

if random_madlib_text_int == 3:
    print("I like ________")

if random_madlib_text_int == 4:
    print("I hate ________")

if random_madlib_text_int == 5:
    print("I ate _______ today")

if random_madlib_text_int == 6:
    print("I made _______")

if random_madlib_text_int == 7:
    print("make stuff later")

if random_madlib_text_int == 8:
    print("make stuff later")

if random_madlib_text_int == 9:
    print("make stuff later")

if random_madlib_text_int == 10:
    print("make stuff later")






app.run()