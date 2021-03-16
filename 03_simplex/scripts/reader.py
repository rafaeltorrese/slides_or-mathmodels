import csv
import re

with open("example03-33.txt", "r") as f:
    text = [line.strip() for line in f]



string = "x1 + 2x2 - 3x3"
regex = re.compile("\d[+-]?x")
print(regex.findall(string))

# pattern = "[<>]="
# line4 = text[3]
# print(line4)
# regex = re.compile(pattern)
# match = regex.search(line4)
# print(match)
# ineqsymbol = match.group()
# print('Symbol: ', ineqsymbol)
# print(match.start())
# print(match.end())
# print(match.span())

# all_matches = regex.findall(line4)
# print(all_matches)






