import toml
import rlp
import enum
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
    def list(self, w='*'):
        NotFound = True
        for k in self.linkionary.keys():
            if len(self.linkionary[k]['links']) == 0:
                NotFound = False
                print(k)
        if NotFound:
            print("Every word is linked.")
# Operation types
class CMD(enum.Enum):
    Quit = 1
    Wait = 2 
    HELP = 3
    Link = 4
    Search = 5
    ListAlone = 6
    Edit = 7
def decode():
    return
if __name__ == '__main__':
    cmd = CMD.Wait
    L = Linkionary()
    # Load file if it exists
    with open('./dictionary.toml', 'r') as f:
        L.linkionary = toml.load(f)
    # Handle all the operations
    while cmd != CMD.Quit:
        if cmd == CMD.Wait:
            arg = input("choose operation: ")
            if arg == 'link':
                cmd = CMD.Link
            elif arg == 'search':
                cmd = CMD.Search
            elif (arg == 'list alone') | (arg == 'll'):
                cmd = CMD.ListAlone            
            elif arg == 'edit':
                cmd = CMD.Edit
            elif (arg == 'X') | (arg == 'XX'):
                cmd = cmd.Quit
            else:
                print("unknow command")
        elif cmd == CMD.Link:
            arg = input("(link): ").split(', ')
            if arg[0] == 'X':
                cmd = CMD.Wait
                continue
            if arg[0] == 'XX':
                break
            L.link(arg) 
        elif cmd == CMD.Search:
            arg = input("(search): ").split(', ')
            if arg[0] == 'X':
                cmd = cmd.Wait
                continue
            elif arg[0] == 'XX':
                break
            for w in arg:
                if not L.search(w):
                    print('word {} not found'.format(w))
        elif cmd == CMD.ListAlone:
            L.list()
            cmd = CMD.Wait
        elif cmd == CMD.Edit:
            # rm: remove, cm: comment(w.os), e: edit
            arg = input('(edit): ').split(' ')
            if (arg[0] == 'rm') | (arg[0] == 'remove'):
                if len(arg) != 2:
                    print('Bad input')
                elif arg[1] not in L.linkionary:
                    print("{} not in linkionary".format(arg[1]))
                else:
                    L.linkionary.pop(arg[1])
            elif (arg[0] == 'cm') | (arg[0] == 'comment'):
                if len(arg) != 2:
                    print('Bad input')
                elif arg[1] not in L.linkionary:
                    print("{} not in linkionary".format(arg[1]))
                else:
                    cm = input("input comment: ")
                    L.linkionary[arg[1]]['os'] = cm
            elif (arg[0] == 'e') | (arg[0] == 'edit'):
                if len(arg) != 3:
                    print('Bad input')
                elif arg[1] not in L.linkionary:
                    print("{} not in linkionary".format(arg[1]))
                else:
                    L.linkionary.pop(arg[1])
                    L.link(arg[2])
            elif arg[0] == 'X':
                cmd = cmd.Wait
                continue
            elif arg[0] == 'XX':
                break
            else:
                print('Command not found.')

    # Dump file
    f = open('./dictionary.toml', 'w')
    toml.dump(L.linkionary, f)
    f.close()
