# -*- coding: utf-8 -*-
"""방번호.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PbY2h0ZYP5hF1JlDpkbliJUjuYEzqHJ4

다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)
"""

def finds():
  global cnt 
  z= 0
  while z < len(room_num):
    if room_num[z] in card:
      a = room_num[z]
      card.remove(a)
      room_num.remove(a)

    else :
      for j in range(10):
        if j == 9:
          card.append(6)
        else:
          card.append(j)
      cnt +=1
      finds()
  return cnt

card =[]
room = list(map(int,input()))
room_num=[]
ori = []
cnt = 1

for x in range(10):
  if x == 9:
    card.append(6)
  else:
    card.append(x)
    
ori = card

for y in range(len(room)):
  room_num.append(room[y])
  if room_num[y] == 9:
    room_num[y] = 6
    

a=finds()
print(a)

a = [1,2,3]

b= [4,5,6]

b.append(a)

print(b)