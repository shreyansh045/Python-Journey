# a=open(r"Python Journey\FileHandling\basics.py")

# print(a.read())
# r=open("random.txt",'w')
# r.write("Hello this is shreyansh dwivedi")
r=open("random.txt",'a')
r.write("i am appending some content in this")

r.close()