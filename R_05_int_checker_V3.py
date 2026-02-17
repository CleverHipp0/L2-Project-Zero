def int_checker(question, hi, lo):
    """Checks if a number is an integer or a float depending on the situation"""

    # Error message set up
    error = f"🚨 ERROR: Please enter an integer (whole number) between {lo} and {hi}. 🚨"

    while True:
        # Strips unnecessary character
        result = input(question).strip(r"\ ")


        # Converts result to int or float if possible, else it prints an error.
        try:

            if lo < int(result) < hi:
                return result
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine
print(int_checker("Number to check: ", 10, 1))

