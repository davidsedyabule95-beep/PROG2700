import csv
from datetime import datetime

# Calculator Functions
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b with error handling"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def log_calculation(num1, operator, num2, result):
    """Log calculation to text file with timestamp"""
    try:
        with open("calc_log.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {num1} {operator} {num2} = {result}\n")
        print("✓ Calculation logged successfully")
    except Exception as e:
        print(f"Error logging calculation: {e}")

def view_calc_log():
    """Read and display the calculation log"""
    try:
        with open("calc_log.txt", "r") as file:
            contents = file.read()
            if contents:
                print("\n" + "="*50)
                print("CALCULATION LOG")
                print("="*50)
                print(contents)
            else:
                print("No calculations logged yet.")
    except FileNotFoundError:
        print("No log file found. Perform a calculation first!")

def calculator():
    """Main calculator function with file logging"""
    calc_count = 0
    
    while True:
        print("\n" + "="*50)
        print("MODULAR CALCULATOR")
        print("="*50)
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View Calculation Log")
        print("6. Exit Calculator")
        
        choice = input("\nEnter choice (1-6): ")
        
        if choice == "6":
            break
        elif choice == "5":
            view_calc_log()
            continue
        elif choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                result = add(num1, num2)
                operator = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                operator = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                operator = "*"
            elif choice == "4":
                result = divide(num1, num2)
                operator = "/"
            
            if isinstance(result, str):  # Error message
                print(result)
            else:
                print(f"\nResult: {num1} {operator} {num2} = {result}")
                log_calculation(num1, operator, num2, result)
                calc_count += 1
                
        except ValueError:
            print("Error: Please enter valid numbers")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    return calc_count


# Converter Functions
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def km_to_miles(km):
    """Convert kilometers to miles"""
    return km * 0.621371

def miles_to_km(miles):
    """Convert miles to kilometers"""
    return miles / 0.621371

def kg_to_pounds(kg):
    """Convert kilograms to pounds"""
    return kg * 2.20462

def pounds_to_kg(pounds):
    """Convert pounds to kilograms"""
    return pounds / 2.20462

def log_conversion(conv_type, input_val, output_val):
    """Log conversion to CSV file"""
    try:
        # Check if file exists to determine if header is needed
        try:
            with open("conversions.csv", "r") as file:
                has_header = True
        except FileNotFoundError:
            has_header = False
        
        with open("conversions.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not has_header:
                writer.writerow(["Type", "Input", "Output", "Timestamp"])
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([conv_type, round(input_val, 2), round(output_val, 2), timestamp])
        
        print("✓ Conversion logged successfully")
    except Exception as e:
        print(f"Error logging conversion: {e}")

def view_conversions():
    """Read and display all conversions"""
    try:
        with open("conversions.csv", "r") as file:
            reader = csv.reader(file)
            print("\n" + "="*70)
            print("CONVERSION HISTORY")
            print("="*70)
            
            rows = list(reader)
            if len(rows) <= 1:
                print("No conversions logged yet.")
            else:
                # Print header
                print(f"{rows[0][0]:<25} {rows[0][1]:<15} {rows[0][2]:<15} {rows[0][3]}")
                print("-"*70)
                # Print data
                for row in rows[1:]:
                    print(f"{row[0]:<25} {row[1]:<15} {row[2]:<15} {row[3]}")
                    
    except FileNotFoundError:
        print("No conversion history found. Perform a conversion first!")

def converter():
    """Main converter function with CSV logging"""
    conv_count = 0
    
    while True:
        print("\n" + "="*50)
        print("UNIT CONVERTER")
        print("="*50)
        print("1. Celsius → Fahrenheit")
        print("2. Fahrenheit → Celsius")
        print("3. Kilometers → Miles")
        print("4. Miles → Kilometers")
        print("5. Kilograms → Pounds")
        print("6. Pounds → Kilograms")
        print("7. View Conversion History")
        print("8. Exit Converter")
        
        choice = input("\nEnter choice (1-8): ")
        
        if choice == "8":
            break
        elif choice == "7":
            view_conversions()
            continue
        elif choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please try again.")
            continue
        
        try:
            value = float(input("Enter value to convert: "))
            
            if choice == "1":
                result = celsius_to_fahrenheit(value)
                conv_type = "Celsius → Fahrenheit"
                print(f"\n{value}°C = {round(result, 2)}°F")
            elif choice == "2":
                result = fahrenheit_to_celsius(value)
                conv_type = "Fahrenheit → Celsius"
                print(f"\n{value}°F = {round(result, 2)}°C")
            elif choice == "3":
                result = km_to_miles(value)
                conv_type = "Kilometers → Miles"
                print(f"\n{value} km = {round(result, 2)} miles")
            elif choice == "4":
                result = miles_to_km(value)
                conv_type = "Miles → Kilometers"
                print(f"\n{value} miles = {round(result, 2)} km")
            elif choice == "5":
                result = kg_to_pounds(value)
                conv_type = "Kilograms → Pounds"
                print(f"\n{value} kg = {round(result, 2)} lbs")
            elif choice == "6":
                result = pounds_to_kg(value)
                conv_type = "Pounds → Kilograms"
                print(f"\n{value} lbs = {round(result, 2)} kg")
            
            log_conversion(conv_type, value, result)
            conv_count += 1
            
        except ValueError:
            print("Error: Please enter a valid number")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    return conv_count