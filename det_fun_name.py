import fundef
#import ip
import re

def det_fun_name():
    st=[]
    rettype='[void int float double]'
    space='\s+'
    text='(.*)'
    ob='('
    cb=')'
    fl='[ A-Za-z]'
    sl='[A-Za-z0-9 ]*'
    varname=fl+sl
    funcdef=rettype+space+varname+ob+text+cb
    with open('y.c') as g:
        for line in g:
            print line
            if(re.match(funcdef,line) is not None):
                ans=fundef.fundef(line)
                if(ans==4):
                    if(line=='void main()\n' or line=='int main()\n'):
                        st.append(line)
                    else:
                        v=line.split('(')
                        st.append(v[0])
            else:
                print 1
    print st
det_fun_name()

    
                
                
    
