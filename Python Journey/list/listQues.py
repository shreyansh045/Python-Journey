# print all positive and negative elements
"""
a=[20,34,-21,20,-31,-89,89]
print("All positive elements")
for i in a:
    if i>=0:
        print(i)
print("All negative elements")
for i in a:
    if i<0:
        print(i)"""

# print the mean of list
"""
a=[1,2,3,4,5,6,7,8]
sum=0
n=len(a)
for i in a:
    sum=sum+i
print(sum/n)  """

# Print the largest elemnt in list

"""
a=[23,43,21,19,9,88,43]
largest=a[0]
index=0
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
        index=i
print(f"The largest no. is {largest} at index {index}") """

# Print largest and second largest
"""
a=[21,11,31,45,34,65]
largest=a[0]
second_largest=a[0]
for i in a:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest:
        second_largest=i
print(largest,second_largest) 
"""

# check the list is sorted or not
a=[11,13,15,54,34,65]
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        continue
    else:
        print("List is not sorted")
        break
else:
    print("List is sorted")
    
    
