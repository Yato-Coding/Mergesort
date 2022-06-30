from fibonnaci import fib_arr
import time
import os

def merge_sort_fibonacci(fib_arr):
    if len(fib_arr) > 1:
        middle = len(fib_arr)//2
        l = fib_arr[:middle]
        r = fib_arr[middle:]
        merge_sort_fibonacci(l)
        merge_sort_fibonacci(r)
        l_i = arr_i = r_i = 0
        while l_i < len(l) and r_i < len(r):
            if l[l_i] < r[r_i]:
                fib_arr[arr_i] = l[l_i]
                l_i += 1
            else:
                fib_arr[arr_i] = r[r_i]
                r_i += 1
            arr_i += 1
        while l_i < len(l):
            fib_arr[arr_i] = l[l_i]
            l_i +=1
            arr_i += 1
        while r_i < len(r):
            fib_arr[arr_i] = r[r_i]
            r_i += 1
            arr_i += 1

print("Given Array is: ")
print(fib_arr)
time.sleep(2)
os.system("clear")
merge_sort_fibonacci(fib_arr)
print("Sorted Array is: ")
print(fib_arr)


