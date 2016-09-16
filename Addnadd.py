import sys,os,subprocess,io
sys.path.insert(0,"\\")
try:
    import currnumberstore
except(ImportError):
    print("Failed!")
    with io.FileIO("currnumberstore.py","w"):
        pass
    with open ("currnumberstore.py","a") as f: f.write("currnumber = 0\nnextstep = 0")
import currnumberstore
currnumber = currnumberstore.currnumber
nextstep = currnumberstore.nextstep
gone = 0
while True:
    while gone != 1000:
        currnumber = currnumber + nextstep
        nextstep = nextstep +1
        gone = gone + 1
        print (currnumber)
    if gone == 1000 or gone >1000:
        import os
        os.remove("currnumberstore.py")
        with io.FileIO("currnumberstore.py","w"):
            pass
        with open ("currnumberstore.py","a") as f: f.write("currnumber = ")
        with open ("currnumberstore.py","a") as f: f.write(str(currnumber))
        with open ("currnumberstore.py","a") as f: f.write("\nnextstep = ")
        with open ("currnumberstore.py","a") as f: f.write(str(nextstep))
        gone = 0
    
    
