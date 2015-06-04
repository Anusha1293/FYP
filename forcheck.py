import re
'''def acc():
    t=raw_input()
    c=[]
    c=forcheck(t)
    print c'''


def forcheck(line):
    flag=0
    d=[]
    f=[]
    g=[]    
    emplis='for\([\s]*;[\s]*;[\s]*\)'
    if(re.match(emplis,line)):
        flag=3
        return flag
    d=line.split('(') 
    g=d[1].split(')')
    f=g[0].split(';')

    if(re.search('=',f[0])  is not None):
        if(f[0].count('=')==1):
            flag=flag+1
            
            
            
    if(re.match('[\s]+',f[0]) is not None):
        flag=flag+1
        
    if(len(f)>1):    
        if(re.search('<=',f[1]) is not None):
            flag=flag+1
    
        if(re.search('>=',f[1]) is not None):
            flag=flag+1
       
        if(re.search('<',f[1]) is not None):
            flag=flag+1
 
        if(re.search('>',f[1]) is not None):
            flag=flag+1
    if(len(f)>2):

        if(re.search('\+=',f[2]) is not None):
            flag=flag+1
   
        if(re.search('-=',f[2]) is not None):
            flag=flag+1
    
        if(re.search('\*=',f[2]) is not None):
            flag=flag+1
    
        if(re.search('\/=',f[2]) is not None):
            flag=flag+1
    
        if(re.search('\+\+',f[2]) is not None):
            flag=flag+1
   
        if(re.search('--',f[2]) is not None):
            flag=flag+1

    return flag
#acc()
