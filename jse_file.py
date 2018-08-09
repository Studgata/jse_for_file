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
    h = []
    k = 0
    p = 0
    chunk = 0
    count = 1
    fil = open('testfle.txt')
    filread = fil.readlines()
    while k < len(filread)-1:
        while p < seg:
            h.append(filread[k])
            k = k +1
            p= p+1
            holder.update({chunk:h})
        h = []
        chunk = chunk +1
        p = 0


    for x,y in holder.items():   
        print(x,y)
    print(len(holder))
            
    



























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
