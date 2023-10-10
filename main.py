def menu():
    print("A.isplay the value of the factorial of N.")
    print("B.Display the value of the sine of X.")
    print("C.Display the value of the cosine of X.")
    print("M.Display the menu of options.")
    print("Q.Exit from the program.")

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(f"The number {num}\'s factorial is:{fact}")    

def trig():
    print("Welcome to the TRIG!!")
    menu()
    is_ok=False
    m=['a','b','c','m','q']
    e = 2.718281828459045
    choose=input("Choose one of them:").lower()
    if choose in m:
        is_ok=True
    while is_ok:
        if choose=='a':
            num=int(input("Enter the number to find the factorial:"))
            factorial(num)
        elif choose=='b':
            rad=int(input("Enter the radian to find sine:"))
            deg=57.2958*rad
            sx=(e**(deg*1j)).imag
            print(f"The sine of the {deg} degree is:{sx}")

        elif choose=='c':
            rad=int(input("Enter the radian to find cose:"))
            deg=57.2958*rad
            cx=(e**(deg*1j)).real
            print(f"The sine of the {deg} degree is:{cx}")
        elif choose=='q':
            is_ok=False
            exit()
        else:
            if choose=='m':
                menu()
    
        menu()
        choose=input("Choose one of them:").lower()




trig()


