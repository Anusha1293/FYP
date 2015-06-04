import re
import whilecheck
import forcheck
import subprocess
import printcheck
import scanfcheck
import fundef
import dtcheck
import ifcheck

def match():
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
	
	hf='#include'+l+text+r
	dbs='\/\/'
	comment=dbs+text
	
	
	with open("y.c") as f:
		for line in f:
			if(re.search('for',line) is not None):
				print line
				ans=forcheck.forcheck(line)
				#print ans
				if(ans==3):
					print "correct for statement"
			
				else:
					print "wrong. syntax error in for"
					if(marks!=0):
					    marks=marks-1
					


                        elif(re.match(dec,line) is not None):
				print line
				res3=dtcheck.dtcheck(line)
				if res3==-2:
					print"error in declararion"
					if marks!=0:
                                            marks-=0.25

                                        else:
                                            pass
				else:
					print "valid declaration"

			

			elif(re.search(text+'='+text,line)is not None):
				print line
				print "assignment statement"
			 

                        elif(re.search(comment,line) is not None):
				print line
				print "comment line"
				
		   
				
			
			elif(re.search(pfpat,line)is not None):
			   ans1=printcheck.printfcheck(line)
			   print line
			   if ans1==9:
				   print 'correct printf'
			   else:
					print"error in printf"
					if(marks!=0):
						marks-=0.25
						
			elif(re.search(sfpat,line)is not None):
			   ans2=scanfcheck.scanfcheck(line)
			   print line
			   if ans2==9:
				   print 'correct scanf'
			   else:
					print"error in scanf"
					if(marks!=0):
						marks-=0.25
						
			
			   
			
			elif(re.search('while',line) is not None):
				print line
				res=whilecheck.whilecheck(line)
				if(res==14):
					print "correct while condition"
				else:
					print "wrong. Error in syntax of while"
					if(marks!=0):
						marks-=1
			elif(re.search('if',line) is not None):
				print line
				res1=ifcheck.ifcheck(line)
				if(res1==14):
					print "correct if condition"
				else:
					print "wrong. Error in syntax of if"
					if(marks!=0):
						marks-=1
			elif(re.search(funcdef,line)is not None):
				print line
				ans3=fundef.fundef(line)
				
				if(ans3==-1):
					print("mistake in function defination")
				else:
					print 'correct function definition'
				
				
			elif(re.match(funpro,line) is not None):
				print line
				print 'correct'
			
			
			elif(re.match(ofb,line)is not None):
				lisblst.append('{')
				print line
				print 'correct'
			elif(re.match(cfb,line)is not None):
			   if(lisblst!=[]):
				   print line
				   lisblst.pop()
			   else:
				   print line+ "extra closing brace"
			elif(re.match(hf,line)is not None):
				print line
				print 'header file'
				continue

			elif(re.match(nl,line)is not None):
				continue

			else:
				print line
				print 'ok'
				  
	
	
	'''m=subprocess.call("gcc y.c",shell=True)
	if(m==0):
		print("This is Output")
		subprocess.call("./a.out", shell=True)'''
	#print marks
	return marks
match()
					 
		
