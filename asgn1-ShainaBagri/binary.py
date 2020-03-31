# Implements operations on binary numbers.
# CSC 225, Assignment 1
# Given code, Winter '20


def add(addend_a, addend_b):
    """
    Add two 8-bit, two's complement binary numbers; ignore carries/overflows.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param addend_a: A bitstring representing the first number
    :param addend_b: A bitstring representing the second number
    :return: A bitstring representing the sum
    """
    sum = ""
    add_a = list(addend_a)
    add_b = list(addend_b)
    x = 7
    carry = False
    while x >= 0:
        if add_a[x]=='0':
            col_a = 0
        else:
            col_a = 1
        if add_b[x]=='0':
            col_b = 0
        else:
            col_b = 1
        int_col = col_a + col_b
        if carry:
            int_col += 1
        if int_col==2:
            carry = True
            int_col = 0
        elif int_col==3:
            carry = True
            int_col = 1
        else:
            carry = False
        if int_col==0:
            sum = "0" + sum
        else:
            sum = "1" + sum
        x -= 1
    return sum



def negate(number):
    """
    Negate an 8-bit, two's complement binary number.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A bitstring representing the number to negate
    :return: A bistring representing the negated number
    """
    num = list(number)
    for x in range(0,8):
        if num[x]=='0':
            num[x]='1'
        else:
            num[x]='0'
    num_str = "".join(num)
    neg_num = add(num_str, "00000001")
    return neg_num


def subtract(minuend, subtrahend):
    """
    Subtract one 8-bit, two's complement binary number from another.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param minuend: A bitstring representing the number from which to subtract
    :param subtrahend: A bitstring representing the number to subtract
    :return: A bitstring representing the difference
    """
    neg_sub = negate(subtrahend)
    ans = add(minuend, neg_sub)
    return ans


def binary_to_decimal(number):
    """
    Convert an 8-bit, two's complement binary number to decimal.
    TODO: Implement this function.

    :param number: A bitstring representing the number to convert
    :return: An integer, the converted number
    """
    if number == "10000000":
        return -128
    ans = 0
    neg = False
    if number[0] == '1':
        number = negate(number)
        neg = True
    for i in range(0, 7):
        if number[7-i]=='1':
            ans += (2**i)
    if neg:
        ans *= -1
    return ans

def decimal_to_binary(number):
    """
    Convert a decimal number to 8-bit, two's complement binary.
    TODO: Implement this function.

    :param number: An integer, the number to convert
    :return: A bitstring representing the converted number
    :raise OverflowError: If the number cannot be represented with 8 bits
    """
    if number < -128 or number > 127:
        raise OverflowError
    if number == -128:
        return "10000000"
    bitstring = "0"
    neg = False
    if number < 0:
        neg = True
        number *= -1
    i = 6
    while i >= 0:
        if (2**i)<=number:
            number -= (2**i)
            bitstring += "1"
        else:
            bitstring += "0"
        i -= 1
    if neg:
        bitstring = negate(bitstring)
    return bitstring
