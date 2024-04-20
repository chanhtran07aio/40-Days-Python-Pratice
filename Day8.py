# ENUMARATE
# Method 1
shopping_list = ["Kiwi", "Măng cụt", "Sầu riêng"]
print("Danh sách shopping list Method 1:")
for index in range(len(shopping_list)):
    print(f'{index+1}.{shopping_list[index]}')

#Method 2
print("Danh sách shopping list Method 2:")
for index,item in enumerate(shopping_list, start = 1):
    print(f"{index}:{item}")

###########SEARCH##################################
food_list = [
                ["Bơ", "Nho", "Sầu riêng"],
                ["Kiwi", "Táo", "Thơm"],
                ["Cherry", "Măng cụt", "Mãng cầu"]
            ]
# Method 1
print("Search Method 1:")
for i in range(len(food_list)):
    for j in range (len(food_list[i])):
        if food_list[i][j] in shopping_list:
            print(f"{food_list[i][j]} được tìm thấy ở dòng {i+1} và cột {j+1}")

# Method 2
print("Search method 2:")
for i, row in enumerate(food_list, start=1):
    for j, item in enumerate(row, start=1):
        if item in shopping_list:
            print(f"{item} được tìm thấy {i} và cột {j}")