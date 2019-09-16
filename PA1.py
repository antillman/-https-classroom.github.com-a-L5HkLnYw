# Programmer: (Ariel Tillman)
# Course: CS151, Dr. Simari
# Date: (9/18/2019)
# Programming Assignment: 1
# Program Inputs: (what is the length, width, and height of a room)
# Program Outputs: (Computes total area to be painted and amount of primer and paint)

# output purpose
print("This program will compute the area of a room.")

# get input (dimensions) from user
length = input("Please enter the length of the room:")
length = int(length)

width = input("Please enter the width of the room:")
width = int(width)

height = input("Please enter the height of the room:")
height = int(height)

# compute the area of the room
area = length * width + 2 * length * height + 2 * width * height

# Output result
print("The area of the room is", area, ".")

# compute the amount of primer
primer = area / 200

# compute the amount of paint
paint = area / 350

# Output result
print("The amount of paint is", paint, ".")

# Output result
print("The amount of primer is", primer, ".")
