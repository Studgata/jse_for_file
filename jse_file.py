import socket
s = socket.socket()
host = ""
port = 1001
addr = (host,port)
s.bind(addr)


def division():
    # number of lines
    seg = 10
    num_line = 0
    for x in open("testfle.txt"):
        num_line += 1

    print(num_line)

    # segmentation
    # number of chunks
    chunks = num_line // seg
    ext = num_line % seg
    if ext != 0:
        chunks += 1
    # division
    print(chunks)


    holder = {}
    lst = []


    e = -1
    chk = 0
    count = 1

    fil = open('testfle.txt')
    filread = fil.readlines()
    d = 0


    for x in range(0,11):
        lst.append(filread)

        print(lst)
            
            
    



























"""
    while (count < (chunks + 1)):
        for line in filread:
            e = len(lst)

            if (e != seg):
                lst.append(line)
            else:
                chk = chk + seg
                count = count + 1
                e = -1
                break
            holder.update({count: lst})
            
            lst = []
    return holder
        
"""



def jse():
    fle = division()
        
    #for key, value in fle.items() :
     #   print (key, value)
    print(fle)    
def main():
    jse()





if __name__ == "__main__":
    main()
