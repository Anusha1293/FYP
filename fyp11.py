import re
import whilecheck
import forcheck
import subprocess
import printcheck
import scanfcheck
import fundef
import dtcheck
import ifcheck
#result=open('res.txt','w')
def match(ipfile):
        
	marks=5
	pr='printf'
	ob='('
	text='(.*)'
	cb=')'
	sc=';'
	datatype='[int float double char]'
	pfpat=pr+ob+text+cb+sc
	sf='scanf'
	space='\s+'
	sfpat=sf+ob+text+cb+sc
	dec=datatype+text+sc
	rettype='[void int float double]'
	ofb='{'
	cfb='}'
	nl='\n*'
	lisblst=[]
	funpro=rettype+ob+text+nl+cb+sc
	funcdef=rettype+space+text+ob+text+cb
	l='<'
	r='>'
	result=open("res1.txt","w")
	hf='#include'+l+text+r
	dbs='\/\/'
	comment=dbs+text
	
	
	with open(ipfile) as f:
		for line in f:
			if(re.search('for',line) is not None):
				#result.write (line)
				#result.write("\n")
				ans=forcheck.forcheck(line)
				#result.write ans
				if(ans==3):
					#result.write( "correct for statement")
					#result.write("\n")
                                        pass
			
				else:
                                        result.write (line)
                                        result.write("\n")
					result.write( "wrong. syntax error in for")
					result.write("\n")
					if(marks!=0):
						marks-=1

			

			elif(re.search(text+'='+text,line)is not None):
                                pass
				#result.write (line)
				#result.write("\n")
				#result.write("assignment statement")
				#result.write("\n")
			 

                        elif(re.match(comment,line) is not None):
				#result.write (line)
				#result.write("\n")
				#result.write ("comment line")
				#result.write("\n")
				pass
				
		   
				
			
			elif(re.search(pfpat,line)is not None):
			   ans1=printcheck.printfcheck(line)
			   #result.write (line)
			   #result.write("\n")
			   if ans1==9:
				   #result.write ('correct printf')
				   #result.write("\n")
                                   pass
			   else:
                                        result.write (line)
                                        result.write("\n")
					result.write("error in printf")
					result.write("\n")
					if(marks!=0):
						marks-=0.25
			elif(re.search('scanf',line)is not None):
			   ans2=scanfcheck.scanfcheck(line)
			   #result.write (line)
			   #result.write("\n")
			   if ans2==9:
				   #result.write ('correct scanf')
				   #result.write("\n")
                                   pass
			   else:
                                        result.write (line)
                                        result.write("\n")
					result.write("error in scanf")
					result.write("\n")
					if(marks!=0):
						marks-=0.25
						
			elif(re.search(dec,line) is not None):
				#result.write (line)
				#result.write("\n")
				res3=dtcheck.dtcheck(line)
				if res3==-2:
                                        result.write (line)
                                        result.write("\n")
					result.write("error in declararion")
					result.write("\n")
					if(marks!=0):
						marks-=0.5
					
				else:
					#result.write ("valid declaration")
					#result.write("\n")
                                        pass
						
			
			   
			
			   
			
			elif(re.search('while',line) is not None):
				#result.write (line)
				#result.write("\n")
				res=whilecheck.whilecheck(line)
				if(res==14):
					#result.write ("correct while condition")
					#result.write("\n")
                                        pass
				else:
					result.write ("wrong. Error in syntax of while")
					result.write("\n")
					if(marks!=0):
						marks-=1
                        
			elif(re.search('if',line) is not None):
				#result.write (line)
				#result.write("\n")
				res1=ifcheck.ifcheck(line)
				if(res1==14):
					#result.write ("correct if condition")
					#result.write("\n")
                                        pass
				else:
                                        result.write (line)
                                        result.write("\n")
					result.write ("wrong. Error in syntax of if")
					result.write("\n")
					if(marks!=0):
						marks-=1
			elif(re.search(funcdef,line)is not None):
        
                                #result.write (line)
                                #result.write("\n")
                                ans3=fundef.fundef(line)
				
                                if(ans3==-1):
                                        result.write (line)
                                        result.write("\n")
                                        result.write("mistake in function defination")
                                        result.write("\n")
                                else:
                                        #result.write ('correct function definition')
                                        #result.write("\n")
                                        pass
				
				
			elif(re.match(funpro,line) is not None):
				'''result.write (line)
				result.write("\n")
				result.write ('correct')
				result.write("\n")'''
				pass
			
			
			elif(re.match(ofb,line)is not None):
				lisblst.append('{')
				'''result.write (line)
				result.write("\n")
				result.write ('correct')
				result.write("\n")'''
				pass
			elif(re.match(cfb,line)is not None):
			   if(lisblst!=[]):
				   '''result.write (line)
				   result.write("\n")'''
				   lisblst.pop()
			   else:
                                   #result.write (line)
                                   #result.write("\n")
				   result.write ((line)+ "extra closing brace")
				   result.write("\n")
			elif(re.match(hf,line)is not None):
				'''result.write (line)
				result.write("\n")
				result.write ('header file')
				result.write("\n")'''
				pass
			elif(re.match(nl,line)is not None):
				continue

			

			else:
				'''result.write (line)
				result.write("\n")
				result.write ('ok')
				result.write("\n")'''
				pass
				  
	
	
	'''m=subprocess.call("gcc y.c",shell=True)
	if(m==0):
		result.write("This is Output")
		subprocess.call("./a.out", shell=True)'''
	#result.write marks
	return marks
#match()
					 
		
