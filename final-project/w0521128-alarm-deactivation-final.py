# Alarm Deactivation System
# PROG1700 - Logic & Programming

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
    except:
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
    return user_input in passcodes

def run_alarm_system():
    """Main alarm system controller"""
    # Set initial states (start)
    alarm_status = "off"
    alarm_activated_status = "off"
    password_attempts = 3
    
    # Read passcodes from file
    passcodes = read_passcodes()
    
    # Main loop - keep going until alarm triggers or deactivated
    while True:
        # Display to User: Enter your 5 digit Password
        print(f"\nEnter your 5 digit Password")
        user_input = input()
        
        # Convert Keyboard ASCII to Number (already done by input)
        
        # Valid Number?
        if not is_valid_number(user_input):
            # No - Display to User: Invalid Password
            print("Invalid Password")
            # Continue to password attempts check (loop continues)
        else:
            # Yes - Check Password first before decrementing
            if check_password(user_input, passcodes):
                # Password Match
                alarm_status = "off"
                alarm_activated_status = "off"
                print("\nAlarm Status: off")
                print("Alarm Activated Status: off")
                break
            else:
                # Incorrect Password - Decrement the password_attempts counter
                password_attempts -= 1
                print("Incorrect Password")
                
                # Password Attempts = 0?
                if password_attempts == 0:
                    # Yes - Set alarm_status to on, Display alarm_status to User
                    alarm_status = "on"
                    alarm_activated_status = "on"
                    print("\nAlarm Status: on")
                    print("Alarm Activated Status: on")
                    break
                else:
                    # Show remaining attempts
                    print(f"You have {password_attempts} attempts remaining")
                # Loop back to display prompt

# Run the program
print("=== Alarm Deactivation System ===")
print("System Status: ACTIVATED")
run_alarm_system()
print("\n=== System End ===")