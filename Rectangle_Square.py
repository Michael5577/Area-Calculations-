# Function to calculate area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Function to calculate area of a square
def calculate_square_area(side):
    return side * side

if __name__ == "__main__":
    # Get user input for shape type
    shape_type = input("Enter 'rectangle' or 'square' to calculate area: ").lower()
    
    if shape_type == "rectangle":
        # Get length and width for rectangle
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        
        # Calculate and display area of rectangle
        area = calculate_rectangle_area(length, width)
        print(f"Area of the rectangle: {area}")
    
    elif shape_type == "square":
        # Get side length for square
        side = float(input("Enter the side length of the square: "))
        
        # Calculate and display area of square
        area = calculate_square_area(side)
        print(f"Area of the square: {area}")
    
    else:
        print("Invalid shape type entered. Please choose 'rectangle' or 'square'.")
