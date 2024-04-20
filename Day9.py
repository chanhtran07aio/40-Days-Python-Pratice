# List - Median
# Cau 1
lst_data = []
for data in range(1,11):
    lst_data.append(data)
print(f"Cau 1: {lst_data}")

# Cau 2
# Step 1: Sort list
lst_data = [10,2,3,4,5,6,7,8,9,1]
for i in range(len(lst_data)):
    for j in range(len(lst_data)-i-1):
        if lst_data[j] > lst_data[j+1]:
            lst_data[j], lst_data[j+1] = lst_data[j+1] , lst_data[j]
#print(f"Sort list: {lst_data}")

# Step 2: Tinh median
index = len(lst_data)
if index % 2 == 0:
    m = int(index/2)
    n = m-1
    #print(f'm={m} va n={n}')
    median = (lst_data[m] + lst_data[n])/2
else:
    m = int(index/2)
    median = lst_data[m]

print(f"Cau 2: Median: {median}")

# Cau 3
lst_odd_filter = []
for i in range(len(lst_data)):
    if lst_data[i] % 2 != 0:
        lst_odd_filter.append(lst_data[i])
lst_odd_filter = lst_odd_filter[::-1]
print(f"Cau 3: {lst_odd_filter}")
