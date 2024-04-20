# Câu 1: Tạo  mới 1 list
data = [1,2,3,4,5,6,7,8,9,10]
lst_data=[]

# Câu 2: In ra 5 phần tử đầu tiên của list
print(f"Câu 2: {data[:5]}")

# Câu 3: In ra các phần tử không chia hết cho 2
for i in data:
    if (i % 2) != 0:
        lst_data.append(i)
print(f"Câu 3: {lst_data}")

# Câu 4: In tổng kết quả trong list
sum=0
for i in data:
    sum=sum+i
print (f"Câu 4: {sum}")