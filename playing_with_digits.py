def dig_pow(n, p):
    # your code
    s = str(n)
    list_s = list(s)
    result = 0
    p_temp = p
    for i in range(len(list_s)):
        result += pow(int(list_s[i]) , p_temp)
        p_temp += 1

    if result % n == 0:
        k = result / n
        return k
    else:
        return -1

print(dig_pow(46288, 3))