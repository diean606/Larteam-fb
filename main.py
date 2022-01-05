import sys,shutil

runtah=["larteam-fb"]

if sys.version[0]!="3":
	exit(" ! harap gunakan python3")

from "larteam-fb"
try: [shutil.rmtree(x) for x in runtah]
except: pass
awokawokawok()