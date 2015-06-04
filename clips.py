import subprocess
import re
import ip
#lis=['add(int','read(int','display(int','main()\n']
#t=" "

lis=[]
lis=ip.get_fun_names()
def clip(line,y):
    strt=False
    stack=[]
    fob="{"
    fcb="}"
    
    first=ip.benchmark
    #print first
    with open("benchmarkfile.c") as g:
        for line1 in g:
            
            if(line1==line):
                strt=True
                y.write(line1)
                #print stack
                
            elif strt is True:
                if(re.match(fob,line1) is not None):
                    stack.append("{")
                    #print stack
                    
                    y.write(line1)
                    
                elif(re.match(fcb,line1) is not None and strt is True):
                    o=stack.pop()
                    #print stack
                    y.write(line1)           
                    if stack==[]:
                        strt=False
                        #print "anu"
                        return
                        
                else:
                    y.write(line1)
                
                
            
                
                
                
def startp():
    
    stk=[]
    fob='{'
    fcb='}'
    datatype="[void|int|double|float|char| ]+"
    space="\s+"
    r='>'
    l='<'
    funname='[a-zA-Z0-9\(\)]*'
    ob="\("
    cb="\)"
    text="(.*)"
    fundef=datatype+space+funname+ob+text+cb
    defn=fundef
    funpro=datatype+space+funname+ob+text+cb+';'
    #print fundef
    br=[]
    hf='#include'+l+text+r
    #strt=False
    r=open("z.c","w")
    stack=[]
    start=False
    count=0
    c=0
    d=0
    
    #print ip.ipfile
    with open(ip.ipfile) as f:
        for line in f:
            xen=line.split(' ')
            
            #print xen 
            '''if re.match(hf,line) is not None and d==0:
                r.write(line)
                d=1'''
            
            
            if(re.match(defn,line) is not None and re.match(funname,xen[1]) is not None and xen[1]=='main()\n'  and c==0 ):
                index=lis.index(xen[1])
                t=lis.pop(index)
                #print lis
                start=True
                count=0
                c=1 
                
                clip(line,r)
                
                
            elif(re.match(defn,line) is not None and count!=0):
                r.write(line)
                start=False
                #count=count+1
                
            elif(start==True):
                #r.write(line)
                #yo=True
                if(re.match(fob,line) is not None):
                    stk.append('{')
                    #print stk
                    
                elif(re.match(fcb,line) is not None): 
                    v=stk.pop()
                    #print v
                    if(stk==[]):
                        start=False
                else:
                    pass
                    
                               
                    
                
                
            elif(start==False):
                r.write(line)    
                
                
    
        
def main1():
    
    '''name=1
    f=str(name)'''
    p=open('h.txt',"a")
    
    #print lis
    startp()
    m=subprocess.call("gcc z.c 2>err.txt",shell=True)
   
    #print v
    if(m==0):
        subprocess.call("./a.out>h.txt",shell=True)    
        #p.write("Compilation is successful\n")
            
        
        return 30
    else:
        return 1990

       

#main1()
