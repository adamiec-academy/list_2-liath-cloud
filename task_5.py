def cipher(text, shift):
    new_message = ""
    for i in text:

        if i == " ":
            new_message += i

        else:
            letter_no = ord(i)
            letter_no += shift

            if letter_no > 90 and letter_no <97:

                letter_no -= 90
                new_letter = 64 + letter_no
                new_message += chr(new_letter)

            elif letter_no > 122:

                letter_no -= 122
                new_letter = 96 + letter_no
                new_message += chr(new_letter)

            else:
                new_message += chr(letter_no)

    return new_message


def decipher(text, shift):
    new_message = ""
    for i in text:

        if i == " ":
            new_message += i

        else:
            letter_no = ord(i)
            letter_no -= shift

            if letter_no > 90 and letter_no <97:

                new_letter = 123 - 97 + letter_no
                new_message += chr(new_letter)

            elif letter_no < 65:

                new_letter = 90 - 65 + letter_no
                new_message += chr(new_letter)

            else:
                new_message += chr(letter_no)

    return new_message
