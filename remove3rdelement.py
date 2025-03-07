nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
index = 2  

while nums:
    index = index % len(nums)  # Keep index within bounds
    print(nums.pop(index))  # Remove and print the element
    index += 2  # Move to the next third element
