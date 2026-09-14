# Program to identify the type of triangle using a function

def triangle_type(a, b, c):
    # Check whether the given sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle"

    # Check for equilateral triangle
    if a == b == c:
        return "Equilateral triangle"

    # Check for isosceles triangle
    elif a == b or b == c or a == c:
        triangle = "Isosceles triangle"
    else:
        triangle = "Scalene triangle"

    # Check for right-angled triangle
    sides = sorted([a, b, c])

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        triangle += " and Right-angled triangle"

    return triangle


# Accept three sides from the user
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

result = triangle_type(side1, side2, side3)

print("The triangle is:", result)
