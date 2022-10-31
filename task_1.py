def remove_parentheses(text):
    
    new_text = ''
    indx_new_text = 0

    flag = 0

    for i in text:

        if i == "(":
            flag = 1

        elif flag == 0:
            new_text += i
            indx_new_text += 1

        elif i == ")":
            flag = -1

        elif flag == -1:
            flag = 0

    return new_text

