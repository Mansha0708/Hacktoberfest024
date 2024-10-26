def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swap was made in this pass
        swapped = False
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps were made, the array is already sorted
        if not swapped:
            break

# Example usage
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", sample_array)
    bubble_sort(sample_array)
    print("Sorted array:", sample_array)
