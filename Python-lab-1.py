
# Remove the first occurrence of 20
a = [10, 20, 30, 20, 40, 50]
a.remove(20)
print(a) 

# Remove element at index 1 and return its value
a = [10, 20, 30, 20, 40, 50]
val = a.pop(1)
print(val)  
print(a) 

# Remove elements from index 1 to index 3
a = [10, 20, 30, 40, 50, 60, 70]
del a[1:4]
print(a) 

# Remove all elements
a = [10, 20, 30, 40, 50, 60, 70]
a.clear()
print(a)  

# Count occurrences of 'iti' in a string
text = "iti is a great iti initiative iti!"
count = text.count('iti')
print(count) 

# Convert binary to decimal
binary = input("Enter a binary number: ")
decimal = int(binary, 2)
print("Decimal:", decimal)

# FizzBuzz function
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

num = int(input("Enter a number: "))
print(fizzbuzz(num))

# Calculate area and circumference of a circle
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"Area: {area}")
print(f"Circumference: {circumference}")

# Get user details
name = input("Enter your name: ")
while not name.isalpha():
    name = input("Invalid input. Enter your name: ")

email = input("Enter your email: ")
print(f"Name: {name}, Email: {email}")
