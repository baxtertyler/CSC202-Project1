# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    if n == 42:  # Base case
        return True
    if n % 2 == 0 and n > 42:  # checks for divisible by 2
        if bears(n // 2):  # recursive call if true
            return True
    if (n % 3 == 0 or n % 4 == 0) and n > 42 and not (int(str(n)[-1]) * int(str(n)[-2]) == 0):  # checks divisible 3,4
        if bears(n - (int(str(n)[-1]) * int(str(n)[-2]))):  # recursive call if true
            return True
    if n % 5 == 0 and n > 42:  # checks for divisible by 5
        if bears(n - 42):  # recursive call if true
            return True
    return False
