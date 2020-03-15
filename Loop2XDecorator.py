from Operation import Operation

class Loop2XDecorator(Operation):
    def __init__(self, op):
        self.operation = op
        self.helpMsg = op.helpMsg
        self.prefix = "decorator"
    def do(self):
        while(True):
            arg = input(self.operation.prefix).split(', ')
            if arg[0] == 'X':
                break
            elif arg[0] == '?':
                self.operation.printHelp()
            else:
                self.operation.do(arg)
