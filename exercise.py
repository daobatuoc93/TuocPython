# câu 1:
def cau1(X,Y):
    result = []
    for i in range(X,Y):
        if((i % 7 == 0) & (i % 5 !=0)):
            result.append(i)
    print(result)

def cau2(Giaithua):
    if(Giaithua == 0):
        return 1
    else:
        return Giaithua * cau2(Giaithua-1)
def cau3(args):
    x = dict()
    for i in range(1,args+1):
        x[i]=i*i
    print(x)

def cau4():
    x = input("press something : ")
    n = x.split(",")
    tup = tuple(n)
    print(n)
    print(tup)

# cau 5:
class Cau5:
    def __init__(self):
        self.str = ""
    def getString(self):
        str_user = input("Plz press some thing:")
        self.str = str_user
    def printString(self):
        return self.str.upper()
# cau 6:
def binhphuong(n):
    '''Tra ve gia tri binh phuong cua 1 so'''
    return n**2
# cau 7:

print(binhphuong.__doc__)
# cau 8:
class Person:
    gentle = "man"
    year = 0
    heigh = "1.7"
    def __init__(self, name = ""):
        self.name = name 
       
    def printPerson(self):
        print("name: {} \nold: {}\ngentle: {}\nheigh:{}".format(self.name, self.year, self.gentle, self.heigh))
#  Phần 2 
# câu 9 
# import math
# D = [x for x in input("nhap vao day so:").split(",")]
# x = []
# for i in D:
#     x.append(str(round(math.sqrt((2*50*int(i))/30))))
# result = ','.join(x)
# print(result)
# # câu 10:
# '''using this function to create maxtrix '''
# # make sure you are need to create maxtrix 2
# arr = [int(x) for x in input("nhập vào x,y:").split(',')]

# value = [[x*y for x in range(arr[1])] for y in range(arr[0])]
# print(value)



# câu 11:
'''
Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, 
phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái,
 phân tách nhau bằng dấu phẩy.

Giả sử đầu vào được nhập là: without,hello,bag,world,
thì đầu ra sẽ là: bag,hello,without,world.
'''

# string = [stg for stg in input("Nhap vao chuoi string:").split(",")]
# for i in range(len(string)):
#     for j in range(len(string)):
#         if (string[i] < string[j]):
#             tmp = string[j]
#             string[j] = string[i]
#             string[i] = tmp
# câu 12:
lines = []
while True:
   s = input()
   if (s):
      lines.append(s.upper())
   else:
      break
for sentence in lines:
    print (sentence)