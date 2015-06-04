import re
'''def acc():
    t=raw_input()
    
    c=printfcheck(t)
    print c'''


def printfcheck(line):
    specifiers=['%d','%s','%f','%c','%ld']
    count=0
    x=0
    d=[]
    f=[]
    g=[]
    h=[]
    d=line.split('(')
    f=d[1].split(')')
    #print f
    g=f[0].split('"')
    print g
    if(len(g)>1):
        h=g[2].split(',')

        
    
    else:
        return 9
    #print h
    if(len(h)!=0):
        count=len(h)-1
    if(re.search('%d',g[1])):
        cnt=g[1].count("%d")
        x+=cnt
    if(re.search('%f',g[1])):
        cnt=g[1].count("%f")
        x+=cnt
    if(re.search('%ld',g[1])):
        cnt=g[1].count("%ld")
        x+=cnt
    if(re.search('%s',g[1])):

        cnt=g[1].count("%s")
        x+=cnt
    if(re.search('%c',g[1])):
        cnt=g[1].count("%c")
        x+=cnt
        
    

    if(x==count):
        return 9
    else:
        return 0
        
    

#acc()
