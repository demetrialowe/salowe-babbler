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
    wordmap = {}
    startlist = get_start_states(filename, ngramsize)
    wordlist = makeWordList(filename)
    #for every state in that list, put those into the dictionary
    #for now I'm putting that each start state has a list as its value
    for start in startlist:
        if start not in wordmap:
            wordmap[start] = []
        teststring = ''
        for i in range(ngramsize):
            teststring = teststring + ' ' + wordlist[i]
            if teststring == start:  # won't work but maybe right idea?
                nextword = wordlist[i + ngramsize + 1]
                wordmap[start].append(nextword)
    #
    # wordmap = {}
    # startlist = ['this is', 'is a', 'a sentence']
    # wordlist = ['This', 'is', 'not', 'a', 'sentence', 'this', 'is', 'a', 'sentence', 'this', 'is', 'a', 'dog']
    # ngramsize = 2
    # count = 0
    # for start in startlist:
    #    if start not in wordmap:
    #        wordmap[start] = []
    #    if count <= len(wordlist) - ngramsize - 1:
    #         for word in wordlist:
    #             teststring = ''
    #                 for i in range(count, count + ngramsize):
    #                     teststring = teststring + ' ' + wordlist[i]
    #                     print(teststring)
    #                 count = count + 1
    #         print count

    #print(wordmap)
    #tested in console, basically works. Order is weird but don't think that should affect

    #from here I want to take each start state and get the next word in the file, and append that word to the list
    #maybe go back to wordlist of the file, find the first instance of each startstate, slice the next word?





    '''Use the text contained in the file with given filename to create a map
    of ngrams of the given ngram size. Then return the list of all words that
    could follow the given state. For example, for test_cases/test1.txt, with
    ngram size of 2 and the state "this is", we should return the list:
    ['an', 'great', 'great'] (or something like this in a different order).
    '''

    # TODO: return all the words that could follow the given state
    return ['dog', 'cat', 'dog', 'bird']


def babble(filename, ngramsize, numsentences):
    '''Generate the given number of sentences using the given ngram size.
    Create a dictionary where keys are each n-1 words, and the values
    are the words that can follow in a list. Randomly pick a word, generate
    a new key, and continue until you reach a stop token (such as . or !)
    '''

    # TODO: return sentences from the file
    return ['sentence one', 'sentence two']


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
    ngram = 3
    numsentences = 2

    # possible_words = get_possible_words(filename, ngram, 'this is')
    # assert ('an' in possible_words)
    # assert (possible_words.count('great') == 2)

    start_states = get_start_states(filename, ngram)
    print(start_states)
    # assert ('This is' in start_states)
    # TODO: you should check other possible start states

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
