
import random
import time
import Jumbling_Char
import JumbDec_Test
from P1 import division
import timeit
ency_total_time = 0


file = division()


encrypted_file = {}
decrypted_file = {}

start_time = timeit.default_timer()
#encryption
for key,chunk in file.items():

    for line in chunk:
        
        rl = Jumbling_Char.length
        Jumbledline = Jumbling_Char.JumblingBlock(line,rl)

        '''Salting'''
        CurrDate = str(time.strftime('%Y%m%d'))
        CurrTime = str(time.strftime('%H%M%S'))
        SaltedLINE = Jumbledline + CurrDate+CurrTime



        SLINE = SaltedLINE

        encrypted_file.update({key:SLINE})
        
        line_time = timeit.default_timer()-start_time
        ency_total_time = ency_total_time + line_time


for x,y in encrypted_file.items():
    print(x,y)
    print("\n")


print("Total time for encryption", ency_total_time)

total_dec = 0



#decryption
startdec = timeit.default_timer()
decryted_file = {}
for key,chunk in encrypted_file.items():
        
       
        DSL=list(SLINE)

        u=JumbDec_Test.RevJumblingBlock(DSL,rl)
        dec_time  = timeit.default_timer()-startdec
        
        total_dec = total_dec + dec_time

        
        decrypted_file.update({key:u})

for x,y in decrypted_file.items():
    print(x ,":", y)
    print('\n')    

print("Total time for decryption: ", total_dec)
