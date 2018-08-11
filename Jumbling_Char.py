import random
import time
length=random.randrange(10,100)


def JumblingBlock(number,length):
    cset = list(map(chr, range(97, 10000)))
    # print('Random length:',length)

    rlength=length
    for i in range(0,length):
        x=random.randrange(0,len(cset))
        number=number+cset[x]
   # print ('Appended String: ',number)
    numlist=list(number)
    fix=len(numlist)
    # print('Length of array: ',fix)
    i=0
    # print (rlength)
    while(rlength!=0):
        j=0
        j=(fix%rlength)
        #print ("Swapping positions ",i,",",j)
        numlist[i], numlist[j]=numlist[j] , numlist[i]
        rlength=rlength-1
        i=i+1
        #print(numlist)
    JumbledString=''.join(numlist)
    print('Jumbled String: ',JumbledString)
    print('\n')
    if (length%2==0):
        JumbledString=''.join(reversed(JumbledString))
        print('Reversed String ',JumbledString)
    else:
        pass
    if JumbledString is None:
        return ''
    return str(JumbledString)    
