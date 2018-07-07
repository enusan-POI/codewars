def countBits(n):
    convert_binary = '{0:b}'.format(n)
    str_bin = str(convert_binary)
    list_bin =[]

    for char in str_bin:
        list_bin += char
    
    count_num = 0
    list_bin_lengh = len(list_bin)
    for i in range(list_bin_lengh):
        if list_bin[i] == '1':
            count_num += 1
   
    return count_num

countBits(1234)