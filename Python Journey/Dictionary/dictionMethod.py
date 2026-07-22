# d={1:12,2:13,3:22}
# d.clear()
# print(d.items())

# Merge two dictionary
"""
a={"name":"Shreyansh","age":23,10:21}
b={10:33,20:23,30:34}
for i in b:
    a[i]=b[i]
print(a)   """

# sum of all values
"""
b={10:100,20:200,30:300}
sum=0
for i in b:
    sum=sum+b[i]
print(sum) """

# Count the frequency of each element in list 
"""
a=[1,1,1,2,2,3,3,4,5]
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)
"""

#combining two dictionaries by adding common values
a={10:100,20:200,30:300}
b={30:400,40:500,50:600}
for i in b:
    if i in a.keys():
        a[i]+=b[i]
    else:
        a[i]=b[i]
print(a) 