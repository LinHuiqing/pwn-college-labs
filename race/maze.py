# create maze

import os
import sys
import shutil

pwd = os.getcwd()
sys.setrecursionlimit(100000)
#ENV=[]

def maze(n):
    s = str(n)+"/"
    for i in range(400):
        s += "0/"
    try:
        shutil.rmtree(str(n))
        os.remove(str(n)+"_end")
    except:
        pass

    os.makedirs(s, exist_ok=True)
    os.symlink(pwd, s+"root")
    os.symlink(s, str(n)+"_end")
    #ENV.append("export P{}={}".format(str(n), s[:-1]))

def create_maze(n):
    path = ""
    for i in range(n):        
        maze(i)
        path += "{}_end/root/".format(i)
    path +="tmp/test"
    os.makedirs("tmp")
    open("tmp/test", 'a').close()
    print(path)

create_maze(10)

