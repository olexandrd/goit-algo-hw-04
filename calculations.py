import time
import matplotlib.pyplot as plt
from data_generator import generate_array
from sorts import insertion_sort, tim_sort

def merge_sort(arr) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right) -> list:
    merged = []
    left_index = 0
    right_index = 0
    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged

# We do not need to generate random lists every time for measures
memo = dict()
def collect_execution_time(method, datasize=10000):
    if datasize in memo: 
        datasample = memo[datasize]
    else:
        datasample = generate_array(datasize)
        memo[datasize] = datasample
    start_time = time.time()
    _ = method(datasample)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Define size for sorting
n = [2**x for x in range(1, 6)]

# Get execution time for each sort algorithm
timSort = [collect_execution_time(tim_sort, x) for x in n]
insertionSort = [collect_execution_time(insertion_sort, x) for x in n]
mergeSort = [collect_execution_time(merge_sort, x) for x in n]

# Show plot
plt.figure(figsize=(12, 8))
plt.plot(n, insertionSort, label="InsertionSort")
plt.plot(n, mergeSort, label="MergeSort")
plt.plot(n, timSort, label="TimSort")
plt.xlabel("n")
plt.ylabel("Time, s")
plt.yscale("log")
plt.title("Seach algorithms comparison")
plt.legend()
plt.grid(True, which="both", ls="--", c='0.65')
plt.show()
