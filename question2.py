no_of_student=int(input("enter the no of students="))
kharacha_of_student=int(input("enter the kharacha of students="))
budget=no_of_student*kharacha_of_student
if(budget<=50000):
    print("budget me hai")
else:
    print("budget ke bahar hai")