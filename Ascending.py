l=[1,5,3,4,2]
temp=0

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)


# Using a function
l1=[9,7,5,6,8]
l1.sort()
print(l1)
