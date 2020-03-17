from Operation import Operation

class Loop2X(Operation):
    def __init__(self, op):
        self.operation = op
        self.helpMsg = "Looping, X to exit, and ? to get help\n" + self.operation.helpMsg
        self.prefix = "decorator"
    def do(self):
        while(True):
            arg = input(self.operation.prefix).split(', ')
            if arg[0] == 'X':
                break
            elif arg[0] == '?':
                printHelp()
            else:
                self.operation.do(arg)
    def printHelp(self):
        print(self.helpMsg)
