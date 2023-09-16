#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    print('Welcome to the geometric shape area calculator!')
    # User Options
    # Circle = 1
    # Rectangle = 2
    # Triangle = 3
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print('Circle' + ' ' + 'Rectangle' + ' ' + 'Triangle')
    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = input('Select a shape by entering 1, 2, or 3')
    # TODO: Convert the variable 'choice' to an integer data type.
    choice = int(choice)
    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    print(type(choice) == int)
    if choice == 1:  #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle

        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        radius = input("What would you like the radius to be?")
        # TODO: Convert 'radius' to float.
        radius = float(radius)
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        area = (radius * radius) * circle_pi
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        length = input('What is the length?')
        width = input('What is the width')
        # TODO: Convert both 'length' and 'width' to float.
        length = float(length)
        width = float(width)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        area = length * width
        # HINT: The formula to find the area of a rectangle: length times width

    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        base = input("what is the base?")
        height = input('What is the height?')
        # TODO: Convert both 'base' and 'height' to float.
        base = float(base)
        height = float(height)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        area = (.5*base) * height
        # HINT: The formula to find the area of a Triangle: half times base times height

    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
        print('Invalid Choice .')
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 
    steps = '''
    1. First I had to copy the repo from Github
    2. Then clone it to my computer
    3. Because there were no variables for the shapes, I had to enclose them in quotes
    4. Used input function, then assigned variable to new data type
    5. Used type() function to then use conditional to see if variable type was int
    5a. When asking for user input for measurements, had to do this step as well
    6. Rinse and repeat for all shapes
    - I just needed to adjust the formula based on shape
    7. Invalid choice only worked for ints, but not strings, but assignment did not ask for it so I left it
    8. instead of using multiple print statements, I assigned this part to a variable
    9. I ran the unittest, but it failed, so now I am in the process of trying to debug it,
    but all the errors are coming from the test files and not my actual code file
    10. Wish me luck on trying to debug it before I
    10a, Git add (file name) git commmit -m 'My notes', then git push 
    '''
    print(steps)

if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
