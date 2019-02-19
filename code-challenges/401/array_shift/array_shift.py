def insert_shift_array(arr, val):
    count = len(arr)
    middle = count // 2
    arr2 = []
    for i in range(count):
        if i != middle:
            arr2.append(arr[i])
        elif i == middle and count % 2 == 1:
            arr2.append(arr[i])
            arr2.append(val)
        else:
            arr2.append(val)
            arr2.append(arr[i])
    return arr2

if __name__ == "__main__":
    array_count = int(input('How many elements in array? '))
    input_array = []

    for i in range(array_count):
        input_array.append(input('Give me a value to put in the original array. '))

    value_to_add = input('What value would you like to add to the array? ')

    print(insert_shift_array(input_array, value_to_add))
