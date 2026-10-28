def read_file():
    file = open("char.txt", 'r')

    file.seek(0,0)

    list = []
    # content = file.read()
    # print(content)

    lines = file.readlines()

    for line in lines:
        list.append(line.rstrip('\n'))

    print(list)

    file.close()

def write_file():
    file = open("char.txt", 'w')

    list = ["Hey", "my", "name", "is", "Aadarsha"]

    for lis in list:
        file.write(lis + "\n")

    file.close()

def main():
    write_file()
    read_file()
    return

if __name__ == "__main__":
    main()