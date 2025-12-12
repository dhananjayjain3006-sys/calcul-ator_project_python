# ============================================================
# PROJECT: MULTI-FUNCTION CALCULATOR (ARITHMETIC + TRIG + STATS)
# MADE BY: 
# _____________________
# CLASS: XII (CBSE)
# ============================================================

import math
from datetime import datetime
import statistics

# ============================================================
# ====================== HISTORY FUNCTIONS ===================
# ============================================================

def clear():
    with open("doc.txt","w") as file:
        file.write("")
    print("HISTORY CLEARED") 

def viewhistory_():
    try:
        with open("doc.txt", "r") as file:
            content = file.read()
            if len(content) == 0:
                print("NO HISTORY FOUND")
            else:
                print(content)
    except FileNotFoundError:
        print("NO HISTORY FOUND")

def save(*args):
    with open("doc.txt","a+") as file:
        file.write("\n")
        file.write(str(datetime.now()))
        file.write(" | ")
        for a in args:
            file.write(str(a) + " ")

def show(*args):
    for a in args:
        print(a, end=" ")
    print()
    save(*args)

# ============================================================
# ================= ARITHMETIC INPUT + HELPERS =============
# ============================================================

def get(s):
    while True:
        try:
            return float(input(s))
        except ValueError:
            print("Enter only number!")

# ============================================================
# ================== STATISTICS INPUT FUNCTIONS =============
# ============================================================

def input_list():
    print("How many numbers you want to enter?")
    while True:
        try:
            n = int(input("Enter value: "))
            break
        except ValueError:
            print("Enter only integer!")
    li = []
    for i in range(1, n+1):
        while True:
            try:
                a = float(input(f"Enter number {i}: "))
                li.append(a)
                break
            except ValueError:
                print("Enter only number!")
    return li

def stat(name, func):
    nums = input_list()
    show(name, func(nums))

def mean():
    stat("MEAN IS:", statistics.mean)

def median():
    stat("MEDIAN IS:", statistics.median)

def mode():
    stat("MODE IS:", statistics.mode)

# ============================================================
# ============= TRIGONOMETRIC INPUT + HELPERS ==============
# ============================================================

def ang():
    while True:
        try:
            return float(input("Enter angle in degrees: "))
        except ValueError:
            print("Enter only number!")   

def ang2():
    while True:
        try:
            return float(input("Enter value: "))
        except ValueError:
            print("Enter only number!")

def get_trig():
    print("ENTER VALUE FROM -1 TO 1")
    return get("Enter number: ")

def sq(y, cs):
    if -1>y>1:
        return "INVALID INPUT"
    if cs == "as":
        return math.degrees(math.asin(y))
    if cs == "ac":
        return math.degrees(math.acos(y))

def qw():
  while True:
        try:
            y = float(input("Enter value greater than 1 or less than -1: "))
            if abs(y) >= 1:
                return y
            else:
                print("INVALID INPUT! Must be >1 or <-1")
        except ValueError:
            print("Enter number!")
def trigo(name, func):
    rad = ang()
    value=func(math.radians(rad))
    value=round(value,6)
    show(name, rad, "is:",value )

# ============================================================
# ==================== TRIGONOMETRIC FUNCTIONS ==============
# ============================================================

def sin_():
    trigo("SINE", math.sin)

def cosine_():
    trigo("COS", math.cos)

def tangent_():
    rad = ang()
    value=math.tan(math.radians(rad))
    value=round(value,6)
    if rad == 90:
        print("Tan at 90 degree not defined.")
    else:
        show("TANGENT OF", rad, "is:",value)

def cotangent_():
    rad = ang()
    value=1/math.tan(math.radians(rad))
    value=round(value,6)
    if math.degrees(rad) == 0:
        print("Cotangent not defined")                    
    else:                
        show("COTANGENT OF",rad, "is:",value)

def secant_():
    rad = ang()
    if rad == 90:
        print("Secant at 90 is not defined")
    else:
         value=1/math.cos(math.radians(rad))
         value=round(value,6)
         show("SECANT OF", rad, "is:",value)
 
def cosecant_():
    rad = ang()
    if math.degrees(rad) == 0:
        print("Cosecant at 0 is not defined")
    else:
         value=1/math.sin(math.radians(rad))
         value=round(value,6)
         show("COSECANT OF",rad, "is:", value)

def arcsine_():
    y = get_trig()
    show("ARC SINE OF", y, "is:", sq(y, "as"), "degrees")

def arccosine_():
    y = get_trig()
    show("ARC COSINE OF", y, "is:", sq(y, "ac"), "degrees")

def arctangent_():
    y = get("Enter value: ")
    rad = math.atan(y)
    deg = math.degrees(rad)
    show("ARC TANGENT OF", y, "is:", deg, "degrees")

def arccotangent_():
    print("ENTER VALUE")
    y = ang2()
    if y == 0:
        print("INVALID INPUT")
    else:
        rad = math.atan(1/y)
        deg = math.degrees(rad)
        show("ARC COTANGENT OF", y, "is:", deg, "degrees")

