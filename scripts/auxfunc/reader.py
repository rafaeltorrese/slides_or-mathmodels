import csv
import re

with open("example03-33.txt", "r") as f:
    text = [line.strip() for line in f]


def get_coefficients(expression):
    pass

string = "2.2x1   - x2 - 6.45x3 + 10x4"
string = "".join(string.split())
print(string)

pattern1 = "([+-]?\s*\d*\.?\d*)\s*[a-zA-Z]\d*"
pattern2 = "(\d*\.?\d*)[a-z]"



regex1 = re.compile(pattern1)
regex2 = re.compile(pattern2)

print(regex2.findall(string))

# new_string = regex2.sub("1", string)
# print("New String: ", new_string)

signs = regex1.findall(string)

print(signs)

# elements = ["1" if e == '' else e for e in signs]
# print(elements)

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




