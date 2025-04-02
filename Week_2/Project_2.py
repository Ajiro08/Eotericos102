import math

def find_cubic_roots():
    """
    Finds the roots of a cubic equation: ax^3 + bx^2 + cx + d = 0
    """
    print("Cubic Equation: ax^3 + bx^2 + cx + d = 0")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    d = float(input("Enter the value of d: "))

    # Calculate the discriminant
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    
    # Calculate the roots
    if p == 0 and q == 0:
        print("The equation has three real roots:")
        print(f"x1 = x2 = x3 = {-b / (3 * a)}")
    else:
        # Calculate the discriminant
        D = q ** 2 / 4 + p ** 3 / 27
        
        if D > 0:
            print("The equation has one real root and two complex roots:")
            u = -q / 2 + math.sqrt(D)
            v = -q / 2 - math.sqrt(D)
            x1 = 2 * math.pow(u, 1/3) - b / (3 * a)
            x2 = -math.pow(u, 1/3) + b / (3 * a) + 1j * math.sqrt(3) * math.pow(u, 1/3)
            x3 = -math.pow(u, 1/3) + b / (3 * a) - 1j * math.sqrt(3) * math.pow(u, 1/3)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
            print(f"x3 = {x3}")
        elif D == 0:
            print("The equation has three real roots:")
            x1 = -b / (3 * a) - 2 * math.pow(-q / 2, 1/3)
            x2 = -b / (3 * a) + math.pow(-q / 2, 1/3)
            x3 = x2
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
            print(f"x3 = {x3}")
        else:
            print("The equation has three real roots:")
            theta = math.acos(-q / (2 * math.sqrt(-p ** 3 / 27)))
            r = 2 * math.sqrt(-p / 3)
            x1 = r * math.cos(theta / 3) - b / (3 * a)
            x2 = r * math.cos((theta + 2 * math.pi) / 3) - b / (3 * a)
            x3 = r * math.cos((theta - 2 * math.pi) / 3) - b / (3 * a)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
            print(f"x3 = {x3}")

def find_quartic_roots():
    """
    Finds the roots of a quartic equation: ax^4 + bx^3 + cx^2 + dx + e = 0
    """
    print("Quartic Equation: ax^4 + bx^3 + cx^2 + dx + e = 0")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    d = float(input("Enter the value of d: "))
    e = float(input("Enter the value of e: "))
    
    # TODO: Implement the code to find the roots of a quartic equation
    print("Finding the roots of a quartic equation...")

def find_quadratic_roots():
    """
    Finds the roots of a quadratic equation: ax^2 + bx + c = 0
    """
    print("Quadratic Equation: ax^2 + bx + c = 0")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))

    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant > 0:
        print("The equation has two real roots:")
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif discriminant == 0:
        print("The equation has one real root:")
        x = -b / (2 * a)
        print(f"x = {x}")
    else:
        print("The equation has two complex roots:")
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"x1 = {real_part} + {imaginary_part}i")
        print(f"x2 = {real_part} - {imaginary_part}i")

def main():
    print("Choose an operation:")
    print("1. Find the roots of a Cubic Equation")
    print("2. Find the roots of a Quartic Equation")
    print("3. Find the roots of a Quadratic Equation")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        find_cubic_roots()
    elif choice == "2":
        find_quartic_roots()
    elif choice == "3":
        find_quadratic_roots()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
