def spin_words(sentence):
    # Your code goes here
    words = sentence.split()
    words_list_len = len(words)
    new_sentence = []
    for i in range(words_list_len):
        if len(words[i]) >= 5:
            temp = words[i][::-1]
            new_sentence.append(temp)
            new_sentence.append(' ')
        else:
            new_sentence.append(words[i])
            new_sentence.append(' ')
    

    str1 = ''.join(new_sentence)
    return str1

