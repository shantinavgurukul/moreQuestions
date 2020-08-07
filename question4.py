num1=int(input("enter the num1="))
num2=int(input("enter the num2="))
num3=int(input("enter the num3="))
if num1>num2 and num1>num3:
    print(num1,"this big")
elif(num2>num1 and num2>num3):
    print(num2,"this is big")
elif(num3>num1 and num3>num2):
    print(num3,"this is big")
else:
    print("all things equal and different")