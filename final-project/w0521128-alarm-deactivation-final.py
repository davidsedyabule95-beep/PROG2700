# Alarm Deactivation Program
# Follows the provided flowchart exactly

def read_passcodes():
    """Read valid 5-digit passcodes from passwords.txt"""
    try:
        with open("passwords.txt", "r") as file:
            codes = [line.strip() for line in file.readlines() if line.strip()]
        return codes
    except FileNotFoundError:
        print("Error: passwords.txt not found.")
        exit()


def is_valid_number(user_input):
    """Check if the input is exactly 5 digits."""
    return user_input.isdigit() and len(user_input) == 5


def main():
    # ----- Start / Initialization -----
    alarm_status = "off"
    alarm_activated_status = "off"   # You said teacher's correction: must be OFF
    password_attempts = 3

    # Load password list from file
    password_list = read_passcodes()

    # ----- Main Loop (3 attempts max) -----
    while password_attempts > 0:

        print("Enter your 5 digit password:")
        user_input = input().strip()

        # Convert ASCII keyboard input to number (flowchart wording)
        # Here it simply stays as a string, but validation checks digits.
        if not is_valid_number(user_input):
            print("Invalid Password")
            password_attempts -= 1
            continue

        # Valid 5-digit number, now check attempts
        if password_attempts <= 3:
            # Create password list already loaded from file
            # Check password
            if user_input in password_list:
                # Password Match
                alarm_status = "off"
                alarm_activated_status = "off"
                print("Alarm Status:", alarm_status)
                print("Alarm Activated Status:", alarm_activated_status)
                return
            else:
                print("Invalid Password")
                password_attempts -= 1

    # ----- If user failed all 3 attempts -----
    alarm_status = "on"
    alarm_activated_status = "on"
    print("Alarm Status:", alarm_status)
    print("Alarm Activated Status:", alarm_activated_status)


# Run program
main()
