import toml
from Operation import Operation

class LinkVoc(Operation):
    def __init__(self, words):
        self.words = words
        self.helpMsg = "<word1, word2, ...>"
        self.prefix = "link: "
    def _link(self, A, B):
        if (A in self.words[B]['links']) | (A == B):
            return
        # Links directly
        self.words[A]['links'].append(B)
        self.words[B]['links'].append(A)
        # Links all the links from counterpart.
        for w in self.words[A]['links']:
            self._link(w, B)
        for w in self.words[B]['links']:
            self._link(w, A)
    # link all the words in arg
    def do(self, arg):
        print("linking")
        # Build entry for words which don't exist.
        for w in arg:
            if w not in self.words.keys():
                print('building new word: ', w)
                self.words[w] = {'word': w, 'links':[]}
        # Link list of words in pairs
        for i in range(len(arg)):
            for j in range(i + 1, len(arg)):
                self._link(arg[i], arg[j])
        f = open('Vocs.txt', 'w')
        toml.dump(self.words, f)
        f.close()
