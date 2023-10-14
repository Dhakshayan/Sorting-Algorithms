print("Sort Elements of List by Unit Digits")
l= list(map(int,input("Enter List: ").split()))
l.sort(key= lambda i: (i%10,i))
print(*l)