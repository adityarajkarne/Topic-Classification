

## Reads the file the same way label.py does
def read_data(fname):
    exemplars = []
    file = open(fname, 'r');
    for line in file:
        data = tuple([w.lower() for w in line.split()])
        exemplars += [ (data[0::2], data[1::2]), ]

    return exemplars

start = read_data('bc.test')
print(start)

## Start of the training portion
def training(data):
    all_words= []
    all_parts=[]
    sentences = []
    parts = []
    for x in data:
        sentences.append(x[0])  #creates sentences
        parts.append(x[1])  #creates parts of speech fo each sentence
    for i in sentences:
        for i in i:
            all_words.append(i)  #list of every word (not set)
    for i in parts:
        for i in i:
            all_parts.append(i)  #list of every part of speech (not set)

    words_set=list(set(all_words))  #word set if needed
    parts_set=list(set(all_parts))  #parts os speech set if needed

    initial_words=[i[0] for i in sentences]  #initial words, from all_words
    initial_parts=[i[0] for i in parts]  #initial pos, from all_parts
#
#     ## calculated the maximum of a list or list of lists
#     def max_calc(list):
#         maximum = [0, 0]
#         for i in list:
#             if i[1] > maximum[1]:
#                 maximum = i
#         return maximum
#
#     def init_word_prob(word):
#         return [word, float(initial_words.count(word))/float(len(initial_words))]  #initial probability of a word
#
#     def init_part_prob(part):
#         return [part, float(initial_parts.count(part))/float(len(initial_parts))]  #initial probability of a pos
#
#     def word_prob(word):
#         return [word, float(all_words.count(word))/float(len(all_words))]  #probability the word exists --> P(w)
#
#     def parts_prob(part):
#         return [part, float(all_parts.count(part)) / float(len(all_parts))]  #probability the pos exists --> P(s)
#
#     def word_part_list(sample):  #creates a list of all words and their respective pos -->  [word,pos]
#         matched=[]
#         for i in sample:
#             for n in range(len(i[0])):
#                 matched.append([i[0][n],i[1][n]])
#         return matched
#
#
#     ## this one below may need to be tweaked. i think this is usefull for the assignment (if the sentence is provided, this is part of calculating the most probable POS
#     def parts_give_word(word):  #returns a list of all the parts of speech if the word is supplied
#         parts_found=[]
#         for i in word_part_list(data):
#             if i[0]==word:
#                 parts_found.append(i[1])
#         return parts_found
#
#     # pgw = "Part of speech given word"
#     def pgw_calc(word):     #this calculates the probabilities of the pos given the word (used formula above) --> returns only the maximum, but doesn't use the max def at the top
#         probs=[]
#         for i in parts_give_word(word):
#             probs.append([i,float(parts_give_word(word).count(i))/float(len(parts_give_word(word)))])
#         maximum=[0,0]
#         for i in probs:
#             if i[1]>maximum[0]:
#                 maximum=i
#         return maximum
#
#     def words_give_parts(part): #this is the same as the calculations above but for words given the part of speech
#         words_found=[]
#         for i in word_part_list(data):
#             if i[1]==part:
#                 words_found+=i[0]
#         return words_found
#
#     #wgp = "word given pos"
#     def wgp_calc(part):
#         probs=[]
#         for i in words_give_parts(part):
#             probs.append([i,float(words_give_parts(part).count(i))/float(len(words_give_parts(part)))])
#         maximum=[0,0]
#         for i in probs:
#             if i[1]>maximum[0]:
#                 maximum=i
#         return maximum
#
#     def trial(test):  #This was the initial calculations for the input sentence, it uses pgw_calc
#         output=[]
#         for i in test:
#             output.append((pgw_calc(i)[0]))
#         return output
#
#     print("Thinking...")
#     print (" ".join(trial(true_test)))
#
#     ## Calculates the most likely initial part of speech
#     t=[init_part_prob(i) for i in parts_set]
#     #print max_calc(t)
#
#
#
#
#
# test = 'There is time to study'
# true_test = test.lower().split(' ')
# print ("Input sentence:")
# print (test,"\n")
# training(start)
#