def arcsecant_():
    y =qw()
    if -1<y<1:
        print("Invalid Input")
    else:
        result = math.degrees(math.acos(1/y))
        show("ARC SECANT OF", y, "is:", result, "degrees")

def arccosecant_():
    y = qw()
    if -1<y<1:
        print("Invalid Input")
    else:
          result = math.degrees(math.asin(1/y))
          show("ARC COSECANT OF", y, "is:", result, "degrees")
  
# ============================================================
# ================= ARITHMETIC INPUT + HELPERS =============
# ============================================================

def ma(s, v):
    if v == "add":
        result = 0
    elif v == "mul":
        result = 1
    elif v == "sub":
        result = get("From which number you want to subtract? ")

    y = get(s)
    for i in range(1, int(y)+1):
        while True:
            try:
                a = float(input(f"Enter number {i}: "))
                if v == "add":
                    result += a 
                if v == "mul":
                    result *= a
                if v == "sub":
                    result -= a 
                break
            except ValueError:
                print("Enter number!")
    return result

def one_num(name, value):
    show(name, value)

def add_():
    y = ma("How many numbers you want to add? ", "add") 
    show("SUM RESULT =", y)

def sub_():
    y = ma("How many numbers you want to subtract? ", "sub")
    show("SUBTRACTION RESULT =", y)

def mul_():
    y = ma("How many numbers you want to multiply? ", "mul")
    show("MULTIPLICATION RESULT =", y)

def div_():
    print("Which number you want to divide with which one?")
    a = get("Enter the number to be divided: ")
    b = get("Enter the number to divide by: ")
    if b == 0:
        print("Division by zero is not defined")
    else:
        show("DIVISION RESULT =", a/b)

def exp_():
    a = get("Enter the base number: ")
    b = get("Enter the exponent: ")
    show("EXPONENT RESULT =", a**b)

def sqrt():
    y = get("Enter number: ")
    one_num("Square root of", y**0.5)

def sqr():
    y = get("Enter number: ")
    one_num("Square of", y**2)

def cube():
    y = get("Enter number: ")
    one_num("Cube of", y**3)

def inv():
    y = get("Enter number: ")
    if y == 0:
        print("Not defined")
    else:
        one_num("Inverse of", 1/y)

def fact():
    y = get("Enter number: ")
    x = 1
    if y < 0:
        print("Enter positive value!")
    else:
        for i in range(1, int(y)+1):
            x *= i
        show("Factorial of", y, "is", x)

# ============================================================
# ======================= MAIN PROGRAM LOOP =================
# ============================================================

while True:
    print("\nCHOOSE TYPE OF CALCULATOR YOU WANT:\n1.ARITHMETIC CALCULATOR\n2.TRIGONOMETRIC CALCULATOR\n3.STATISTICS\n4.VIEW HISTORY\n5.CLEAR HISTORY\n6.EXIT")
    n = get("ENTER: ")
    if n == 1:
        while True:
            print("\nCHOOSE ARITHMETIC OPERATION\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXPONENTIAL\n6.SQUARE ROOT\n7.Square of a number\n8.Cube of a number\n9.inverse of a number\n10.Factorial of a number\n11.EXIT")
            x = get("ENTER: ")
            if x == 1: add_()
            elif x == 2: sub_()
            elif x == 3: mul_()
            elif x == 4: div_()
            elif x == 5: exp_()
            elif x == 6: sqrt()
            elif x == 7: sqr()
            elif x == 8: cube()
            elif x == 9: inv()
            elif x == 10: fact()
            elif x == 11: break
    elif n == 2:
        while True:
            print("\nTRIGONOMETRIC OPERATIONS:\n1.SINE\n2.COSINE\n3.TANGENT\n4.COTANGENT\n5.SECANT\n6.COSECANT\n7.ARC SINE\n8.ARC COSINE\n9.ARC TANGENT\n10.ARC COTANGENT\n11.ARC SECANT\n12.ARC COSECANT\n13.EXIT")
            y = get("ENTER: ")
            if y == 1: sin_()
            elif y == 2: cosine_()
            elif y == 3: tangent_()
            elif y == 4: cotangent_()
            elif y == 5: secant_()
            elif y == 6: cosecant_()
            elif y == 7: arcsine_()
            elif y == 8: arccosine_()
            elif y == 9: arctangent_()
            elif y == 10: arccotangent_()
            elif y == 11: arcsecant_()
            elif y == 12: arccosecant_()
            elif y == 13: break
    elif n == 3:
        while True:
            print("What do you want to calculate?\n1.MEAN\n2.MEDIAN\n3.MODE\n4.EXIT")
            z = get("ENTER: ")
            if z == 1: mean()
            elif z == 2: median()
            elif z == 3: mode()
            elif z == 4: break
    elif n == 4:
        viewhistory_()
    elif n == 5:
        clear()
    elif n == 6:
        print("EXITING...")
        break
