from Tkinter import *
import Pmw
import csv
import fyp11
import subprocess
result=open('res.txt','w+')
''''lis=[]
lis=ip.get_fun_names()'''
class Window(Frame):       
        def __init__(self):
                Frame.__init__(self)
                self.master.title(" PROGRAMMING ASSIGNMENT GRADER ")
       
                self.grid()
                self.benchmark=''
                self.ipfile=''
                self.lis=[]
                self.misty=[]
                #self.selectbackgroundcolor("blue")
                self.projlabel=Label(self,text="PROGRAMMING ASSIGNMENT GRADER",font=('verdana', 18, 'bold', 'italic')).grid(row=1,column=20)
                self.csvfile=Label(self, text="Benchmark File").grid(row=10, column=0)
                self.bar=Entry(self).grid(row=10, column=1)

                self.csvfile1=Label(self, text="Input File").grid(row=15, column=0)
                self.bar1=Entry(self).grid(row=15, column=1)
                 

                #Buttons  
                #y=7
                
                #y+=1
                
                self.bbutton1= Button(self, text="Browse", command=self.browsecsv)
                self.bbutton1.grid(row=10, column=3)
                self.bbutton2= Button(self, text="Browse", command=self.browsecsv1)
                self.bbutton2.grid(row=15, column=3)
                
                

             #self.jump(self.benchmark,self.ipfile,self.lis)
        '''def getvar(self,lis):
                
                
                #benchmark='y.c''
                #ipfile='testmod1.c'
                #benchmark=self.bar.get()
                #ipfile=self.bar1.get()
                self.jump(benchmark,ipfile,lis)'''

        def browsecsv(self):
                from tkFileDialog import askopenfilename
                #self.benchmark=StringVar
                Tk().withdraw()
                f = askopenfilename()
                self.benchmark=f
                
                
        def browsecsv1(self):
                from tkFileDialog import askopenfilename
                #ipfile=StringVar
                Tk().withdraw() 
                g = askopenfilename()
                self.ipfile=g
                self.cbutton= Button(self, text="OK", command=self.make)
                self.cbutton.grid(row=20, column=3, sticky = W + E)
                
                #return self.ipfile
        def make(self):
                self.jump(self.benchmark,self.ipfile,self.lis,self.misty)
        
                
        def jump(self,benchmark,ipfile,lis,misty):
                marks=0
                max_mrks=0
                #ip.get_input()
                lis=get_fun_names(benchmark)
                print lis
                for i in lis:
                        if i=='':
                                lis.pop(lis.index(i))
                misty=get_fun_names(benchmark)
                for i in misty:
                        if i=='':
                                misty.pop(misty.index(i))
                
                for i in lis:
                        if i!='':
                                max_mrks+=5
                max_mrks+=10 
                create_benchmark(benchmark)
                g=main1(benchmark,ipfile,misty)

                st1 = Pmw.ScrolledText(self, borderframe=1, labelpos=N,
                label_text='Ready Reckoner', usehullsize=1,
                hull_width=400, hull_height=450,
                text_padx=10, text_pady=10,
                text_wrap='none')
                st1.importfile('rr.txt')
                st1.grid(row=50,column=20)   
                if(g==30):
                        rw=20
                        print "Sucessful execution. %d/%d!" % (max_mrks,max_mrks)
                        labx=Label(text="Maximum Marks=").grid(row=rw,column=0)
                        entrx=Entry(relief=RIDGE,width=5)
                        entrx.grid(row=rw+1,column=0)
                        entrx.insert(END,max_mrks)
                        rw=22
                        cw=3
                        cw1=8
                        labx1=Label(text="Marks obtained=").grid(row=rw+2,column=0)
                        entrx1=Entry(relief=RIDGE,width=5)
                        entrx1.grid(row=rw+3,column=0)
                        entrx1.insert(END,max_mrks)
                else:
                        #print g
                        marks=main(benchmark,ipfile,lis)
                        #print marks
                        print "Mistake in program"
                        rw=20
                        labx=Label(text="Maximum Marks=").grid(row=rw,column=0)
                        entrx=Entry(relief=RIDGE,width=5)
                        entrx.grid(row=rw+1,column=0)
                        entrx.insert(END,max_mrks)
                        
                        print('Marks obtained= %d/30' % marks)
                        rw=22
                        cw=3
                        cw1=8
                        labx1=Label(text="Marks obtained=").grid(row=rw+2,column=0)
                        entrx1=Entry(relief=RIDGE,width=5)
                        entrx1.grid(row=rw+3,column=0)
                        entrx1.insert(END,marks)
                        st = Pmw.ScrolledText(self, borderframe=1, labelpos=N,
                        label_text='Summary', usehullsize=1,
                        hull_width=400, hull_height=450,
                        text_padx=10, text_pady=10,
                        text_wrap='none')
                        st.importfile('res1.txt')
                        st.grid(row=50,column=15)

                
                
                
                
                

                
                
