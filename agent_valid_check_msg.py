import os

msg = "Agent configuration [ IP ] is wrong."

f = open("tmp", 'r')
while True:
    line = f.readline()
    if line == "":
        print('\033[31m' + '[FAIL]' + '\033[0m', end='')
        print(" NOT working for Invalid parameter")
        break;
    if msg in line:
        print('\033[32m' + '[SUCCESS]' + '\033[0m', end='')
        print(" %s"%line)
        break;
f.close();