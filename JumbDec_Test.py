import random
import Jumbling_Char


def RevJumblingBlock(number,randno):
    del number[-14:]


    if (randno%2==0):
        number = ''.join(reversed(number))
      
    else:
        number = ''.join(number)
      

    num = len(number)-randno

    numlist=list(number)
    fix=len(numlist)
    #print('Length of array: ',fix)

    numlen=1
    #print (numlen)
    i=randno-1
    while(numlen<=randno):
        j=0
        j=(fix%numlen)
        #print ("Swapping positions ",i,",",j)
        numlist[i],numlist[j]=numlist[j],numlist[i]
        numlen=numlen+1
        i=i-1
        #print(numlist)
    cv=''.join(numlist)
  
    
    x=''
    for i in range(0,num):
        x=x+numlist[i]
   
    

    return x


    
