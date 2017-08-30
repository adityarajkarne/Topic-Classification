# Topic-Classification


Classified the genre/topic of a document in an academic corpus consisting of 20 different topics with 83% accuracy and generated a list of top 10 distinctive words for every topic.

Logic: Consider sentences as Markov Chains. The set of possible states is the set of words in the English language. There’s an initial distribution P (W 1 ), the probability of each word occurring at the
beginning of a sentence. Then there’s P (W i+1 |W i ), the probability that a word follows a given other word.
