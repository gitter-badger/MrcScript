import json, sys, importlib
import modules.builtin as builtin

VERSION = "1.0"
ERRORS = { #Still working on error system
    "UNKNOWN": "Something went wrong!",
    "BAD_IMPORT": "You are attemping to importing a module that does not exist",
    "NO_PROGRAM": "Please include a program!"
}
MODULES = {}
GLOBALS = {}
VARIABLES = {}

if len(sys.argv) == 1:
   print("MrcScript v" + VERSION )
   print()
   print("MrcScript.py (script file).mrcscript")
   print("\t     (script file).json")
else:
    f = open(sys.argv[1], "r")
    fc = f.read()
    f.close()

    j = json.loads(fc)

    if 'imports' in j:
        for i in j['imports']:
            try:
                MODULES[i] = importlib.import_module("modules." + i)
            except ImportError:
                print(ERRORS['BAD_ERROR'])
                sys.exit(1)

    if 'globals' in j:
        for g in j['globals']:
            GLOBALS[g[0]] = g[1]

    if not 'program' in j:
        print(ERRORS["NO_PROGRAM"])
        sys.exit(1)
    for c in j['program']:
        if isinstance(c[0], str):
            continue
        if len(c[0]) == 1:
            args = c[1:]
            varlist = eval("builtin." + c[0][0] + "(args, VARIABLES, GLOBALS)")
            VARIABLES = varlist
        else:
            args = c[1:]
            varlist = eval("MODULES[c[0][0]]." + c[0][1] + "(args, VARIABLES, GLOBALS)")
            VARIABLES = varlist
