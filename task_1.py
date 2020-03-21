def sort(array):
    if len(array) < 2:
        return array
    else:
        a = array[0]
        less = [i for i in array[1:] if i <=a ]
        greater = [i for i in array[1:] if i > a]
        return sort(less) + [a] + sort(greater)
number_list = [int(i) for i in input('Введите числа через пробел: ').split(' ')]
sort_array = sort(number_list)
print(sort_array)
input()
