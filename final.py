import clips
import find
import create_bench
import ip
def jump():
    marks=0
    #ip.get_input()
    create_bench.create_benchmark()
    g=clips.main1()
    if(g==30):
        print "Sucessful execution. 30/30!"
    else:
        print g
        marks=find.main()
        #print marks
        print "Mistake in program"
        print('Marks obtained= %d/30' % marks)
    
    
jump()
