numOne = (int(input("What is your first number?")))
numTwo = (int(input("What is your second number?")))
modNum = numOne % numTwo

if modNum == 0:
    print("Even")
else:
    print("Odd")

print(modNum)

