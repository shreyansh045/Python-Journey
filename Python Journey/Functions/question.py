def pallindrome(st):
    rev=""
    for i in range(len(st)-1,-1,-1):
        rev=rev+st[i]
    if rev==st:
        print(f"{st} String is pallindrome")
    else:
        print(f"{st} String is not pallindrome")
pallindrome("NAMAN")
pallindrome("Prashant")