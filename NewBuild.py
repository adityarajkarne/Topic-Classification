import math

class Solver:
    #General note: pos = 'Parts of speech'
    initial = {}
    transition = {}
    emission = {}
    words_dict = {}
    parts_dict = {}
    pos_prob = {}

    trans_count = 0
    sent_len = []

    ## Creates a dictionary with the probability as values
    def prob(self, input_data):
        for i in range(len(input_data)):
            total = sum(input_data[i].values())
            for x in input_data[i].keys():
                input_data[i][x] = (input_data[i][x], input_data[i][x] / total)
        return input_data
    #logarithmic posterior probability
    def posterior(self, sentence, pos):
        sum = float(0)
        temp_calc = math.log(1)
        for i in range(len(sentence)):
            emmission = self.emission[(sentence[i], pos[i])]
            if emmission == 0:
                emmission = 1.00000/10.00000**10
            sum += emmission * self.pos_prob[pos[i]]
            temp_calc += math.log(emmission * self.pos_prob[pos[i]])
            posterior_prob = temp_calc - math.log(sum)
        return posterior_prob


    def train(self, data):
        self.transition = {}
        self.emission = {}
        self.words_dict = {}
        self.parts_dict = {}
        self.trans_count = 0

        for i in data:
            #learning from each word of given sentence
            for x in range(len(i[0])):
                try:    #length of longest sentence
                    self.sent_len[x][i[1][x]] = self.sent_len[x].get(i[1][x], 0) + 1.0
                except IndexError:
                    self.sent_len += [{i[1][x]:1.0}]  #length of 1, otherwise
                #counts the words
                if i[0][x] not in self.words_dict:
                    self.words_dict[i[0][x]] = 1.0
                else:
                    self.words_dict[i[0][x]] += 1.0
                #counts the POS
                if i[1][x] not in self.parts_dict:
                    self.parts_dict[i[1][x]] = 1.0
                else:
                    self.parts_dict[i[1][x]] += 1.0
                #Initial POS
                if x == 0:
                    if i[1][x] not in self.initial:
                        self.initial[i[1][x]] = 1.0
                    else:
                        self.initial[i[1][x]] += 1.0
                else:   #transitions
                    temp_trans = (i[1][x-1], i[1][x])

                    if temp_trans not in self.transition:
                        self.transition[temp_trans] = 1.0
                        self.trans_count += 1.0
                    else:
                        self.transition[temp_trans] += 1.0
                        self.trans_count += 1.0
                #counts of all the emissions
                if (i[0][x], i[1][x]) not in self.emission:
                    self.emission[(i[0][x], i[1][x])] = 1.0
                else:
                    self.emission[(i[0][x], i[1][x])] += 1.0
        ## Emission prob
        for i in self.words_dict.keys():
            for x in self.parts_dict.keys():
                if (i, x) in self.emission:
                    self.emission[(i, x)] /= self.parts_dict[x]
        ## Initial probs
        for i in self.parts_dict.keys():
            self.initial[i] /= len(data)
        ## Simple prob of POS
        for i in self.parts_dict.keys():
            self.pos_prob[i] = self.parts_dict[i] / sum(self.parts_dict.values())
        ## Transition Probs
        for x in self.parts_dict.keys():
            for y in self.parts_dict.keys():
                if (x, y) not in self.transition:
                    self.transition[(x, y)] = 1.000/10.000**10
                else:
                    self.transition[(x, y)] /= self.parts_dict[x]
        #Assumes that if the word wasn't found or tagged in the training file that it was 'itching' to show up
        #Therefore, at 1/(all words + 1) it's assumed to had been the very next word that didn't make the cut...
        for i in range(len(self.sent_len)):
            if len(self.parts_dict.keys()) != len(self.sent_len[i].keys()):
                for pos in set(self.parts_dict.keys()) - set(self.sent_len[i].keys()):
                    self.sent_len[i][pos] = 1/(len(self.words_dict.keys())+1)
        self.sent_len = self.prob(self.sent_len)


    def hmm_viterbi(self, sentence):
        print_out = []
        temp_dict = {}
        pos_sentence = {} #pos_sentence is a sentence made of only POSs
        #wors on initial word
        for POS in self.parts_dict.keys():
            if (sentence[0], POS) not in self.emission:
                self.emission[(sentence[0], POS)] = 1/(len(self.emission)+1) #as if it would have been the next emission
            prob = float(self.initial[POS] * self.emission[(sentence[0], POS)])
            temp_dict[(POS, 0)] = prob
        #works the rest of the sentence for potential POSs and compares them --NOT LAST WORD IN SENTENCE
        for x in range(1, len(sentence)):
            for potential_pos1 in self.parts_dict.keys():
                max_prob = float(0)
                likely_pos = None
                for potential_pos2 in self.parts_dict.keys():
                    prob = temp_dict[(potential_pos2, x-1)] * self.transition[(potential_pos2, potential_pos1)]
                    if prob > max_prob:
                        max_prob = prob
                        likely_pos = potential_pos2
                #if probability is zero then tag 'noun' POS
                if max_prob == 0:
                    max_prob = 0.001
                    likely_pos = 'noun'  #independent analysis showed noun at 18.5% recurrance, so we assigned
                                         #the default value on 'noun' and bumped the max prob to .001 just in case
                temp_dict[(potential_pos1, x)] = self.emission[(sentence[x], potential_pos1)] * max_prob
                pos_sentence[(potential_pos1, x)] = likely_pos
        sent_len = len(sentence) - 1
        max = float(0)
        for POS in self.parts_dict.keys():  #here's where we calculate the last word
            if temp_dict[(POS, sent_len)] > max:
                max = temp_dict[(POS, sent_len)]
                likely_pos = POS
        print_out.append(likely_pos)
        sent_len = len(sentence)

        for i in range(sent_len-1):
            POS = pos_sentence[(likely_pos, sent_len-i-1)]
            likely_pos = POS
            print_out.append(POS)

        print_out.reverse()
        return [ [print_out], [] ]

