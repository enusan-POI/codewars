def openOrSenior(data):
    # Hmmm.. Where to start?
    data_size = len(data)
    result_list = []
    for i in range(data_size):
        age = data[i][0]
        handicap = data[i][1]
        if age >= 55:
            if handicap > 7:
                result_list.append('Senior')
            else:
                result_list.append('Open')             
        else:
            result_list.append('Open')

    return result_list

openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]])