
# MLPT - Math Learning Python Toolkit
# This program provides several mathematical tools:
# - Mini calculator
# - Prime decomposition
# - Factorial calculation
# - GCD and LCM calculation
# - Geometry calculations
# Author: Josaphat

import time


# Mini calculator that allows the user to perform
# addition, subtraction, multiplication and division
def Mini_calculator():
        def addition(a, b):
            return a + b

        def substraction(a, b):
            return a - b

        def multiplication(a, b):
         return a * b

        def division(a, b):
            if b != 0:
                return a / b
            else:
                return "Error : division by zero"

        def menu():
            print("\n=== CALCULATOR ===")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Quitter")

        while True:
            menu()
            choix = input("Choose a number (1-5) : ")

            if choix == '5':
                print("Goodbye!")
                return False


            if choix in ['1', '2', '3', '4']:
                try:
                    nbr1 = float(input("Insert your first number : "))
                    nbr2 = float(input("Insert your second number  : "))
                except ValueError:
                    print("Please enter a valid number (a number between 1 to 5)")
                    continue

            if choix == '1':
                print("Result :", addition(nbr1,nbr2))
            elif choix == '2':
                print("Result :", substraction(nbr1,nbr2))
            elif choix == '3':
                print("Result :", multiplication(nbr1,nbr2))
            elif choix == '4':
                print("Result :", division(nbr1,nbr2))
            else:
                print("Invalid option.Please enter a valid number (a number between 1 to 5).")

# Function that decomposes a number into its prime factors
def Prime_decomposition():
    resp="1"
    while resp=="1":
        a=int(input("\nInsert your choice: "))
        original_number=a
        liste=""
        i=2
        while a>1:
            if a%i==0:
                liste+=str(i)+","
                a=a/i
            else:
                i+=1
        print()
        print(f"{original_number}={liste}")
        print("""\n
        1-continue 
        Other -sortir\n""")
        resp=input("Insert your choice: ")

# Function that calculates the factorial of a number
def Factorial():
    resp="1"
    while resp=="1":
        print()
        factorielle=int(input("Insert your choice: "))
        port=1
        affichage=""
        if factorielle>0:
            for i in range (factorielle,0,-1):
                port=port*i
                if i==1:
                    affichage=affichage+str(i)
                else:      
                    affichage+=str(i)+"*"
            print()
            print(f"{factorielle}!={affichage}={port}") 
        elif factorielle==0:
         print("\n0!=1") 
        else:
            print("\nWe can't calculate the factorial of negative number")
        print("""\n
            1-continue
            Other-sortir\n""")
        resp=input("Insert your choice: ")

# Function that calculates the GCD and LCM of two numbers
# using the Euclidean algorithm
def GCD_LCM():
    resp="1"
    while resp=="1":
        print()
        a=int(input("Insert your first number: "))
        print()
        b=int(input("Insert your second number: "))
        r=a%b
        p=a*b
        while r!=0:
            a=b
            b=r
            r=a%b
        pp=p//b
        print(f"\nThe PGCD is {b}")
        print(f"The PPCM is {pp}")
        print("""\n
            1-continue 
            Other-sortir\n""")
        resp=input("Insert your choice: ")

