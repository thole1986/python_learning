from typing import MutableSequence

def insertion_sort(data: MutableSequence):

    for first_unsorted_index in range(1, len(data)):
        print("first_unsorted_index", first_unsorted_index)
        new_element = data[first_unsorted_index]
        print("new_element: ", new_element)
        i = first_unsorted_index - 1
        print("I: ", i)
        while i >=0 and data[i] > new_element:
            data[i + 1] = data[i]
            i -= 1
            print("While i: ", i)
        
        data[i + 1] = new_element

        print(f"End of pass {first_unsorted_index}. `data` is now {data}")



if __name__ == '__main__':
    from array import array
    numbers = array('i', [20, 35, -15, 7, 55, 1, -22])

    print(f"Sorting {numbers}")
    insertion_sort(numbers)
    print(f"The sorted data is {numbers}")
