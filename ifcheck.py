import re
'''def acc():
    t=raw_input()
    c=[]
    c=whilecheck(t)
    print c'''


def ifcheck(line):
    d=[]
    f=[]
    g=[]
    h=[]
    k=[]
    andcount=0
    orcount=0
    d=line.split('(')
    f=d[1].split(')')
    
    
    #print f
    andcount=f[0].count('&&')
    orcount=f[0].count('||')
    if(andcount==0 and orcount==0 ):
       # for i in f[0]:
        if((re.search('!',f[0]) is not None) or (re.search('<=',f[0]) is not None) or (re.search('>=',f[0]) is not None) or (re.search('<',f[0]) is not None) or (re.search('>',f[0]) is not None) or (re.search('!=',f[0]) is not None) or (re.search('==',f[0]) is not None) or (re.search('True',f[0]) is not None) or (re.search('False',f[0]) is not None) or (re.search('0',f[0]) is not None) or (re.search('1',f[0]) is not None)):
            return 14
        else:
            return -14

        
    elif(andcount>=1 and orcount==0 ):
        g=f[0].split('&&')
        #print g

    elif(orcount>=1 and andcount==0):
        g=f[0].split('||')
       # print g
    
    elif( '||' in line and andcount>=1):
        k=f[0].split('||')
        for i in k :
            if('&&' in i):
               g= i.split('&&')
               g=g+k
              # print g
    flag=len(g)
    
    if ( len(g)!= 0):
        for i in g:
            if((re.search('!',i) is not None) or (re.search('<=',i) is not None) or (re.search('>=',i) is not None) or (re.search('<',i) is not None) or (re.search('>',i) is not None) or (re.search('!=',i) is not None) or (re.search('==',i) is not None) or (re.search('True',i) is not None) or (re.search('False',i) is not None) or (re.search('0',i) is not None) or (re.search('1',i) is not None)):
                #print 'yo'
                flag=flag-1
           

    if flag==0:
        return 14
    else:
        return -14
    



        
