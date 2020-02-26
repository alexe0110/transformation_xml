import sys
import time

START = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="URN:CREATE_BP_AND_BO_DRKK">\n<soapenv:Header/>\n<soapenv:Body>\n'
FINAL = '\n</soapenv:Body>\n</soapenv:Envelope>\n'

try:
    file = sys.argv[1]
    print("Выбран " + file)
except IndexError:
    file = 'file.xml'
    print("По умолчанию file.xml")


def drop_each(string, num):
    return string.replace(string[num], ' ')


def drop_dash(file):
    with open(file, 'r', encoding="UTF-8") as f:
        a = f.read()
        for i in range(len(a)):
            if a[i] == '-' and a[i - 1] == '\n':
                a = drop_each(a, i)
    with open(file, 'w', encoding="UTF-8") as f:
        f.write(a)
    print("Черточки удалены")


def to_soapui(file):
    with open(file, 'r', encoding="UTF-8") as f:
        a = f.readlines()[3:]
        b = START
        for i in a:
            b = b + i
        b = b + FINAL
    with open(file, 'w', encoding="UTF-8") as f:
        f.write(b)

    print("Формат сделан для SOAP UI")


drop_dash(file)
to_soapui(file)
time.sleep(5)
