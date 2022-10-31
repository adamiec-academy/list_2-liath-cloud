def multiplication_table(y1, y2, x1, x2):
    # Counting Max Space
    highest_no = len(str(y2 * x2)) + 1

    first_line = " " * highest_no + "|"

    for i in range(y1, y2+1):
        length_of_no = len(str(i))
        space = highest_no - length_of_no

        first_line += " " * space + str(i)

    print(first_line)

    # Line of ----
    total_length_of_table = len(first_line)
    line_two = "-" * total_length_of_table
    print(line_two)

    # Rest of table
    for i in range(x1, x2+1):
        length_of_no = len(str(i))
        space = highest_no - length_of_no - 1

        line = " " * space + str(i) + " " * 1 + "|"

        for j in range(y1, y2+1):

            length_of_no = len(str(i * j))
            space = highest_no - length_of_no

            line += " " * space + str(i * j)

        print(line)
