x, y = input("Enter a two value: ").split()

x = int(x)
y = int(y)

print("Number of boys: ", x)
print("Number of girls: ", y)

# number array 3 1 5  length - x
arr1 = []

# numbet set 4 2 length - y
arr2 = []

arr1 = input().split()
arr2 = input().split()

print(arr1)
print(arr2)

for i in range(0, x):
    for j in range(0, y):
        # print(arr2[j])
        # print(arr1[i])
        if(int(arr1[i]) > int(arr2[j])):
            temp = arr2[j]
            arr1.insert(i, temp)
            arr2.pop(j)
            x = x+1
            y = y-1


# for X in range(0, len(arr1)-1):         # boys
#     for Y in range(0, len(arr2)-1):     # girls
#         if arr2[Y] < arr1[X]:
#             arr1.insert(Y, arr2[X])
#         else:
#             pass

# for Y in range(0, 1):
#     var = arr2[Y]
#     for X in range(0, 2):
#         if arr1[X] > var:
#             arr1.insert(X, var)

print(arr1)
