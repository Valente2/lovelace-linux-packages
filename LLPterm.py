import os
print("lovelace linux terminal\n[c]2024 GPL 3.0 Licence")
name=input("enter name ")
host=input("enter hostname ")
run=True
while run==True:
    print(name,"@",host," LLPT")
    cmd=input("$ ")
    if cmd=="bash" or  "Batch":
        run2=True
        while run2==True:
            cmd=input("# ")
            os.system(cmd)
    if cmd=="package":
        pass