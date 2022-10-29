def is_prime(n):
    dzielniki = []
    i = 2
    flag = 0

    while i != n:

        if i not in dzielniki:

            if n % i != 0:

                for j in range(i, n, i):
                    dzielniki.append(j)

            else:
                flag = 1
                break

        i += 1

    if flag == 1:
        return False

    else:
        return True



def is_diabolic(n):
    if "666" in str(n):
        return True

    else:
        return False
