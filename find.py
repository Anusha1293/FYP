import subprocess
import fyp11
import re
import ip
#import det_fun_name
#lis=det_fun_name.det_fun_name()
lis=[]
lis=ip.get_fun_names()
hew='benchmarkfile.c'
new=open(hew,"w")
#lis=store
#lis=['add(int','read(int','display(int','main()\n']
#t="x"
def clip(line,y):
    strt=False
    stack=[]
    
    fob="{"
    fcb="}"
    
    
    with open(ip.ipfile) as g:
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
                
                
            
                
                
                
def start1():
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
    t=''
    
    with open(hew) as f:
        for line in f:
            xen=line.split(' ')
            
            #print xen 
            '''if re.match(hf,line) is not None and d==0:
                r.write(line)
                d=1'''
            
            
            if(re.match(defn,line) is not None and re.match(funname,xen[1]) is not None and xen[1] in lis and c==0 ):
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
                
    return t            
    
        
def main():
    store=[]
    datatype="[void|int|double|float|char| ]+"
    space="\s+"
    funname='[a-zA-Z0-9\(\)]*'
    ob="\("
    cb="\)"
    text="(.*)"
    funpro=datatype+space+funname+ob+text+cb+';'
    
    ro=[]
    '''with open(ip.benchmark) as anu:
        for line in anu:
            #print line
            if(re.match(funpro,line) is not None and re.search('scanf',line) is None):
                #print line
                ro=line.split(' ')
                store.append(ro[1])
                continue
            if(line=="int main()\n" or line=='void main()\n' or line=='main()\n'):
                store.append(line)
                new.write(line)
            else:
                new.write(line)
                pass
    #print 'store'
    lis=store'''
    
    '''name=1
    f=str(name)'''
    p=open("x.txt","w")
    sum1=0
    for i in range(len(lis)):
        y=start1()
        #print y
        u=y.split('(')
        m=subprocess.call("gcc z.c 2>err.txt",shell=True)
        if(m==0):
            sum1=sum1+5
            p.write("Compilation of %s successful\n"% u[0])
        else:
            p.write("Compilation unsucessful for %s\n"% u[0])
            mark=fyp11.match()
            sum1+=mark
            
    return sum1
    
            
    #p.close()       
        
       
main()
