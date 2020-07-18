import os


class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
    def intro_self(self):
        print("My name is "+self.name)
class Person():
    def __init__(self, n ,p ,i):
        self.name = n
        self.personality = p
        self.is_sitting = i
    def sit_down(self):
        self.is_sitting = True
    def stand_up(self):
        self.is_sitting = False
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def printvalue(self):
        print("Value print is: ",self.r)
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
x = Bag()
vang = 'vang'
sat = 'sat'
x.add({vang, "10kg"})
x.add({sat, "20Kg"})

class Mapping:
    map = "Map"
    def __init__(self, iterable):
        self.item_list = []
        self.__update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)
    __update = update
M = Mapping(x.data)



class Car:
    def __init__(self, hangxe, tenxe, mausac):
        self.hangxe =   hangxe
        self.tenxe  =   tenxe
        self.mausac =   mausac
    def chayxe(self):
        print("{} dang chay tren duong!".format(self.tenxe))
    def dungxe(self, taisao):
        print(" xe {} dung xe de {}".format(self.tenxe, taisao))
class Toyota(Car):
    tenxe = "Toyota_japan"
    def __init__(self, hangxe,tenxe, mausac, nguyenlieuchinh):
        self.__giaxe = 2000
        super().__init__(hangxe, tenxe, mausac)
        self.nguyenlieuchinh = nguyenlieuchinh
    def chayxe(self):
        print("{} dang chay xe tren duong".format(self.tenxe))
    def dungxe(self):
        print ("{} đang dừng xe để đổ {}".format(self.tenxe, self.nguyenlieuchinh))
    def nomay(self):
        print("{} dang no may!".format(self.tenxe))
    def giaxe(self):
        print("gia xe hien tai la : {}".format(self.__giaxe))
    def changeprice(self, __giaxe):
        self.__giaxe = __giaxe
class Porcher(Car):
    def __init__(self, hangxe,tenxe, mausac, nguyenlieuchinh):
        self.__giaxe = 100000
        super().__init__(hangxe, tenxe, mausac)
        self.nguyenlieuchinh = nguyenlieuchinh
    def chayxe(self):
        print("{} dang chay xe tren duong".format(self.tenxe))
    def dungxe(self):
        print ("{} đang dừng xe để nạp {}".format(self.tenxe, self.nguyenlieuchinh))
    def nomay(self):
        print("{} dang no may!".format(self.tenxe))
    def giaxe(self):
        print("gia xe hien tai la : {}".format(self.__giaxe))
    def changeprice(self, __giaxe):
        self.__giaxe = __giaxe
def kiemtra_dungxe(car): car.dungxe()
toyota = Toyota("Toyota","TuocTOy", "Red", "Xăng")
porsche = Porcher("Porsche", "TuocVipcar", "Blue", "Điện")

# passing the object
kiemtra_dungxe(toyota)
kiemtra_dungxe(porsche)
xpivot = [20, 30, 40]
ypivot = [50, 5 , 1]
x = sum(value*2 for value in range(1180, sum(x*y for x,y in zip(xpivot,ypivot))))
print(x)

dir(os)
os.chdir('E:/Python learning/')
print(os.getcwd())
try: 
    # If the file does not exist, 
    # then it would throw an IOError 
    filename = 'myfile.txt'
    f = open(filename, 'r') 
    text = f.read() 
    print(text)
    f.close() 
  
# Control jumps directly to here if  
#any of the above lines throws IOError.     
except IOError: 
  
    # print(os.error) will <class 'OSError'> 
    print('Problem reading: ' + filename) 