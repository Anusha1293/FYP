import re
def fundef(line):
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    h=[]
    
    eq='='
    numvalue='[0-9.]+'
    charvalue='[A-Za-z0-9]*'
    dq='\"'
    fl='[ A-Za-z]'
    sl='[A-Za-z0-9 ]*'
    rettype='[int float double char void]'
    datatype='[int float double char]'
    space='\s+'
    varname=fl+sl
    funname=fl+sl
    comma=','
    brackets='(\[(0-9)*\])+'
    nl='(\n)+'
    arrname=varname+brackets
    #parameter='(datatype+space+varname)+'
    #parameters='(datatype+space+varname+comma)*'
    #print parameter
    default1=datatype+space+varname+eq+charvalue
    default2=datatype+space+varname+eq+numvalue
    
    #funpro1=rettype+funname+'\('+parameters+parameter+'\)'
    #if(re.search(funpro1,line) is not None):
        
    #h=line.split(';')
    if(re.match(nl,line) is not None):
        pass
    else:
        a=line.split('(')
        if(len(a)>1):
        
            b=a[1].split(')')
        else:
            return 4
        if ',' in b[0]:
            c=b[0].split(',')
        #print c
        for i in c:
            if(re.search(datatype+space+varname,i)is not None or re.search(datatype,i)is not None or re.search(datatype+space+arrname,i)is not None ):
                d.append(i)
            elif(re.search(default1,i) is not None or re.match(default2,i) is not None):
                d.append(i)
            else:
                d.append(0)
            #print d
        if(0 not in d):
        
            for i in range(len(d)):
                po=[]
                #print d[i]
                po=d[i].split(' ')
                #print po
                if(len(po)>=2):
                    e.append(po[1])
                else:
                    return -1
        
            return 4
    
        else:
            return -1
    #else:
        #return "Not a Valid function Prototype"
    
'''def inp():
    f=raw_input()
    res=[]
    res=fundef(f)
    print res'''

#inp()
        
    
    
