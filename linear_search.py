def linear_search(arr, target):
    # Iterate through each element in the list.
    for i in range(len(arr)):
        # Check if the current element is equal to the target.
        if arr[i] == target:
            # If found, return the index where the target is located.
            return i

    # If the target is not found in the list, return -1 to indicate it wasn't found.
    return -1


# Define the list outside of the function.
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Get input target outside of the function.
target = (input("Enter target No: "))

# Call the linear_search function.
result = linear_search(my_list, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
