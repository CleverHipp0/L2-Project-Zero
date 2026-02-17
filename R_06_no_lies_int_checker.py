def int_checker(question):
    """Checks if a number is an integer"""

    # Error message set up
    error = "🚨 ERROR: Please enter an integer (whole number) more than zero. 🚨"

    while True:
        # Strips unnecessary character
        result = input(question).strip(r"\ ")

        # Checks if the number is an integer and then outputs an error if it isn't
        try:
            result = int(result)
            return result

        except ValueError:
            print(error)

# Main routine

# Loop
while True:
    # ask for their name
    name = input("Name? ") # Not blank
    # ask for their age
    age = int_checker("Age? ")

    # age range
    if 12 > age:
        print("Sorry, you are too young.")
        continue

    elif 120 < age:
        print("Sorry, you are too old.")
        continue

    else:
        print("All Good!")


