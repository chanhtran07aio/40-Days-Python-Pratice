# List
# Câu 1
lst_data=[]
for i in range(1,13):
    if i % 2 ==0:
        lst_data.append(i)
print (f'Câu 1: {lst_data}')

# Câu 2
for i in lst_data:
    if i%3 == 0:
        lst_data.remove(i)
print(f'Câu 2: {lst_data}')

# Câu 3: Thêm vào cuối danh sách 1->3 và vị trí số 3 6->8
for i in range(1,4):
    lst_data.append(i)
lst_data[3:3] = (6,7,8)
print(f'Câu 3: {lst_data}')

# Câu 4: Nếu các số trong lst_data chia hết cho 2 hoặC chia hết cho 5 thì cập nhật thành số 0
for i in lst_data:
    if lst_data[i] % 2 == 0 or lst_data[i] % 5==0:
        lst_data[i] = 0
print(f'Câu 4: {lst_data}')