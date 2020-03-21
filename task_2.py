def search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (high-low)//2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item: 
            low = mid+1
        elif guess > item:
            high = mid - 1
    return None
number_list = [int(i) for i in input('Введите числа через пробел: ').split(' ')]
number = int(input('Введите одно число для поиска в последовательности: '))
search_number = search(number_list, number)
print('Номер введенного вами числа в последовательности:',search_number+1)
input()