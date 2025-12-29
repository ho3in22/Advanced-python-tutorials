import os
print(os.name)

os.makedirs(r"c:/Users/Hossein/Desktop/newfolder")
print(os.getcwdb())
os.chdir ("c:/Users/Hossein/Desktop")
print(os.getcwdb())
os.rmdir("newfolder")

fr = "text.txt"
file = open(fr, 'r')
text = file.read()
print(text)
os.close(file)

base = os.getcwd()
print(base)
print(os.path.basename(base))
print(os.path.dirname(base))

print(os.path.isdir("c:\\users\\..."))

import sys

print(sys.platform)