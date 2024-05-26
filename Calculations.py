from Circle import calculate_circle_area, calculate_circle_circumference
from Rectangle_Square import calculate_rectangle_area, calculate_square_area

if __name__ == "__main__":
    print("Welcome to the calculations program!")
    
    while True:
        print("\nMenu:")
        print("1. Calculate area and circumference of a circle")
        print("2. Calculate area of a rectangle")
        print("3. Calculate area of a square")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            radius = float(input("Enter the radius of the circle: "))
            area = calculate_circle_area(radius)
            circumference = calculate_circle_circumference(radius)
            print(f"Area of the circle: {area}")
            print(f"Circumference of the circle: {circumference}")
        
        elif choice == "2":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = calculate_rectangle_area(length, width)
            print(f"Area of the rectangle: {area}")
        
        elif choice == "3":
            side = float(input("Enter the side length of the square: "))
            area = calculate_square_area(side)
            print(f"Area of the square: {area}")
        
        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