def get_fun_names(benchmark):
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
        
                return store
def create_benchmark(benchmark):
                datatype="[void|int|double|float|char| ]+"
                space="\s+"
                funname='[a-zA-Z0-9\(\)]*'
                ob="\("
                cb="\)"
                text="(.*)"
                memo=''
        
                funpro=datatype+space+funname+ob+text+cb+';'
                new=open("benchmarkfile.c","w")
                with open(benchmark) as anu:
                        for line in anu:
                                #print line
                                if(re.match(funpro,line) is not None and re.search('scanf',line) is None):
                                        #print line
                                        pass
                                
                                else:
                                        new.write(line)
                                
                return
def main1(benchmark,ipfile,misty):
        
        
                p=open('h.txt',"a")
        
                #print lis
                startp(benchmark,ipfile,misty)
                m=subprocess.call("gcc z.c 2>err.txt",shell=True)
   
                #print v
                if(m==0):
                        subprocess.call("./a.out>h.txt",shell=True)    
                        #p.write("Compilation is successful\n")
                        
                
                        return 30
                else:
                        return 1990
                
def startp(benchmark,ipfile,misty):
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
                with open(ipfile) as f:
                        for line in f:
                                xen=line.split(' ')
                        
                                #print xen 
                        
                        
                        
                                if(re.match(defn,line) is not None and re.match(funname,xen[1]) is not None and xen[1]=='main()\n'  and c==0 ):
                                        index=misty.index(xen[1])
                                        t=misty.pop(index)
                                        #print lis
                                        start=True
                                        count=0
                                        c=1 
                                
                                        clip1(line,r)
                                
                                
                                elif(re.match(defn,line) is not None and count!=0):
                                        r.write(line)
                                        start=False
                                        #count=count+1
                                
                                elif(start==True):
                                
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

                return
def clip1(line,y):
                strt=False
                stack=[]
                fob="{"
                fcb="}"
        
                #first=ip.benchmark
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
                                else:
                                        pass
def main(benchmark,ipfile,lis):
                store=[]
                datatype="[void|int|double|float|char| ]+"
                space="\s+"
                funname='[a-zA-Z0-9\(\)]*'
                ob="\("
                cb="\)"
                text="(.*)"
                funpro=datatype+space+funname+ob+text+cb+';'
        
                ro=[]
        
        
                p=open("x.txt","w")
                sum1=0
                for i in range(len(lis)):
                        y=start1(benchmark,ipfile,lis)
                        #print y
                        u=y.split('(')
                        m=subprocess.call("gcc z.c 2>err.txt",shell=True)
                        fyp11.match(ipfile)
                        if(m==0):
                                sum1=sum1+5
                                p.write("Compilation of %s successful\n"% u[0])
                        else:
                                p.write("Compilation unsucessful for %s\n"% u[0])
                                mark=fyp11.match("z.c")
                                sum1+=mark
                        
                return sum1
def start1(benchmark,ipfile,lis):
		#print lis
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
        
                with open('benchmarkfile.c','r+') as f:
                        for line in f:
                                xen=line.split(' ')
                        
                        
                        
                                if(re.match(defn,line) is not None and re.match(funname,xen[1]) is not None and xen[1] in lis and c==0 ):
                                        index=lis.index(xen[1])
                                        t=lis.pop(index)
                                
                                        #print lis
                                        start=True
                                        count=0
                                        c=1 
                                
                                        clip(line,r,ipfile)
                                
                                
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
                #print t              
                return t
def clip(line,y,ipfile):
                strt=False
                stack=[]
        
                fob="{"
                fcb="}"
        
        
                with open(ipfile) as g:
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
                return

        
def maing():
        Window().mainloop()
'''root = Tk()
window=Window(root)
root.mainloop()'''
maing()

