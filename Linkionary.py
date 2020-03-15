import toml
import enum
from UsageFactory import UsageFactory
# use toml for readabiliity
class CMD(enum.Enum):
    Quit = 1
    Wait = 2
    HELP = 3
    Link = 4
    Search = 5
    ListAlone = 6
    Edit = 7
if __name__ == '__main__':
    arg = input("choose Usage: (Voc)abulary linking, (Mean)ing Linking: ")
    if arg == 'Voc' or arg == '0':
        Usage = UsageFactory().createVoc()
    elif arg == 'Mean' or arg == '1':
        Usage = UsageFactory().createMean()
    else:
        print("Unknown requirement")
    print('init Factory')
    cmd = CMD.Wait
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
            elif (arg == '?') | (arg == 'help'):
                print(helpMsg)
            else:
                print("unknow command")
        elif cmd == CMD.Link:
            Usage.link.do()
            cmd = CMD.Wait
        elif cmd == CMD.Search:
            Usage.search.do()
            cmd = CMD.Wait
        # elif cmd == CMD.ListAlone:
        #     L.list()
        #     cmd = CMD.Wait
        # elif cmd == CMD.Edit:
        #     # rm: remove, cm: comment(w.os), e: edit
        #     arg = input('(edit): ').split(' ')
        #     if (arg[0] == 'rm') | (arg[0] == 'remove'):
        #         if len(arg) != 2:
        #             print('Bad input')
        #         elif arg[1] not in L.linkionary:
        #             print("{} not in linkionary".format(arg[1]))
        #         else:
        #             L.linkionary.pop(arg[1])
        #     elif (arg[0] == 'cm') | (arg[0] == 'comment'):
        #         if len(arg) != 2:
        #             print('Bad input')
        #         elif arg[1] not in L.linkionary:
        #             print("{} not in linkionary".format(arg[1]))
        #         else:
        #             cm = input("input comment: ")
        #             L.linkionary[arg[1]]['os'] = cm
        #     elif (arg[0] == 'e') | (arg[0] == 'edit'):
        #         if len(arg) != 3:
        #             print('Bad input')
        #         elif arg[1] not in L.linkionary:
        #             print("{} not in linkionary".format(arg[1]))
        #         else:
        #             L.linkionary.pop(arg[1])
        #             L.link(arg[2])
        #     elif arg[0] == 'X':
        #         cmd = cmd.Wait
        #         continue
        #     elif arg[0] == 'XX':
        #         break
        #     else:
        #         print('Command not found.')
