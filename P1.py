

def division(ch_line= 1,file_name="testfle.txt"):
    # number of lines
    p = str(file_name)
    seg = ch_line
    num_line = 0
    for x in open(p, encoding="utf8"):
        num_line += 1

    #print(num_line)

    # segmentation
    # number of chunks
    chunks = num_line // seg
    ext = num_line % seg
    if ext != 0:
        chunks += 1
    

    # division
    fil = open('testfle.txt')
    filread = fil.readlines()

    holder = {}
    # h = []

    chunk = 0
    for i in range(chunks):

        holder.update({chunk: filread[i * seg:(i + 1) * seg]})
        chunk = chunk + 1


    return holder

def jse():
    division()


def main():
    jse()


if __name__ == "__main__":
    main()
