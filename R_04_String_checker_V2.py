def string_checker(question, valid_answers=("yes", "no", "y", "n"), first_letter_count=1):
    """Asks a yes or no question and requires a yes or no response."""

    # Repeats asking until it is answered appropriately with "yes" or "no".
    while True:
        result = input(question).lower()

        for item in valid_answers:
            # If the result is in tolerable answers then return the first letter of the response.
            if result == item or result == item[:first_letter_count]:
                return result


        # Error message for iff a mistake is made.
        print(f"🚨 ERROR: This Field is required. Please enter a response from this list: {valid_answers}. 🚨")


# Main routine goes here
print(string_checker("Do you like cheese? ", ("yes", "no", "maybe")))


