import sys
import random


def makeWordList(filename):
    wordlist = []
    for line in open(filename):
        line = line.rstrip()
        for word in line.split(' '):
            wordlist.append(word)
    return wordlist


def listtostring(list):
    string = ' '.join(list)
    return string


def get_start_states(filename, ngramsize):
    wordlist = []
    start_states = []
    wordlist = makeWordList(filename)
    fake_start_states = []
    while len(wordlist) >= ngramsize:
        fake_start_states.append(wordlist[0:ngramsize])
        del wordlist[0]
    for state in fake_start_states:
        start_states.append(listtostring(state))
    return start_states


def get_possible_words(filename, ngramsize, state):
    possible_words = {}
    startlist = get_start_states(filename, ngramsize)
    wordlist = makeWordList(filename)
    for start in startlist:
        if start in possible_words:
            continue
        if start not in possible_words:
            possible_words[start] = []
        for i in range(len(wordlist) - ngramsize):
            word = wordlist[i]
            teststring = word
            for x in range(i + 1, i + ngramsize):
                teststring = teststring + ' ' + wordlist[x]
                nextword = wordlist[x + 1]
                if teststring == start:
                    possible_words[start].append(nextword)
    return possible_words[state]


def babble(filename, ngramsize, numsentences):
    sentences = []
    for x in range(numsentences):
        firstword = random.choice(get_start_states(filename,ngramsize))
        nextsteps = get_possible_words(filename, ngramsize, firstword)
        nextword = random.choice(nextsteps)
        sentence = firstword + ' ' + nextword
        choice = nextword
        nextword = sentence[sentence.index(' ') + 1:]
        while choice != '.' and choice != '!':
            nextsteps = get_possible_words(filename, ngramsize, nextword) #nextsteps gets the list in my dictionary at key nextword
            choice = random.choice(nextsteps) #i choose a random next word and put it in choice
            sentence = sentence + ' ' + choice #i add that to my sentence
            nextword = nextword + ' ' + choice #i take my key, and concatenate the word I just chose
            nextword = nextword[nextword.index(' ') + 1:] #I take that whole n+1 string and slice off the first word to pass that as my next key
        sentences.append(sentence)
    return sentences

'''Generate the given number of sentences using the given ngram size.
Create a dictionary where keys are each n-1 words, and the values
are the words that can follow in a list. Randomly pick a word, generate
a new key, and continue until you reach a stop token (such as . or !)
'''


# TODO: return sentences from the file



def main():
    filename = 'test_cases/test1.txt'
    ngram = 3
    numsentences = 2
    if len(sys.argv) > 3:
        filename = sys.argv[1]
        ngram = int(sys.argv[2])
        numsentence = int(sys.argv[3])
    print('generate {} sentences from file {} using ngram size {}'.format(
        numsentences, filename, ngram))

    sentences = babble(filename, ngram, numsentences)
    for sentence in sentences:
        print(sentence)


def test1():
    filename = 'test_cases/test1.txt'
    ngram = 2
    numsentences = 2

    possible_words = get_possible_words(filename, ngram, 'this is')
    assert ('an' in possible_words)
    assert (possible_words.count('great') == 2)

    start_states = get_start_states(filename, ngram)
    print(start_states)
    assert ('This is' in start_states)
    assert ('sentence !' in start_states)
    assert ('sentence is' in start_states)

    # setting a seed for the random number generator means that the sequence
    # of pseudo-random numbers is the same for each run of the code.
    random.seed(0)
    # TODO make sure the sentences you generate make sense
    sentences = babble(filename, ngram, numsentences)
    for sentence in sentences:
        print(sentence)


if __name__ == '__main__':
    test1()
    # main()
