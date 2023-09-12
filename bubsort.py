def bubble_sort(arr):
    # Get the length of the array.
    print("Before sorting")
    print(arr)
    print("###########################")
    n = len(arr)

    # Initialize variable swapped to True
    swapped = True

    # Start a while loop that continues until no more swaps are needed
    while swapped:
        # Set swapped to False initially
        swapped = False

        # Iterate through the array from 1st to the last element.
        for i in range(1, n):
            # Compare the current element with the previous one (arr[i - 1] > arr[i])
            if arr[i - 1] > arr[i]:
                # Swap the elements
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

                # Set swapped to True to indicate a swap occurred
                swapped = True
                print(arr)

        # Decrease the length of the array as the largest element is in its correct position
        n -= 1


# Define the input list of numbers
numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Call the bubble_sort function to sort the list
bubble_sort(numbers)

# Print the sorted array
print("Final Sorted Array:", numbers)
