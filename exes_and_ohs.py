def xo(s):
    input_string = s.lower()
    num_x = input_string.count('x')
    num_o = input_string.count('o')
    
    if num_x == num_o:    
        return True
    else:
        return False

print(xo('ooxx'))
print(xo('xooxx'))