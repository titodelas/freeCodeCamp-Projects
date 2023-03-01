def arithmetic_arranger(problems, show_answer=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for problem in problems:
        # Split the problem into the two operands and the operator
        operand1, operator, operand2 = problem.split()

        # Check if the operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if the operands are valid
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Check if the operands are too long
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the length of the longest operand
        max_length = max(len(operand1), len(operand2))

        # Create the first line of the problem
        first_line += operand1.rjust(max_length + 2)
        first_line += "    "
        # Create the second line of the problem
        second_line += operator + " " + operand2.rjust(max_length)
        second_line += "    "
        # Create the line of dashes
        dash_line += "-" * (max_length + 2)
        dash_line += "    "
        # Create the answer line if show_answer is True
        if show_answer:
            if operator == "+":
                answer = int(operand1) + int(operand2)
            else:
                answer = int(operand1) - int(operand2)
            answer_line += str(answer).rjust(max_length + 2)
            answer_line += "    "

    # Combine the lines into the arranged problems string
    arranged_problems += first_line.rstrip() + "\n"
    arranged_problems += second_line.rstrip() + "\n"
    arranged_problems += dash_line.rstrip()
    if show_answer:
        arranged_problems += "\n" + answer_line.rstrip()

    return arranged_problems