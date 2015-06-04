'''from gui2 import process_file
benchmark=gui2.process_file(gui2.filename1)
ipfile=gui2.process_file(gui2.filename1)'''
benchmark=raw_input()
ipfile=raw_input()
#from gui2 import benchmark
import re
def get_fun_names():
    store=['main()\n']
    datatype="[void|int|double|float|char| ]+"
    space="\s+"
    funname='[a-zA-Z0-9\(\)]*'
    ob="\("
    cb="\)"
    text="(.*)"
    memo=''
    
    funpro=datatype+space+funname+ob+text+cb+';'
    with open(benchmark) as anu:
        for line in anu:
            #print line
            if(re.match(funpro,line) is not None and re.search('scanf',line) is None):
                #print line
                ro=line.split(' ')
                store.append(ro[1])
                continue
            else:
                pass
    #print 'store'
    #print store
    return store

    
#ip()
