import bs4


def drop_each(string, num):
    return string.replace(string[num], ' ')


with open('file.xml', encoding="UTF-8") as f:
    a = f.read()
    # print(a)
    for i in range(len(a)):
        # if a[i] == '<':
        #     t = 1
        # if a[i] == '>':
        #     t = 0
        if a[i] == '-':
            a = drop_each(a, i)
            print("del")
    print(a)