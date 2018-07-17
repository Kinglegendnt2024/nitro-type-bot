# randomly choose buttons


import keyboard as kb
alpha_l = ["a",
           "b",
           "c",
           "d",
           "e",
           "f",
           "g",
           "h",
           "i",
           "j",
           "k",
           "l",
           "m",
           "n",
           "o",
           "p",
           "q",
           "r",
           "s",
           "t",
           "u",
           "v",
           "w",
           "x",
           "y",
           "z"]

alpha_u = []
for el in alpha_l:
    alpha_u.append(el.upper())

punc = [".", ",", "?", "!"]


all_list = alpha_l + alpha_u + punc


while True:
    for l in all_list:
        kb.send(l)
