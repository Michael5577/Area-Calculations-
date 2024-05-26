import math

# Function to calculate area of a circle
def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Function to calculate circumference of a circle
def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

if __name__ == "__main__":
    # Get radius input from user
    radius = float(input("Enter the radius of the circle: "))
    
    # Calculate area and circumference
    area = calculate_circle_area(radius)
    circumference = calculate_circle_circumference(radius)
    
    # Display results
    print(f"Area of the circle: {area}")
    print(f"Circumference of the circle: {circumference}")
