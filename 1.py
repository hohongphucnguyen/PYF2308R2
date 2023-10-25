import random
current_number = 0
current_player = random.randint(0,1)
while current_number <= 30:
     print(current_number)
    
     if current_player == 0:
          player_choice  = int(input(' sự lựa chọn của bạn '))
          current_number += player_choice
          print(current_number)
          for player_choice in [1,2,3]:
               continue
          if current_number >= 30 :
            print(' bạn thua ')
            break
          else:
            player_choice = random.randint(1,3)
            print(f' máy chọn {player_choice}')
            current_number += player_choice
            if current_number >= 30:
                print(' bạn đã thắng ')
                break
        

     else:
          player_choice  = random.randint(1,3)
          print(f' máy đã chọn {player_choice}')
          current_number += player_choice
          print(current_number)
          if current_number >= 30:
              print(' bạn đã thắng ')
              break
          else:
            player_choice = int(input(' sự lựa chọn của bạn '))
            for player_choice in [1,2,3]:
               continue
            current_number += player_choice
            if current_number >= 30:
                print('bạn đã thua ')
                break

          