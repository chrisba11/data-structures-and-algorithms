array_count = input('How many elements in array?')
input_array = []

for i in range(count):
    input_array.append(int(input('Give me a value to put in the original array')))

value_to_add = input('What value would you like to add to the array?')


def insert_shift_array(arr, val):
    count = len(arr)
    middle = count // 2
    arr2 = []
    for i in range(count):
        if i != middle:
            arr2.append(arr[i])
        else:
            arr2.append(arr[i])
            arr2.append(val)
    return arr2
