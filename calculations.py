import timeit
import matplotlib.pyplot as plt
from data_generator import generate_array
from sorts import insertion_sort, merge, merge_sort, tim_sort

# We do not need to generate random lists every time for measures
memo = dict()
def collect_execution_time(method, datasize):
    if datasize in memo:
        datasample = memo[datasize]
    else:
        datasample = generate_array(datasize)
        memo[datasize] = datasample
    setup_code = f"from __main__ import {method.__name__}, generate_array; datasample = generate_array({datasize})"
    execution_time = timeit.timeit(f"{method.__name__}(datasample)", setup=setup_code, number=5)
    return execution_time

# Define size for sorting
n = [2**x for x in range(4, 18)]

# Get execution time for each sort algorithm
timSort = [collect_execution_time(tim_sort, x) for x in n]
print("timSort completed")
insertionSort = [collect_execution_time(insertion_sort, x) for x in n]
print("insertionSort completed")
mergeSort = [collect_execution_time(merge_sort, x) for x in n]
print("mergeSort completed")

# Show plot
plt.figure(figsize=(12, 8))
plt.plot(n, insertionSort, label="InsertionSort")
plt.plot(n, mergeSort, label="MergeSort")
plt.plot(n, timSort, label="TimSort")
plt.xlabel("n")
plt.ylabel("Time, s")
#plt.yscale("log")
plt.title("Sort algorithms comparison")
plt.legend()
plt.grid(True, which="both", ls="--", c='0.65')
plt.show()
