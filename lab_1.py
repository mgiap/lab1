#1.6

def sum_of_two_number(a, b):
    sum = a + b
    print(f"The sum is {sum}")

sum_of_two_number(1, 2)

#1.7

def print_out_array(arr):
    print(f"The array is {arr}")

print_out_array([1, 3, 5, 7, 9])

#1.8

def print_out_maximum_element(arr):
    maximum = 0
    for element in arr:
        if element > maximum:
            maximum = element
    print(f"The maximum element is {maximum}")

print_out_maximum_element([1, 3, 5, 7, 9])

#1.9

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                neutral = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = neutral
    print(f"The sorted array is {arr}")

bubble_sort([5, 9, 1, 3, 7])