def alphabet_position(text):
    replaced_list = []
    for i in range(len(text)):
        '''조건문이 숫자인지 체크하는게 아닌, 알파벳(아스키 코드 범위) 내인지 확인할것'''
        if((text[i].lower()).isdigit()):
            continue
        else:
            replaced_list.append(str(ord(text[i].lower())))

    str1 = ''.join(replaced_list)

    return str1