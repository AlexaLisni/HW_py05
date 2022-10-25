# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby, starmap
from os import path

def encodeRle(text="text.txt", codeText="CodeText.txt"):
    if path.exists(text) and path.exists(codeText):
        with open(text) as myFile01, \
                open(codeText, "a") as myFile02:
            for i in myFile01:
                myFile02.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("Error")


def decodeRle(name):
    if path.exists(name):
        with open(name) as myFile:
            n = ""
            for k in myFile:
                word = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word)))
    else:
        print("The files do not exist in the system!")
encodeRle(input("Enter the name of the file with the text: "), input("Enter the file name to record: "))
decodeRle(input("Enter the name of the file to decode: "))