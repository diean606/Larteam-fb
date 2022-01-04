import sys,shutil

runtah=["diean_gans/__pycache__","modul/__pycache__","wibu/__pycache__","diean_gans/ngewe/__pycache__"]

if sys.version[0]!="3":
	exit(" ! harap gunakan python3")

from diean_gans import awokawokawok
try: [shutil.rmtree(x) for x in runtah]
except: pass
awokawokawok()