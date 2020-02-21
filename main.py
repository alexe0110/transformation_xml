import bs4


def drop_each(string, num):
    return string.replace(string[num], ' ')


with open('file.xml', 'r', encoding="UTF-8") as f:
    a = f.read()
    for i in range(len(a)):
        if a[i] == '-':
            a = drop_each(a, i)
            print("del")

print(a)
with open('file.xml', 'w', encoding="UTF-8") as f:
    f.write(a)
