def search_word(sentence):
    word_list = []
    for word in sentence.split():
        word_1 = ''
        for letter in word:
            if letter.isalpha(): 
                word_1 += letter.lower()
        word_list.append(word_1)
    word_list_d = {}.fromkeys(word_list, 0)
    for i in word_list:
        word_list_d[i]+=1
    rd = {}
    for i, j in word_list_d.items():
        rd[j] = rd.get(j, []) + [i]
    return rd.get(1)

sentence = 'Words, different words. Even even; morE woRds'
print('В тексте по одному разу встречаются следующие слова:',search_word(sentence)) 