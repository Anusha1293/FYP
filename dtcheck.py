import re
def dtcheck(line):
    valid_var=[]
    p=[]
    q=[]
    r=[]
    s=[]
    
    fl='[ A-Za-z]'
    sl='[A-Za-z0-9 ]*'
    datatype='[int float double char]'
    varname=fl+sl
    
    brackets='(\[[0-9]+\])+'
    arrname=varname+brackets
    if 'int' in line:
        p=line.split('int')
    elif 'float' in line:
        p=line.split('float')
    elif 'double' in line:
        p=line.split('double')
    elif 'char' in line:
        p=line.split('char')
        
    
    #print p
    if(len(p)>1):
        q=p[1].split(',')
    else:
        return 1
    #print q
    for i in range(len(q)-1):
        t=[]
        if(re.search('=',q[i]) is not None): 
           t=q[i].split('=')
           valid_var.append(t[0])
        else:
           valid_var.append(q[i])
           
           
        
        #valid_var.append(q[i])
    r=q[-1].split(';')
    #print r
    if(re.search('=',r[0]) is not None):
       s=r[0].split('=')
       valid_var.append(s[0])
    else:
        valid_var.append(r[0])
    #print valid_var
    
    #print r
    if(re.search(';',line) is None):
       return -2
     
    else:
        pass
    for i in range(len(q)-1):
        if(re.match(varname,q[i]) is not None or re.match(arrname,q[i]) is not None):
            #print "yes"
            pass
        else:
            return 'error! Invalid variable name'
            
    if(re.match(varname,r[0]) is not None or re.match(arrname,r[0]) is not None):
       #print "yay"
        pass
    else:
       return -2
       
    return 1
            

    
'''def inp():
    t=raw_input()
    f=0
    f=dtcheck(t)
    print f
    
    
inp()'''
