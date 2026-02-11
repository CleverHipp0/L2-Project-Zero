def not_blank(element):
    """Checks whether an answer is not blank."""

    # Checks the length of the answer and outputs an error if it is too short.
    if len(element.strip()) > 0:
        return element
    else:
        return "xxx"


def yes_no(inquiry):
    """Asks a yes or no question and requires a yes or no response."""

    # Sets up a list of tolerable answers.
    tolerable_answers = ["yes", "no"]

    # Repeats asking until it is answered appropriately.
    while True:
        result = not_blank(input(inquiry).lower())

        # Loops for all words in the appropriate answers list
        for word in tolerable_answers:

            if word == result or word[0] == result[0]:
                return word

        # Error message
        print("🚨 ERROR: This Field is required. Please enter a 'yes' or 'no' response. 🚨")


# Main routine goes here

if yes_no("Do you like com sci? ") == "no":
    print("Wrong answer")
else:
    print("Correct")