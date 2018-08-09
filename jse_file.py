import itertools


def division():
    # number of lines
    seg = 100
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
    fil = open('testfle.txt')
    filread = fil.readlines()
    print(chunks)
    holder = {}
    # h = []
    k = 0
    chunk = 0
    for i in range(chunks):
        k = k + 1

        holder.update({chunk: filread[i * 10:(i + 1) * 10]})
        chunk = chunk + 1
    for x, y in holder.items():
        print(x, y)


def jse():
    division()


def main():
    jse()


if __name__ == "__main__":
    main()
