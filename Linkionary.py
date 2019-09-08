import toml
import rlp
'''
class WordMeta:
    def __init__(self, word, trans = '', os = ''):
        self['word'] = word
        self['links'] = []
        self['trans'] = trans
        self['os'] = os
    def show(self):
        print(self['word'], self['trans'], self['os'])
'''
class Linkionary:
    def __init__(self):
        self.linkionary = {}
        print('init linkionary')
    def _link(self, A, B):
        if (A in self.linkionary[B]['links']) | (A == B):
            return
        # Links directly
        self.linkionary[A]['links'].append(B)
        self.linkionary[B]['links'].append(A)
        # Links all the links from counterpart.
        for w in self.linkionary[A]['links']:
            self._link(w, B)
        for w in self.linkionary[B]['links']:
            self._link(w, A)
    def link(self, arg):
        # Build entry for words which don't exist.
        for w in arg:
            if w not in self.linkionary.keys():
                print('building new word: ', w)
                self.linkionary[w] = {'word': w, 'links':[]}
        # Link list of words in pairs
        for i in range(len(arg)):
            for j in range(i + 1, len(arg)):
                self._link(arg[i], arg[j])
    def search(self, w):
        print('searching: ', w)
        if w in self.linkionary.keys():
            for ww in self.linkionary[w]['links']:
                print(self.linkionary[ww])
            return True
        else:
            return False


def decode():
    return
if __name__ == '__main__':
    #input
    arg = input().split(', ')
    L = Linkionary()
    L.link(arg)
    L.search(arg[1])
    #dump file
    f = open('./dictionary.toml', 'w')
    toml.dump(L.linkionary, f)
    f.close()
