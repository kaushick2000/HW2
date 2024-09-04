import time
import random
import matplotlib.pyplot as plt
import psutil
import platform
import numpy as np

# Insertion Sort
def insertion_sort(array):

    i=1
    while i< len(array):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        i+=1
# Selection Sort
def selection_sort(array):
    n=len(array)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if array[j] < array[min]:
                min = j
        if min != i:
            array[i], array[min] = array[min], array[i]

# Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

# Benchmarking Function
def benchmark(sort_func, sizes):
    times = []
    for size in sizes:
        array = [random.randint(0, 100000) for _ in range(size)]
        start_time = time.time()
        sort_func(array)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# System Information
def system_info():
    print("System Info:")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print(f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    print()

# Main function
def main():
    sizes = [5, 10, 20, 50, 100, 500, 1000, 5000, 10000,15000]

    system_info()

    insertion_sort_times = benchmark(insertion_sort, sizes)
    selection_sort_times = benchmark(selection_sort, sizes)
    bubble_sort_times = benchmark(bubble_sort, sizes)
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, insertion_sort_times, label='Insertion Sort', marker='o')
    plt.plot(sizes, selection_sort_times, label='Selection Sort', marker='o')
    plt.plot(sizes, bubble_sort_times, label='Bubble Sort', marker='o')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Benchmark')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
