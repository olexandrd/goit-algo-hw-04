import time
import matplotlib.pyplot as plt
from data_generator import generate_array
from sorts import insertion_sort, merge, merge_sort, tim_sort

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
n = [2**x for x in range(4, 27)]

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
