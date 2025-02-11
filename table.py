print("Table of 15")
for i in range(21):
    print('15 * ', str(i),' = ', str(i*15))
color=['red','yellow','green']
num=[1,2,3]
for color, num in zip(color,num):
    print("{}:{}".format(num,color))
A,B= 3,8.93
c=int(B)
sum=A+c
print(sum)
price=57
age=89.0
mesh="eram"
print(type(mesh))
print(type(age))
print(type(price))  `