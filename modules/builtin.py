def log(args, varlist, globallist):
    print(args[0])
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

def end(args, varlist, globallist):
    raise SystemExit

def add(args, varlist, globallist):
    varlist[args[0]] = int(args[1]) + int(args[2])
    return varlist

def take(args, varlist, globallist):
    varlist[args[0]] = int(args[1]) - int(args[2])
    return varlist
