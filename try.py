#(1) a description of how you formulated the problem, including precisely defining the
# abstractions (e.g. HMM formulation); (2) a brief description of how your program works; (3) a discussion
# of any problems, assumptions, simplifications, and/or design decisions you made; and (4) answers to any
# questions asked below in the assignment.
"decide what to do with not founds(0s)"

print("--------------------------------------------part 3 output-------------------------------")
import itertools
#usr_input=input("Enter the sentence")
usr_input="There was a bird passed in there room"
usr_input=usr_input.lower().split(' ')
usr_set=set(usr_input)

#finding subs
subs={}
file=open("confused_words.txt","r")
lines = file.readlines()

for i in range(len(lines)):
    lines[i]=lines[i].strip().split(" ")
    for j in range(len(lines[i])):
        if lines[i][j] in usr_set:
            subs[lines[i][j]]=lines[i]


def pcalculator():
    #get counts
    counter={}
    plist=[0]*(len(usr_input)-1)
    ftrain = open("bc.train", 'r')
    train = ftrain.readlines()
    firsts=[]
    for i in range(len(train)):
        train[i]=train[i].strip().lower().split(" ")
        firsts.append(train[i][0])
        for j in range(len(train[i])):
            if train[i][j] in usr_set:
                if train[i][j] not in counter:
                    counter[train[i][j]]=1
                else:
                    counter[train[i][j]] += 1
                try:
                    if train[i][j+2]==usr_input[usr_input.index(train[i][j])+1]:
                        plist[usr_input.index(train[i][j+2])-1]+=1
                except IndexError:
                    pass

    # #calculate p
    pfinals=[firsts.count(usr_input[0])/len(firsts)]+[plist[i]/counter[usr_input[i]] for i in range(len(plist))]
    z=sorted(set(pfinals))[1]/len(firsts)
    pmod=[z if pfinals[i]==0 else pfinals[i] for i in range(len(pfinals))]

    p=1
    for elem in pmod:
        p*=elem
    return p




change = []
for word in usr_input:
    if word in subs:
        change.append(subs[word])
print(list(itertools.product(*change)))


















