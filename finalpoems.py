import random

with open('pfpoems1.txt') as f:
        lines = f.readlines()
        with open('poem5.txt','a') as a_open_file:
            a_open_file.write(random.choice(lines))