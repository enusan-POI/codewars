def filter_list(l):
    result = []
    for i in range(len(l)):
        if isinstance(l[i], int):
            result.append(l[i])
    
    return result

