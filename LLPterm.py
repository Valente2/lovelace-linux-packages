from zipfile import ZipFile
import os
print("lovelace linux terminal\n[c]2024 GPL 3.0 Licence")
name=input("enter name ")
host=input("enter hostname ")
run=True
while run==True:
    print(name,"@",host," LLPT")
    cmd=input("$ ")
    if cmd=="unzip":
        path = input("enter path of zip ")
        ZipFile.extractall(path)
