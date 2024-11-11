import random
import time

# Function to count the number of comparisons
comparisons = 0

# Deterministic QuickSort (choosing the first element as pivot)
def deterministic_quick_sort(arr, low, high):
    global comparisons
    if low < high:
        pivot_index = partition(arr, low, high)
        deterministic_quick_sort(arr, low, pivot_index - 1)
        deterministic_quick_sort(arr, pivot_index + 1, high)

# Randomized QuickSort (choosing a random element as pivot)
def randomized_quick_sort(arr, low, high):
    global comparisons
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

# Partition function for deterministic quick sort (choosing the first element as pivot)
def partition(arr, low, high):
    global comparisons
    pivot = arr[low]  # Choosing the first element as pivot
    i = low + 1
    for j in range(low + 1, high + 1):
        comparisons += 1  # Increment comparison count
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# Partition function for randomized quick sort (choosing a random element as pivot)
def randomized_partition(arr, low, high):
    global comparisons
    # Choose a random pivot index and swap it with the first element
    random_pivot_index = random.randint(low, high)
    arr[low], arr[random_pivot_index] = arr[random_pivot_index], arr[low]
    return partition(arr, low, high)

# Function to generate an array of random numbers
def generate_random_array(n):
    return [random.randint(0, 1000) for _ in range(n)]

# Function to analyze the time and number of comparisons for both quick sort variants
def analyze_quick_sort(n):
    global comparisons

    # Generate random array
    arr_deterministic = generate_random_array(n)
    arr_randomized = arr_deterministic[:]
    
    # Analyze Deterministic QuickSort
    comparisons = 0
    start_time = time.time()
    deterministic_quick_sort(arr_deterministic, 0, len(arr_deterministic) - 1)
    deterministic_time = time.time() - start_time
    deterministic_comparisons = comparisons

    # Analyze Randomized QuickSort
    comparisons = 0
    start_time = time.time()
    randomized_quick_sort(arr_randomized, 0, len(arr_randomized) - 1)
    randomized_time = time.time() - start_time
    randomized_comparisons = comparisons

    # Output results
    print(f"Number of elements: {n}")
    print(f"Deterministic QuickSort - Time: {deterministic_time:.6f} seconds, Comparisons: {deterministic_comparisons}")
    print(f"Randomized QuickSort - Time: {randomized_time:.6f} seconds, Comparisons: {randomized_comparisons}")
    print()

# Main function to run the analysis for different input sizes
def main():
    # Take dynamic input for the number of elements
    try:
        n_values = input("Enter the number of elements (comma separated): ")
        n_values = list(map(int, n_values.split(',')))  # Convert input string into a list of integers

        for n in n_values:
            analyze_quick_sort(n)
    except ValueError:
        print("Please enter valid integers for the number of elements.")

if __name__ == "__main__":
    main()
