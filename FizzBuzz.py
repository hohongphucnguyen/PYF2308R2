hai_so = (input(' nhập vào hai số: '))
tach = hai_so.split(',')
for i in range(len(tach)):
    tach[i] = int(tach[i])
if tach[-1] <= tach[0]: 
    print(' số kết thúc cần lớn hơn số bắt đầu ')
else:
    for x in range(tach[0] +1, tach[-1]):
        if x % 3 ==0 and x % 5 == 0:
            print(x,'FizzBuzz')
        elif x % 3 == 0:
            print(x,'Fizz')
        elif x % 5 == 0:
            print(x,'Buzz')
        else:
            print(x)