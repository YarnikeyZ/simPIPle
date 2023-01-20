from subprocess import getoutput as gout
from sys import argv
from datetime import datetime

com = "pip"
freeze = gout(f"{com} freeze")
argv.pop(0)
skips = argv
for pkg in freeze.split("\n"):
    pkgTimeStart = datetime.now()
    pkgName = pkg.split('==')[0]
    if not pkgName in argv:
        print(f"\033[38;5;6m### Updating: {pkgName}\033[38;5;15m")
        print(gout(f"{com} install -U {pkgName}"))
    else:
        print(f"\033[38;5;9m###  Skiping: {pkgName}\033[38;5;15m")
    pkgTimeEnd = datetime.now()
    print(f"\033[38;5;5m### Time spend: {pkgTimeEnd-pkgTimeStart}")
