i=int(input("enter i:"))
j=int(input("enter j:"))
k=int(input("enter k:"))
if i%2==0 and j%2!=0 and k%2!=0:
    print(f"{i} is even")
elif j%2==0 and i%2!=0 and k%2!=0:
    print(f"{j} is even")
elif k%2==0 and i%2!=0 and j%2!=0:
    print(f"{k} is even")
elif i%2==0 and j%2==0 and k%2!=0:
    print(f"{i} and {j} are even")
elif j%2==0 and i%2!=0 and k%2==0:
    print(f"{j} and {k} are even")
elif k%2==0 and i%2==0 and j%2!=0:
    print(f"{k} and {i} are even")
elif k%2==0 and i%2==0 and j%2==0:
    print(f"{k} and {i} and {j} are even")
else:
    print("All are odd")
