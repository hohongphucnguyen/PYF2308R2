sotien = float(input(' hãy nhập số tiền đã chi tại cửa hàng ($)'))
giam15 = sotien - 15
giam25 = sotien - 25
giam50 = sotien - 50
if sotien < 75 :
    print(' bạn ko được giảm giá ')
elif sotien < 100 :
    print(f'bạn sẽ được giảm giá 15$ và tổng số tiền bạn phải trả là {giam15}')
elif sotien < 150 :
    print(f'bạn sẽ được giảm giá 25$ và tổng số tiền bạn phải trả là {giam25}')
else :
    print(f'bạn sẽ được giảm giá 50$ và tổng số tiền bạn phải trả là {giam50}')
