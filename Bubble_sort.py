
def array_maker():
    array = list()
    while True:
        try:
            size = input("Enter the size of the array: ")
            size = int(size)
            break
        except:
            print("Please Enter the Size for array in Integer")
    i = 0
    while i < size:
        element = (input(f"Enter element at index {i+1}: "))
        try:
            element = int(element)
            array.append(element)
            i+=1
        except ValueError:
            print("Please Enter a Number")
    return array       

def bubble_sort(array):
    for i in range(len(array)):
        for j in range((len(array)-1)-i):
            if array[j] > array[j+1]:
                array[j] = array[j] - array[j+1]
                array[j+1] = array[j+1] + array[j]
                array[j] = array[j+1] - array[j]
    return array

