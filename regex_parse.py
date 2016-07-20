import re

f = open(access_log2.txt)

strToSearch = ''

for line in f:
    strToSearch += line

print(strToSearch)

numFinder1 = re.compile('\s\d{3}[400]\s')
findnum1 = re.search(numFinder1, strToSearch)

if (findnum1):
    print(findnum1.group())
else:
    print("found nothing")

numFinder2 = re.compile('\s\d{3}[500]\s')
findnum2 = re.search(numFinder2, strToSearch)

if (findnum2):
    print(findnum2.group())
else:
    print("found nothing")

