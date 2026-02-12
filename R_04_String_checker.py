def string_checker(inquiry, tolerable_answers=("yes", "no", "y", "n")):
    """Asks a yes or no question and requires a yes or no response."""

    # Repeats asking until it is answered appropriately with "yes" or "no".
    while True:
        result = input(inquiry).lower()

        # If the result is in tolerable answers then return the first letter of the response.
        if result in tolerable_answers:
            return result[0]

        elif len(result) == 1 and result[0] == tolerable_answers[0][0]:
            pass

        else:
            # Error message for iff a mistake is made.
            print("🚨 ERROR: This Field is required. Please enter a 'yes' or 'no' response. 🚨")


# Main routine goes here
string_checker("Do you like cheese? ", ("yes", "no", "maybe"))


