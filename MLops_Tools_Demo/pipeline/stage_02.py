import os

with open("artifact/text.txt", "r") as f:
   s = f.read()
   print(s)


with open("artifact/output.txt", "w") as f:
   f.write("Welcome guys")
   