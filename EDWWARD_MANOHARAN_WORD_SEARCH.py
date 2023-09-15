import random
import numpy as np

vocabulary_file='word_embeddings.txt'

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

print("sandberger")
print(vectors)
vocab_size = len(words)
vocab = {w: idx for idx, w in enumerate(words)}
#sample vocab={'the':0,',':1}->word to index
ivocab = {idx: w for idx, w in enumerate(words)}
#sample ivocab={0:'the,1:','}->index to word

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
'''
#find 3 nearest neighbor
def closestWord(input_term):
    inputVector=vectors[input_term]
    closestIndex=0
    minimalEqlideanValue=0
    for singlevector in :
        i=0
        eqDistance=np.sqrt(np.sum(np.square(inputVector - singlevector)))
        if(closestIndex=0):
            minimalEqlideanValue=eqDistance
        
        else:
            if eqDistance<minimalEqlideanValue:
                minimalEqlideanValue=eqDistance
                closestIndex=i
            
        i+=1
    return ivocab[closestIndex]
# Doing squareroot and
# printing Euclidean distance
print(np.sqrt(sum_sq))

print("hiiiiiiiiiiiiiiiii")
print(vectors[1])
# Main loop for analogy
while True:
    input_term = input("\nEnter three words (EXIT to break): ")
    if input_term == 'EXIT':
        break
    else:
        print(closestWord(input_term))
     
        a = [random.randint(0, vocab_size), random.randint(0, vocab_size),
             random.randint(0, vocab_size)]
         
        print("\n                               Word       Distance\n")
        print("---------------------------------------------------------\n")
        for x in a:
            print("%35s\t\t%f\n" % (ivocab[x], 666))
            
        '''
            