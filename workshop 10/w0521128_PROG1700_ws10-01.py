import csv

def task_a_daily_log():
    """Task A: Daily summary writer"""
    print("\n" + "="*50)
    print("TASK A: DAILY LOG WRITER")
    print("="*50)
    
    entry_count = 0
    
    while True:
        entry = input("\nEnter daily note (or 'done' to finish): ")
        
        if entry.lower() == "done":
            break
        
        if entry.strip() == "":
            print("Empty entries not allowed.")
            continue
        
        try:
            with open("daily_log.txt", "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}] {entry}\n")
            entry_count += 1
            print(f"✓ Entry #{entry_count} logged")
        except Exception as e:
            print(f"Error writing to log: {e}")
    
    # Display log
    try:
        with open("daily_log.txt", "r") as file:
            contents = file.read()
            print("\n" + "="*50)
            print(f"DAILY LOG ({entry_count} entries)")
            print("="*50)
            print(contents)
    except FileNotFoundError:
        print("No log entries found.")

def task_b_inventory_reader():
    """Task B: Read grocery inventory"""
    print("\n" + "="*50)
    print("TASK B: INVENTORY READER")
    print("="*50)
    
    # Create sample inventory file
    sample_data = "Apples,3.50\nBananas,2.75\nBread,2.99\nMilk,4.25\nEggs,3.99\n"
    with open("inventory.txt", "w") as file:
        file.write(sample_data)
    
    try:
        with open("inventory.txt", "r") as file:
            total_value = 0
            item_count = 0
            
            print("\nITEM                 PRICE")
            print("-" * 30)
            
            for line in file:
                try:
                    if line.strip():  # Skip blank lines
                        name, price = line.strip().split(",")
                        price = float(price)
                        print(f"{name:<20} ${price:.2f}")
                        total_value += price
                        item_count += 1
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
            
            print("-" * 30)
            print(f"Total Items: {item_count}")
            print(f"Total Value: ${total_value:.2f}")
            if item_count > 0:
                print(f"Average Price: ${total_value/item_count:.2f}")
                
    except FileNotFoundError:
        print("Inventory file not found!")

def task_c_cafe_sales_writer():
    """Task C: Café sales CSV export"""
    print("\n" + "="*50)
    print("TASK C: CAFÉ SALES EXPORT")
    print("="*50)
    
    sales = [
        ["Latte", 12, 3.25],
        ["Tea", 10, 2.50],
        ["Muffin", 5, 2.00],
        ["Cappuccino", 8, 3.75]
    ]
    
    try:
        with open("cafe_sales.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Item", "Quantity", "Price", "Revenue"])
            
            total_revenue = 0
            
            for row in sales:
                revenue = row[1] * row[2]
                writer.writerow([row[0], row[1], f"${row[2]:.2f}", f"${revenue:.2f}"])
                total_revenue += revenue
            
            writer.writerow(["", "", "TOTAL:", f"${total_revenue:.2f}"])
        
        print("✓ Sales data exported to cafe_sales.csv")
        print(f"Total Revenue: ${total_revenue:.2f}")
        
    except Exception as e:
        print(f"Error writing sales data: {e}")

