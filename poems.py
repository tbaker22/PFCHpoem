import random
#my first attempt to pick out random lines.
#def random_line(poetry_foundation_poems):
    #lines = open(poetry_foundation_poems).read().splitlines()
    #return random.choice(lines)
#print(random_line('poem1.txt'))

#This code just prints random lines to the terminal, but I want to see if I can write it to a file.
#with open('pfpoems.txt') as f:
    #lines = f.readlines()
    #print(random.choice(lines))

#with open('pfpoems.txt') as f:
    #lines = f.readlines()
    #print(random.choice(lines))

#This is what I tried to make it so that I create a file that would store the different lines of poetry that are randomly selected into one file to create a new poem. But it would just create the file, and then write one randomly chosen line, but when I tried to do multiple lines, nothing happened.
    #with open('poem1.txt','a') as a_open_file:
        #a_open_file.write(random.choice(lines))

#This was my second attempt to print multiple lines into a single document, but it still would only write one line and just replace whatever was written to the file before, while completely different lines would print in the terminal, despite the fact that I didn't have an active print statement. I realized it wasn't working because I had originally kept the 'w' in with statement, when I didn't need to since the file was already created.
        # with open('poem1.txt','a') as a_open_file:
            # a_open_file.write(random.choice(lines))

#Next I realized I wanted to clean the file a bit, and take out all instances of the '<|endoftext|>'. That's what this code below tried to do. I tried to also figure out how to potentially skip the titles with the author, but I couldn't.
with open('pfpoems.txt','r') as f:
    lines = f.readlines()
with open('pfpoems1.txt','w') as f:
    for line in lines:
        if line.strip('\n') !='<|endoftext|>':
            f.write(line)

#and now the code again to write a file and then append random lines into that file to create a new poem.
    with open('pfpoems1.txt') as f:
        lines = f.readlines()
        #print(random.choice(lines))

        #with open('poem2.txt','a') as a_open_file:
            #a_open_file.write(random.choice(lines))

        # with open('poem3.txt','w') as a_open_file:
            # a_open_file.write(random.choice(lines))
        #with open('poem3.txt','a') as a_open_file:
            #a_open_file.write(random.choice(lines))

        with open('poem4.txt','a') as a_open_file:
            a_open_file.write(random.choice(lines))