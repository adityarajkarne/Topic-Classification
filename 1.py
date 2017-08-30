#(1) a description of how you formulated the problem, including precisely defining the
# abstractions (e.g. HMM formulation); (2) a brief description of how your program works; (3) a discussion
# of any problems, assumptions, simplifications, and/or design decisions you made; and (4) answers to any
# questions asked below in the assignment.

import random

file = open("bc.train", 'r')
lines = file.readlines()
firsts=[]
for i in range(len(lines)):
    lines[i]=lines[i].strip().split(" ")
    firsts.append(lines[i][0])


print("--------------------------------------------part 2 output-------------------------------")
for i in range(5):
    counter=0
    next=random.choice(firsts)
    sentence=[next]
    while next not in (".","!","?"):
        nexts=[]
        for i in range(len(lines)):
            try:
                if next in lines[i]:
                    nexts=nexts+[lines[i][index+2] for index, word in enumerate(lines[i][:-2]) if word == next]
            except IndexError:
                pass
        next=random.choice(nexts)
        if next==";" :
            counter+=1
            if counter>5:
                while next!=";":
                    next = random.choice(sentence)
        sentence.append(next)

    print(" ".join(sentence))
