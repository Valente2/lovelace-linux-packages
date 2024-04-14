import os
from zipfile import ZipFile
class math():
    def add():
        numa=input("enter number 1 ")
        numb=input("enter number 2 ")
        ans=int(numa)+int(numb)
        print(numa,"+",numb,"=",ans)
    def sub():
        numa=input("enter number 1 ")
        numb=input("enter number 2 ")
        ans=int(numa)-int(numb)
        print(numa,"-",numb,"=",ans)
    def mult():
        numa=input("enter number 1 ")
        numb=input("enter number 2 ")
        ans=int(numa)*int(numb)
        print(numa,"x",numb,"=",ans)
    def divi():
        numa=input("enter number 1 ")
        numb=input("enter number 2 ")
        ans=int(numa)/int(numb)
        print(numa,"/",numb,"=",ans)
class file():
    def mkdir(name):
        os.system("mkdir ",name)
    def unzip():
        path=input("enter zip path ")
        ZipFile.extractall(path)
~
