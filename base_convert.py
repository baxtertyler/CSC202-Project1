# int, int -> string
# Given integer num and base b, converts num to a string representation in base b
def convert(num, b):
    quotient = num // b  # Finds 1 and r
    remainder = num % b
    remainder_s = str(remainder)
    if remainder_s == "10":  # Sets char var to remainder when >10
        remainder_s = "A"
    if remainder_s == "11":
        remainder_s = "B"
    if remainder_s == "12":
        remainder_s = "C"
    if remainder_s == "13":
        remainder_s = "D"
    if remainder_s == "14":
        remainder_s = "E"
    if remainder_s == "15":
        remainder_s = "F"
    if quotient == 0:
        return remainder_s
    return convert(quotient, b) + remainder_s  # recursive call to get all remainder
