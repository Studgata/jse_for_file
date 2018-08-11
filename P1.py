

def division():
    # number of lines
    seg = 1
    num_line = 0
    for x in open("testfle.txt", encoding="utf8"):
        num_line += 1

    print(num_line)

    # segmentation
    # number of chunks
    chunks = num_line // seg
    ext = num_line % seg
    if ext != 0:
        chunks += 1
    print(chunks)

    # division
    fil = open('testfle.txt')
    filread = fil.readlines()

    holder = {}
    # h = []

    chunk = 0
    for i in range(chunks):

        holder.update({chunk: filread[i * seg:(i + 1) * seg]})
        chunk = chunk + 1
    """
    for j in range(1,ext+1):
        n = j * -1
        ll = filread[n]

        h.append(ll)

        h = list(reversed(h))
    print(h)
    holder.update({chunk:h})

    """

    for x, y in holder.items():
        print(x, y)
    return holder

def jse():
    division()


def main():
    jse()


if __name__ == "__main__":
    main()
