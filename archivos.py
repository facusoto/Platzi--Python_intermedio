def read():
    lst = []
    with open("./archivos/numbers.txt", "r", newline="", encoding="utf-8") as f:
        lst = [line.strip() for line in f]
    print(lst)


def write():
    names = ["Facundo","Facundo","Facundo","Facundo","Facúndo"]
    with open("./archivos/names.txt", "a", newline="", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()
    write()


if __name__ == '__main__':
    run()
    