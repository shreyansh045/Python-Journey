from pathlib import Path
import os

def readFileAndFolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readFileAndFolder()
        name=input("Plese tell your file name:")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data=input("What do you wnt to write : ")
                fs.write(data)

            print(f"file created successfully")
        else:
            print("This file already exists")
    except Exception as err:
        print(f"an error occured as {err}")

def readfile():
    try:
        readFileAndFolder()
        name=input("please tell your file name:")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data=fs.read()
                print(data)
            print("Data readed successfully")
        else:
            print("File not exist")
    except Exception as err:
        print(f"an error occured as{err}")

def updatefile():
    try:
        readFileAndFolder()
        name=input("Plese tell your file:")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for renaming the file")
            print("Press 2 for overwriting the file")
            print("press 3 for appending the file")
            res=int(input("Give your response:"))
            if res==1:
                name2=input('give me the new name:')
                p2=Path(name2)
                p.rename(p2)

            if res==2:
                with open(p,"w") as fs:
                    data=input("What do you want to overwrite:")
                    fs.write(data)
            if res==3:
                with open(p,"a") as fs:
                    data=input("What do you want to append:")
                    fs.write(" "+data)
           
    except Exception as err:
        print("An error occured as {err}")

def deletefile():
    try:
        readFileAndFolder()
        name=input("Please tell file which file you want to delete:")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File removed successfully")
        else:
            print("No such file exist")
    except Exception as err:
        print("An error occured as {err}")

print("Press 1 for creating the file")
print("Press 2 for reading the file")
print("Press 3 for updating the file")
print("Press 4 for deleting the file")

check = int(input("Plese type your response:"))
if check==1:
    createfile()

elif check==2:
    readfile()

elif check==3:
    updatefile()

elif check==4:
    deletefile()