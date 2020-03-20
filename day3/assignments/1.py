import re

pattern = r'\+\d{1,3}-\d{5,10}'

with open('genius club.txt') as file:
    lines = file.readlines()
    for line in lines:
        matches = re.findall(pattern, line)
        for match in matches:
            print(match)