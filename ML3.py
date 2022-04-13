# การใช้ Tuple จะต่างกับลิสต์


# การสร้าง Tuple จาก list
a = (1,2,3,4,5)
list = [1,2,3,4]
b = tuple(list)
c = tuple([1,2,3,4,5])
d = (1,) # ถ้าสมาชิกใน tuple มีตัวเดียวจะต้องใส่ , ตามหลัง
print(*d)

# การเข้าถึงสมาชิกของ tuple
num = (2 , 4 , 6 , 8 , 10)
print(num[0])  # 2
print(num[1])  # 4
print(num[2])  # 6
print(*num)  # 2 4 6 8 10
