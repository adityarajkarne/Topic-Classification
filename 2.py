#(1) a description of how you formulated the problem, including precisely defining the
# abstractions (e.g. HMM formulation); (2) a brief description of how your program works; (3) a discussion
# of any problems, assumptions, simplifications, and/or design decisions you made; and (4) answers to any
# questions asked below in the assignment.

print("--------------------------------------------part 3 output-------------------------------")
import itertools
usr_input=input("Enter the sentence")
usr_input = usr_input.lower().split(' ')
original=usr_input[:]
usr_set = set(usr_input)

#finding subs
subs={}                                     #will store word as a key and a list of confused words as value
file=open("confused_words.txt","r")
lines = file.readlines()

for i in range(len(lines)):
    lines[i]=lines[i].strip().split(" ")
    for j in range(len(lines[i])):
        if lines[i][j] in usr_set:
            subs[lines[i][j]]=lines[i]
indices=[i for i in range(len(usr_input)) if usr_input[i] in subs] #gets all indices that represent confused words


def pcalculator(gen_input):
    gen_set = set(gen_input)
    #get counts
    counter={}                                              #stores individual counts
    plist=[0]*(len(gen_input)-1)                            #stores all transition probabilities,p12 stored in index1
    ftrain = open("bc.train", 'r')
    train = ftrain.readlines()
    firsts=[]                                               #stores all first words of the sentence
    for i in range(len(train)):
        train[i]=train[i].strip().lower().split(" ")
        firsts.append(train[i][0])
        for j in range(len(train[i])):
            if train[i][j] in gen_set:
                if train[i][j] not in counter:
                    counter[train[i][j]]=1
                else:
                    counter[train[i][j]] += 1
                try:
                    if train[i][j+2]==gen_input[gen_input.index(train[i][j])+1]:   #if next word in text is the next word in sentence
                        plist[gen_input.index(train[i][j+2])-1]+=1
                except IndexError:
                    pass

    # #calculate p
    pfinals=[firsts.count(gen_input[0])/len(firsts)]+[plist[i]/counter[gen_input[i]] for i in range(len(plist))]  #po,follwed by transition probabilities
    z=sorted(set(pfinals))[1]/len(firsts)                                                                         #for not found cases min/length
    pmod=[z if pfinals[i]==0 else pfinals[i] for i in range(len(pfinals))]
    p=1
    for elem in pmod:
        p*=elem
    return p


change = []
for word in usr_input:
    if word in subs:
        change.append(subs[word])
combo=list(itertools.product(*change))              #generates all possible combinations that can be inserted in the sentence

suggest=0
best=[]
for tups in combo:
    for (k,v) in list(zip(indices,tups)):
        usr_input[k]=v
    new=pcalculator(usr_input)
    if  new > suggest:
        suggest= new
        best=usr_input[:]

if best==original:
    print("This seems alright!")
else:
    print("Substitute with:"," ".join(best))















