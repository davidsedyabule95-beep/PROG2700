# Alarm Deactivation System

def read_passcodes():
    """Read valid passcodes from passwords.txt file"""
    passcodes = []
    try:
        with open('passwords.txt', 'r') as file:
            for line in file:
                code = line.strip()
                if code:
                    passcodes.append(code)
        return passcodes
    except FileNotFoundError:
        print("Error: passwords.txt file not found")
        exit()

def is_valid_number(user_input):
    """Check if input is exactly 5 digits"""
    if len(user_input) != 5:
        return False
    if not user_input.isdigit():
        return False
    return True

def check_password(user_input, passcodes):
    """Check if the password matches any valid passcode"""
    if user_input in passcodes:
        return True
    return False

def run_alarm_system():
    """Main alarm system controller"""
    # Set initial states
    alarm_status = "off"
    alarm_activated_status = "off"
    password_attempts = 3
    
    # Read passcodes from file
    passcodes = read_passcodes()
    
    # Main loop
    while password_attempts > 0:
        # Display prompt to user
        print("\nEnter your 5 digit Password")
        user_input = input()
        
        # Check if valid number
        if not is_valid_number(user_input):
            print("Invalid Password")
            password_attempts -= 1
            continue
        
        # Decrement password attempts counter
        password_attempts -= 1
        
        # Check if attempts exhausted
        if password_attempts == 0:
            alarm_status = "on"
            alarm_activated_status = "on"
            print("\nAlarm Status: on")
            print("Alarm Activated Status: on")
            break
        
        # Check password against list
        if check_password(user_input, passcodes):
            # Password match
            alarm_status = "off"
            alarm_activated_status = "off"
            print("\nAlarm Status: off")
            print("Alarm Activated Status: off")
            break
        else:
            # Reset the password attempts counter
            password_attempts = 3

# Run the program
run_alarm_system()