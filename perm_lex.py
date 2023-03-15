# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):
    lst = []
    if len(str_in) == 0:  # Base case 1
        return []
    if len(str_in) == 1:  # Base case 2
        return [str_in]
    for i in range(len(str_in)):  # Loop to pick location of removed char
        for j in perm_gen_lex(str_in[:i] + str_in[i+1:]):  # Loop to recursively call function with outer loop removal
            lst.append(str_in[i] + j)
    return lst
