def plus(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(plus(1,2,3,4,5,6,7,8,9,10))
#*args : argument 개수제한이 없는 함수
#argument를 tuple로 받아옴
#keyword 딸린 argument를 넣으면 에러남

def test(**kwargs):
    print(kwargs)

test(hello=True, name="chichoon", family = True)
#**kwargs : argument 개수제한이 없고, keyword와 함께 받아오는 함수
#keyword가 딸려있는 argument를 dictionary로 받아옴
#일반 argument를 넣으면 에러남

#################################################
class Cat():
    def __init__(self, name):
        self.name = name    
        self.animal = True
        self.leg = 4
        self.cute = True
        self.scientific_name = "Felis catus Linnaeus"
        self.color = "cheese"
        #기본 method인 __init__ 재정의
    
    def cry(self):
        #argument로 self가 들어감 - Instance에서 불러와질 때 Instance가 들어가는 자리
        if self.name == "yattong":
            print("yattong")
        else:
            print("meow")
    #cry Method 생성 
#Class 한 개 생성

yattong = Cat("yattong")
yattong.color = "mackerel"
#Instance 하나 생성
samsaek = Cat("samsaek")
samsaek.color = "yellow-black-white"
#Instance 하나 더 생성

yattong.cry()
#yattong instance에서 cry 함수를 사용하면 self에 yattong이 들어간다
samsaek.cry()

print(dir(Cat))
#숨겨진 method들 - __class__, __dict__ 등이 나옴
print(yattong)
#__str__이 호출됨 : instance를 string처럼 불러오려 할때
#이러한 숨겨진 method들은 내가 재정의해서 쓸 수도 있음 
#(__init__ 처럼 instance 생성 시에 동작하도록 재정의 등)
