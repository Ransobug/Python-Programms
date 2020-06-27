x = int (input("Enter First Number: "))
y = int (input("Enter Second Number: "))
z = int (input("Enter Third Number: "))
print ("The Greatest among Three is: ",end="")
if y<=x>=z:
    print(x)
elif x<=y>=z:
    print(y)
else:
    print(z)