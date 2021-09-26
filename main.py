import sys,shutil
def approval():
	time.sleep(1)

CorrectAip = 'SDJKHANSDJ'
loop = 'true'
while loop == 'true':
    username = input(' Enter Your Aip Key : ')
    if username == CorrectAip:
            print('\x1b[1;92m Logged in successfully')
            loop = 'false'
            
runtah=["saya_gans/__pycache__","modul/__pycache__","wibu/__pycache__","saya_gans/ngewe/__pycache__"]

if sys.version[0]!="3":
	exit(" ! USE THIS > python main.py")

from saya_gans import awokawokawok
try: [shutil.rmtree(x) for x in runtah]
except: pass
awokawokawok()
