# Functions go here
def statement_generator(statement, decoration, lines=1):
    """Creates headings (3 lines), sub-headings (2 lines), and mini headings (1 line).
    ONLY USE EMOJIS FOR SINGLE LINE TEXT!!"""

    # This is where the nitty-gritty "command" line is formed.
    # It contains all the important information like the statement.
    command_line = f"{decoration * 3} {statement} {decoration * 3}"

    # Finds the length of the command line.
    command_line_length = len(command_line)

    # Repeats the decoration for the length of the command line.
    top_and_bottom_line = decoration * command_line_length

    # Determines how many lines are needed for the statement.
    # If the number of lines is inserted incorrectly outputs error
    if lines == 1:
        print(command_line)

    elif lines == 2:
        print(f"{command_line} \n{top_and_bottom_line}")

    elif lines == 3:
        print(f"{top_and_bottom_line} \n{command_line} \n{top_and_bottom_line}")

    else:
        print("ERROR: Too many lines in 'statement_generator'.")

# Main Routine goes here
statement_generator("Cameron is Awesome!", "😎")
print()
statement_generator("Cameron is Awesome!", "-", 2)
print()
statement_generator("Cameron is Awesome!", "=", 3)
print()

