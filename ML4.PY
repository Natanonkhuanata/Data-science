# Dictionary
contries = {'th':'Thailand' , 'jp':'Japan' , 'kr':'korea'}
My = {'name':'natanon' , 'nickname':'khuanta' , 'hight':177 , 'single':True}
range = {'range1':range(0,5) , 'range2':range(1,5) , 'range3':range(2,5)}
list = {'1':[1,2,3,4,5] , '2':[2,3,4,5,6] , '3':[3,4,5,6,7,8]}


# การอ้างอิงถึงข้อมูลภายในลิสต์

contries = {'th':'Thailand' , 'jp':'Japan' , 'kr':'korea'}
print(contries['th'])
print(contries['jp'])

# สมาชิกเป็นลิสต์

num = {'list1':[1,2,3,4] , 'list2':[2,3,4,5,6]}
print(num['list1'])
print(num['list2'][2]) # 4

