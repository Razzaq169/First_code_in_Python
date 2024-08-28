a = input("Enter First number : ")
funct = int(input(f"Select your operation : \n Press 1 to Add\n Press 2 to subtract\n Press 3 to Multiply\n Press 4 to Divide\n"))

if funct in range(1,5):
    b = input("Enter Second number : ")
    if funct == 1:
        c = float(a) + float(b)
        print(a, " + ", b , " = ", c )
    elif funct == 2:
        c = float(a) - float(b)
        print(a, " - ", b , " = ", c )
    elif funct == 3:
        c = float(a) * float(b)
        print(a, " * ", b , " = ", c )
    elif funct == 4:
        c = float(a) / float(b)
        print(a, " / ", b , " = ", c )
    else:
        print("Invalid Operation!...")
else:
    print("Invalid Operation!...")
        