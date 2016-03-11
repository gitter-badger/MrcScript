def log(args, varlist, globallist):
    if isinstance(args[0], str):
        print(args[0])
    elif isinstance(args[0], list):
        if args[0][0] == "var":
            print(varlist[args[0][1]])
        elif args[0][0] == "global":
            print(globallist[args[0][1]])
        else:
            print(str(args[0]))
    else:
        print(str(args[0]))
    return varlist

def read(args, varlist, globallist):
    if len(args) == 1:
        varlist[args[0]] = input()
    else:
        varlist[args[1]] = input(args[0])
    return varlist

def var(args, varlist, globallist):
    varlist[args[0]] = args[1]
    return varlist