# Geometry calculator that computes area, perimeter
# or volume for several geometric shapes
def Geometry():
    while True:
        print("""
                 1-Carré
                 2-Rectangle
                 3-Triangle
                 4-Cercle
                 5-Parallélogramme
                 6-Losange
                 7-Trapèze
                 8-Ellipse
                 9-Cube
                 10-Parallélépipède
                 11-Sphère
                 12-Cylindre
                 13-Cône
                 14-SORTIR 
              """)
        userchoice=input("Insert your choice: ")
        while userchoice not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]:
            print("Option invalide")
            userchoice=input("Insert your choice: ")
        else:
            match userchoice:
                case "1":
                    coté=int(input("the quarter's measure: "))
                    peri=coté*4
                    aire=coté*coté
                    print("")
                    print(f"The perimeter measures {peri} and the area worths {aire}")
                case "2":
                    long=int(input("the length's measure: "))
                    larg=int(input("the width's measure: "))
                    peri=(long+larg)*2
                    aire=long*larg
                    print("")
                    print(f"The perimeter measures {peri} and the area worths {aire}")
                case "3":
                    firtcoté=int(input("the first quarter's measure: "))
                    secondcôté=int(input("the second quarter's measure: "))
                    thirdcoté=int(input("the third quarter's measure: "))
                    heightcoté=int(input("the hight's measure: "))
                    base=int(input("the base's measure(first quarter or second quarter ou third quarter): "))
                    peri=firtcoté+secondcôté+thirdcoté
                    aire=(base * heightcoté) / 2
                    print("")
                    print(f"The perimeter measures {peri} and the area worths {aire}")
                case "4":
                    rayon=int(input("the radius's measure: "))
                    aire=3.14*(rayon*rayon)
                    peri=2*3.14*rayon
                    print("")
                    print(f"The perimeter measures {peri} and the area worths {aire}")
                case "5":
                    coté1=int(input("the first quarter's measure: "))
                    coté2=int(input("the second quarter's measure: "))
                    base=int(input("the base's measure(first quarter or second quarter): "))
                    heightcoté=int(input("the hight's measure: "))
                    aire=base*heightcoté
                    peri=(coté1+coté2)*2
                    print("")
                    print(f"The perimeter measures {peri} and the area worths {aire}")
                case "6":
                    diago1=int(input("the first diagonal's measure: "))
                    diago2=int(input("the second diagonal's measure: "))
                    coté=int(input("the quarter's mesure: "))
                    peri=coté*4
                    aire=(diago1*diago2)/2
                    print("")
                    print(f"The perimeter measures {peri} and the area worths {aire}")
                case "7":
                    base1=int(input("the first base's measure: "))
                    base2=int(input("the second base's measure: "))
                    heightcoté=int(input("the hight's measure: "))
                    coté1=int(input("the first quarter's measure: "))
                    coté2=int(input("the second quarter's measure: "))
                    coté3=int(input("the third quarter's measure: "))
                    coté4=int(input("the four quarter's measure: "))
                    aire=((base1+base2)*heightcoté)/2
                    peri=(coté1+coté2+coté3+coté4)
                    print("")
                    print(f"The perimeter measures {peri} and the area worths {aire}")
                case "8":
                    axe1=int(input("the big half's measure: "))
                    axe2=int(input("the little half's measure: "))
                    aire=axe1*axe2*3.14
                    peri = 3.14 * (3*(axe1+axe2) - ((3*axe1+axe2)*(axe1+3*axe2))**0.5)
                    print("")
                    print(f"The perimeter measures {peri} and the area worths {aire}") 
                case "9":
                    arrete=int(input("the arete's measure: "))
                    volume=arrete*arrete*arrete
                    aire=arrete*arrete*6
                    print("")
                    print(f"The volume worths {volume} and the area worths {aire}") 
                case "10":    
                    long=int(input("the length's measure: "))
                    larg=int(input("the width's measure: "))
                    heightcoté=int(input("the hight's measure: "))
                    volume=long*larg*heightcoté
                    aire=2*((long*larg)+(long*heightcoté)+(larg*heightcoté))
                    print("")
                    print(f"The volume worths {volume} and the area worths {aire}") 
                case "11":
                    rayon=int(input("the radius's measure: "))
                    aire=3.14*4*(rayon*rayon)
                    volume=(4/3)*3.14*(rayon*rayon*rayon)
                    print("")
                    print(f"The volume worths {volume} and the area worths {aire}")  
                case "12":
                    rayon=int(input("the radius's measure: "))
                    heightcoté=int(input("the hight's measure: "))
                    aire=3.14*heightcoté*(rayon*rayon)
                    volume=volume = 3.14 * rayon * rayon * heightcoté
                    print("")
                    print(f"The volume worths {volume} and the area worths {aire}") 
                case "13":
                    rayon=int(input("the radius's measure: "))
                    heightcoté=int(input("the hight's measure: "))
                    Generatrice=int(input("the power reactor's measure: "))
                    aire=3.14*rayon*(rayon+Generatrice)
                    volume=(1/3)*3.14*heightcoté*(rayon*rayon)
                    print("")
                    print(f"The volume worths {volume} and the area worths {aire}") 
                case _:
                    break

# Display the main menu of the program
def menu():
        print("""
    *****MENU*****

    1 - Mini calculator
    2 - Prime decomposition
    3 - Factorial
    4 - GCD and LCM
    5 - Geometry
    6 - Exit
    """)
        

# Main program loop
# Allows the user to select different mathematical tools
print()
print("Welcome to this MLPT")
print()
menu()
print()
user_choice=input("Insert your choice: ")
while True:
    if user_choice not in ["1","2","3","4","5","6"]:
        print()
        print("Invalid option.Please enter a valid number (a number between 1 to 5).")
        print()
        menu()
        print()
        user_choice=input("Insert your choice: ")
    elif user_choice=="1":
        Mini_calculator()
        print()
        menu()
        print()
        user_choice=input("Insert your choice: ")
    elif user_choice=="2":
        Prime_decomposition()
        print()
        menu()
        print()
        user_choice=input("Insert your choice: ")
    elif user_choice=="3":
        Factorial()
        print()
        menu()
        print()
        user_choice=input("Insert your choice: ")
    elif user_choice=="4":
        GCD_LCM()
        print()
        menu()
        print()
        user_choice=input("Insert your choice: ")
    elif user_choice=="5":
        Geometry()
        print()
        menu()
        print()
        user_choice=input("Insert your choice: ")
    else:
        print()
        print(f"Program ends in 5 seconds\n")
        for x in range(5,-1,-1):
                time.sleep(1)
                print(f"{x}\r",end=" ",flush=False)
                time.sleep(0.5)              
        break