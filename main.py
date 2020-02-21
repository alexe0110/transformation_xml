START = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="URN:CREATE_BP_AND_BO_DRKK">\n<soapenv:Header/>\n<soapenv:Body>\n'
FINAL = '</soapenv:Body>\n</soapenv:Envelope>\n'


def drop_each(string, num):
    return string.replace(string[num], ' ')


def drop_dash(file='file.xml'):
    with open(file, 'r', encoding="UTF-8") as f:
        a = f.read()
        for i in range(len(a)):
            if a[i] == '-':
                a = drop_each(a, i)
                print("del")
    print(a)
    with open('file.xml', 'w', encoding="UTF-8") as f:
        f.write(a)


def to_soapui(file='file.xml'):
    with open(file, 'r', encoding="UTF-8") as f:
        a = f.readlines()[3:]
        b = START
        for i in a:
            b = b + i
        b = b + FINAL
    with open(file, 'w', encoding="UTF-8") as f:
        f.write(b)


to_soapui()
