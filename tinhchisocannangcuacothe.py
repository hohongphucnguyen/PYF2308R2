chieucao = int(input(' hãy nhập chiều cao của bạn (cm) '))/100
cannang = int(input(' hãy nhập cân năng của bạn (kg) '))
BMI = cannang / (chieucao ** 2 )
if BMI < 16 :
    print(' gầy cấp độ iii ')
elif BMI < 17 :
    print(' gầy cấp độ ii ')
elif BMI < 18.5 :
    print(' gầy cấp độ i ')
elif BMI < 25 :
    print(' bình thường ')
elif BMI < 30 :
    print(' thừa cân ')
elif BMI < 35 :
    print(' béo phì cấp độ i ')
elif BMI < 40 :
    print(' béo phì cấp độ ii ')
else :
    print(" béo phì cấp độ iii ")
