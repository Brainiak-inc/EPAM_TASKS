def correct_brackets(sentence):
    while '()' in sentence or '[]' in sentence or '{}' in sentence:
        sentence = sentence.replace('[]','')
        sentence = sentence.replace('()','') 
        sentence = sentence.replace('{}','') 
    return not sentence


sentence = input('Пожалуйста, введите скобочную последовательность: ')
check = correct_brackets(sentence)
if check == True:
    print('Скобочная последовательность корректная.')
else: 
    print('Скобочная последоватлеьность некорректная.')


input()
