import numpy as np

arr1 = np.random.randint(1, 10, size=(3, 3))
arr2 = np.random.randint(1, 10, size=(3, 3))

print("Array arr1:")
print(arr1)

print("Array arr2:")
print(arr2)

arr1 = np.random.randint(1, 10, size=(3, 3))
arr2 = np.random.randint(1, 10, size=(3, 3))

result = arr1 * arr2

print("The result of multiplication is:")
print(result)

arr1 = np.random.randint(1, 10, size=(3, 3))
arr2 = np.random.randint(1, 10, size=(3, 3))

result = arr1 * arr2
sum_of_elements = np.sum(result)

print("the sum of all elemetns obtained in the array:")
print(sum_of_elements)



import numpy as np

data = np.random.randint(1, 100, size=100)

print("Array data:")
print(data)

data = np.random.randint(1, 100, size=100)

mean_value = np.mean(data)
median_value = np.median(data)
std_deviation = np.std(data)

print("The mean value: ", mean_value)
print("The median: ", median_value)
print("The standart deviation: ", std_deviation)