def task_d_grades_reader():
    """Task D: Student grades report"""
    print("\n" + "="*50)
    print("TASK D: GRADES REPORT")
    print("="*50)
    
    # Create sample grades file
    grades_data = [
        ["Name", "Grade"],
        ["Ava", "88"],
        ["Noah", "92"],
        ["Liam", "79"],
        ["Emma", "95"],
        ["Sophia", "85"]
    ]
    
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(grades_data)
    
    try:
        with open("grades.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            
            print("\nSTUDENT              GRADE    STATUS")
            print("-" * 40)
            
            grades = []
            for row in rows[1:]:  # Skip header
                name, grade = row[0], int(row[1])
                grades.append(grade)
                status = "Pass" if grade >= 60 else "Fail"
                print(f"{name:<20} {grade:<8} {status}")
            
            # Calculate statistics
            avg_grade = sum(grades) / len(grades)
            highest = max(grades)
            lowest = min(grades)
            
            print("-" * 40)
            print(f"Average Grade: {avg_grade:.2f}")
            print(f"Highest Grade: {highest}")
            print(f"Lowest Grade: {lowest}")
            
            # Write summary
            with open("grades_summary.txt", "w") as summary:
                summary.write("GRADES SUMMARY REPORT\n")
                summary.write("="*40 + "\n")
                summary.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                summary.write(f"Total Students: {len(grades)}\n")
                summary.write(f"Average Grade: {avg_grade:.2f}\n")
                summary.write(f"Highest Grade: {highest}\n")
                summary.write(f"Lowest Grade: {lowest}\n")
                summary.write(f"Pass Rate: {sum(1 for g in grades if g >= 60)/len(grades)*100:.1f}%\n")
            
            print("\n✓ Summary saved to grades_summary.txt")
            
    except Exception as e:
        print(f"Error processing grades: {e}")


def create_session_summary(calc_count, conv_count):
    """Create session summary report"""
    try:
        with open("session_summary.txt", "w") as file:
            file.write("SESSION SUMMARY REPORT\n")
            file.write("="*50 + "\n")
            file.write(f"Session Date: {datetime.now().strftime('%Y-%m-%d')}\n")
            file.write(f"Session Time: {datetime.now().strftime('%H:%M:%S')}\n\n")
            file.write(f"Total Calculations Performed: {calc_count}\n")
            file.write(f"Total Conversions Performed: {conv_count}\n")
            file.write(f"Total Operations: {calc_count + conv_count}\n")
            file.write("="*50 + "\n")
        
        print("\n✓ Session summary saved to session_summary.txt")
    except Exception as e:
        print(f"Error creating summary: {e}")




def main():
    """Main program entry point"""
    print("="*60)
    print(" FILE I/O & PERSISTENCE LAB - COMPLETE SOLUTION")
    print("="*60)
    
    calc_count = 0
    conv_count = 0
    
    while True:
        print("\n" + "="*60)
        print("MAIN MENU")
        print("="*60)
        print("WORKSHOP 10-00:")
        print("  1. Modular Calculator (with text logging)")
        print("  2. Unit Converter (with CSV logging)")
        print("\nWORKSHOP 10-01:")
        print("  3. Task A - Daily Log Writer")
        print("  4. Task B - Inventory Reader")
        print("  5. Task C - Café Sales Export")
        print("  6. Task D - Grades Report")
        print("\nOTHER:")
        print("  7. Generate Session Summary")
        print("  8. Exit Program")
        
        choice = input("\nEnter choice (1-8): ")
        
        if choice == "1":
            calc_count += calculator()
        elif choice == "2":
            conv_count += converter()
        elif choice == "3":
            task_a_daily_log()
        elif choice == "4":
            task_b_inventory_reader()
        elif choice == "5":
            task_c_cafe_sales_writer()
        elif choice == "6":
            task_d_grades_reader()
        elif choice == "7":
            create_session_summary(calc_count, conv_count)
        elif choice == "8":
            print("\nThank you for using the File I/O Lab!")
            create_session_summary(calc_count, conv_count)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



# Reflection Questions 


# Reflection:
# 1. Importance of file persistence:
#    Allows data to be saved between sessions, enabling history, reports,
#    and stateful applications.

# 2. Best file type (text vs. CSV):
#    CSV is ideal for structured, multi-field data; text files work better
#    for simple, flexible, human-readable content.

# 3. Effect of combining functions and file I/O:
#    Improves modularity and organization by giving each function a clear role
#    and separating storage from program logic.

# 4. What to store next:
#    Could include user preferences, search/filter features, data visualizations,
#    export formats like JSON/PDF, or user-specific histories.


