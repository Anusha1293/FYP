import ip
import re
import subprocess
def create_benchmark():
    datatype="[void|int|double|float|char| ]+"
    space="\s+"
    funname='[a-zA-Z0-9\(\)]*'
    ob="\("
    cb="\)"
    text="(.*)"
    memo=''
    
    funpro=datatype+space+funname+ob+text+cb+';'
    new=open("benchmarkfile.c","w")
    with open(ip.benchmark) as anu:
        for line in anu:
            #print line
            if(re.match(funpro,line) is not None and re.search('scanf',line) is None):
                #print line
                pass
                
            else:
                new.write(line)
                
    return
