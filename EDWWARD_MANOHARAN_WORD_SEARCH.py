import random
import numpy as np

vocabulary_file = 'word_embeddings.txt'

# Read words
print('Read words...')
with open(vocabulary_file, 'r', encoding="utf8") as f:
    words = [x.rstrip().split(' ')[0] for x in f.readlines()]

# Read word vectors
print('Read word vectors...')
with open(vocabulary_file, 'r', encoding="utf8") as f:
    vectors = {}
    for x in f:
        vals = x.rstrip().split(' ')

        vectors[vals[0]] = [float(x) for x in vals[1:]]

vocab_size = len(words)
vocab = {w: idx for idx, w in enumerate(words)}
# sample vocab={'the':0,',':1}->word to index
ivocab = {idx: w for idx, w in enumerate(words)}
# sample ivocab={0:'the,1:','}->index to word

# Vocabulary and inverse vocabulary (dict objects)
print('Vocabulary size')
print(len(vocab))
print(vocab['man'])
print(len(ivocab))
print(ivocab[10])

# W contains vectors for
print('Vocabulary word vectors')
vector_dim = len(vectors[ivocab[0]])
W = np.zeros((vocab_size, vector_dim))
for word, v in vectors.items():
    if word == '<unk>':
        continue
    W[vocab[word], :] = v
print(W.shape)


# find 3 nearest neighbor
def closestWord(input_term):
    inputVector = vectors[input_term]
    minimalEqlideanValue = {}
    i = 0
    for singlevector in vectors:
        tempDict = {}
        if len(minimalEqlideanValue) > 0:
            minimalEqlideanValue = dict(sorted(minimalEqlideanValue.items()))
        eqDistance = np.sqrt(np.sum(np.square(np.array(inputVector) - np.array(vectors[singlevector]))))
        if (len(minimalEqlideanValue) < 3):
            tempDict = {eqDistance: i}
            minimalEqlideanValue.update(tempDict)
        else:
            largestDistance = list(minimalEqlideanValue.keys())[2]
            if eqDistance < largestDistance:
                del minimalEqlideanValue[largestDistance]
                minimalEqlideanValue[eqDistance] = i
        i += 1
    print(minimalEqlideanValue)
    print(ivocab[list(minimalEqlideanValue.values())[0] ])
    relevantWordsIndex = list(minimalEqlideanValue.values())
    #relevantwords = {ivocab[i] for i in relevantWordsIndex}
    distance = list(minimalEqlideanValue.keys())
    return (relevantWordsIndex, distance)


# Main loop for analogy
while True:
    input_term = input("\nEnter a word (EXIT to break): ")
    if input_term == 'EXIT':
        break
    else:
        relevantWordsIndex, distance = closestWord(input_term)
        print("\n                               Word       Distance\n")
        print("---------------------------------------------------------\n")
        for i in range(0,3):
            print("%35s\t\t%f\n" % (ivocab[list(relevantWordsIndex)[i]],list(distance)[i]))


