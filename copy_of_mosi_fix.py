# -*- coding: utf-8 -*-
"""Copy of mosi fix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p6pflc3PtHwPesz5ZmN2rldLhNL4ZIsk
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import copy
from google.colab import files
# %matplotlib inline

x_v = []
y_v = []
covid_v = []
color = {
    "0":'b',
    "1":'r'
}
walker = 100
for i in range(walker):
  x_v.append(random.randint(0,20))
  y_v.append(random.randint(0,20))
  covid_v.append("0")
#create virus
x_v.append(int(np.median(x_v)))
y_v.append(int(np.median(y_v)))
covid_v.append("1")
for i in range(walker+1):
  plt.scatter(x_v[i],y_v[i],color=color[covid_v[i]])
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Uninfected',
                          markerfacecolor='b',markersize = 10),
                      Line2D([0], [0], marker='o', color='w', label='Infected',
                          markerfacecolor='r',markersize = 10),
                      Line2D([0], [0], marker='.', color='w', label='Footsteps',
                          markerfacecolor='r',markersize = 10)]
plt.legend(handles=legend_elements,loc='best')
plt.xlim(-1,30)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

x = copy.deepcopy(x_v)
y = copy.deepcopy(y_v)
covid = copy.deepcopy(covid_v)
print(covid)

step = 0.3
hari = 61
graph = []
days = []
history =[[x[len(x)-1], y[len(y)-1]]]
print(history)
all_infected_loop = 0
count = 0

for j in range(hari):
  for i in range(walker):
    dec = random.randint(1,4)
    if(dec == 1):
        if (x[i] == 0 or x[i] == 20):
          x[i] = random.randint(0,20)
        elif (x[i]>0 and x[i]<20):
          x[i] = x[i]+step
        
    elif(dec == 2):
        if (x[i] == 0 or x[i] == 20):
          x[i] = random.randint(0,20)
        elif (x[i]>0 and x[i]<20):
          x[i] = x[i]-step
        
    elif(dec == 3):
        if (y[i] == 0 or y[i]==20):
          y[i] = random.randint(0,20)
        elif (y[i]>0 and y[i]<20):
          y[i] = y[i]+step
        
    elif(dec == 4):
        if (y[i] == 0 or y[i] == 20):
          y[i] = random.randint(0,20)
        elif (y[i]>0 and y[i]<20):
          y[i] = y[i]-step
    cek = [c for c, e in enumerate(covid) if e == "1"]
    for l in range(len(cek)):
      if (x[i] == x[cek[l]] and y[i]==y[cek[l]]):
        covid[i] = "1"
        jalur = [x[i],y[i]]
        history.append(jalur)
        count = count + 1
        break
      else:
        pass
    for z in range(len(history)):
      if(x[i] == history[z][0] and y[i] == history[z][1]):
        covid[i] = "1"
        count = count + 1
  for k in range(walker+1):
    plt.scatter(x[k],y[k],color=color[covid[k]])
    
  for h in range(len(history)):
    plt.scatter(history[h][0], history[h][1], color="grey", marker=".")
  day = j+1
  days.append(day)
  plt.title('Day '+str(day))
  plt.xlim(-1,30)
  legend_elements = [Line2D([0], [0], marker='o', color='w', label='Uninfected',
                          markerfacecolor='b',markersize = 10),
                      Line2D([0], [0], marker='o', color='w', label='Infected',
                          markerfacecolor='r',markersize = 10),
                      Line2D([0], [0], marker='.', color='w', label='Footsteps',
                          markerfacecolor='grey',markersize = 10)]
  plt.legend(handles=legend_elements,loc='best')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.savefig('./Day_'+str(day)+'.png')
  files.download('Day_'+str(day)+'.png') 
   
  plt.show()
  cov = [int(i) for i in covid]
  cov.sort(reverse=True)
  print(cov)
  cov_counter = cov.count(1)
  print("ini yang count covid", cov_counter)
  graph.append(cov_counter)

  if (cov_counter == walker+1):
    all_infected_loop = all_infected_loop + 1
    if (all_infected_loop == 3):
      break 


print("counter", graph)
print("days leng", len(days))
print("counter len", len(graph))

x = days
y = graph
plt.plot(x,y)
plt.title('Kasus Covid 19')
plt.xlabel("Hari")
plt.ylabel("Total Terinfeksi")
plt.savefig('hasil_graph.png')
files.download('hasil_graph.png')

# step = 2
# # dec = []
# # for j in range (50*walker):
# #   arah = random.randint(1,4)
# #   dec.append(arah)
# print(dec)
# print(len(dec))
# array_titik = []
# for i in range (len(x)):
#   titik = [x[i],y[i]]
#   array_titik.append(titik)
# print(array_titik)
# print("len arr ", len(array_titik))

# for i in range(len(dec)):
#   for j in range(len(array_titik)-1):
#     if(dec[i] == 1):
#       if(array_titik[j][0] >= 0 and array_titik[j][0] < 20):                       # ini X nya yak
#         array_titik[j][0] = array_titik[j][0] + step
#       elif(array_titik[j][0] >=20):
#         array_titik[j][0] = array_titik[j][0] #stay
#       if (array_titik[j][0] == x[len(x)-1] and array_titik[j][1]==y[len(y)-1]):
#         covid[j] = "1"
#       array_titik[i] = array_titik[i]

#     elif(dec[i] == 2):
#       if(array_titik[j][0] <= 20 and array_titik[j][0] > 0):                       # ini X nya yak
#         array_titik[j][0] = array_titik[j][0] - step
#       elif(array_titik[j][0] <= 0):
#         array_titik[j][0] = array_titik[j][0] #stay
#       if (array_titik[j][0] == x[len(x)-1] and array_titik[j][1]==y[len(y)-1]):
#         covid[i] = "1"

#     elif(dec[i] == 3):
#       if(array_titik[j][1] >= 0 and array_titik[j][1] <20):                       # ini Y nya yak
#         array_titik[j][1] = array_titik[j][1] + step
#       elif(array_titik[j][1] >= 20):
#         array_titik[j][1] = array_titik[j][1] #stay
#       if (array_titik[j][0] == x[len(x)-1] and array_titik[j][1]==y[len(y)-1]):
#         covid[i] = "1"

#     elif(dec[i] == 4):
#       if(array_titik[j][1] <= 20 and array_titik[j][1] > 0):                       # ini Y nya yak
#         array_titik[j][1] = array_titik[j][1] - step
#       elif(array_titik[j][1] <= 0):
#         array_titik[j][1] = array_titik[j][1] #stay
#       if (array_titik[j][0] == x[len(x)-1] and array_titik[j][1]==y[len(y)-1]):
#         covid[i] = "1"
#   print(covid)
#   print(len(covid))
#   for k in range(walker+1):
#     plt.scatter(array_titik[k][0],array_titik[k][1],color=color[covid[k]])
#   plt.xlim(-1,21)
#   plt.ylim(-1,21)
#   plt.xlabel('X')
#   plt.ylabel('Y')
#   plt.show()

# step = 2
# for j in range(50):
#   dec = random.randint(1,4)
#   if(dec == 1):
#     for i in range(len(x)-1):
#       if (x[i] == 0):
#         x[i] = x[i]+step
#       elif (x[i]>0 and x[i]<20):
#         x[i] = x[i]+step
#       elif(x[i] >= 20):
#         x[i] = x[i]+0
#       if (x[i] == x[len(x)-1] and y[i]==y[len(y)-1]):
#         covid[i] = "1"
#       else:
#         covid[i] = covid[i]
#   elif(dec == 2):
#     for i in range(len(x)-1):
#       if (x[i] == 0):
#         x[i] = x[i]+step
#       elif (x[i]>0 and x[i]<=20):
#         x[i] = x[i]-step
#       # elif(x[i] == 20):
#       #   x[i] = x[i]-step
#       if (x[i] == x[len(x)-1] and y[i]==y[len(y)-1]):
#         covid[i] = "1"
#       else:
#         covid[i] = covid[i]
#   elif(dec == 3):
#     for i in range(len(y)-1):
#       if (y[i] == 0):
#         y[i] = y[i]+step
#       elif (y[i]>0 and y[i]<20):
#         y[i] = y[i]+step
#       elif(y[i >= 20]):
#         y[i] = y[i]+0
#       if (x[i] == x[len(x)-1] and y[i]==y[len(y)-1]):
#         covid[i] = "1"
#       else:
#         covid[i] = covid[i]
#   elif(dec == 4):
#     for i in range(len(y)-1):
#       if (y[i] == 0):
#         y[i] = y[i]-0
#       elif (y[i]>0 and y[i]<=20):
#         y[i] = y[i]-step
#       elif(y[i > 20]):
#         y[i] = y[i]-0
#       if (x[i] == x[len(x)-1] and y[i]==y[len(y)-1]):
#         covid[i] = "1"
#       else:
#         covid[i] = covid[i]
#   print(dec)
#   for k in range(walker+1):
#     plt.scatter(x[k],y[k],color=color[covid[k]])
#   plt.xlim(-1,21)
#   plt.ylim(-1,21)
#   plt.xlabel('X')
#   plt.ylabel('Y')
#   plt.show()

print(covid)

array_titik = []
for i in range (len(x)):
  titik = [x[i],y[i]]
  array_titik.append(titik)
print(array_titik)

step = 1
arr_dec = []
for l in range (50):
  for i in range(len(array_titik)-1):
    arah = [1,2,3,4]
    dec = random.choice(arah)
    # print(dec)
    arr_dec.append(dec)
    if (arr_dec[i] == 1):
      if(array_titik[i][0] >= 0 and array_titik[i][0] <20):
        array_titik[i][0] = array_titik[i][0] + step
      elif (array_titik[i][0] >= 20):
        array_titik[i][0] = random.randint(1,19) #stay
      cek = [i for i, e in enumerate(covid) if e == "1"]
      # for j in range(len(cek)):
      #   if (covid[cek[j]] != covid[i]):
      #     covid[i] = "1"
      #     break
      #   else:
      #     pass
      # print(array_titik[i])
    elif (arr_dec[i] == 2):
      if(array_titik[i][0] <=20 and array_titik[i][0] >0):
        array_titik[i][0] = array_titik[i][0] - step
      elif(array_titik[i][0] <= 0):
        array_titik[i][0] = random.randint(1,19) #stay
      cek = [i for i, e in enumerate(covid) if e == "1"]
      # for j in range(len(cek)):
      #   if (covid[cek[j]] != covid[i]):
      #     covid[i] = "1"
      #     break
      #   else:
      #     pass
      # print(array_titik[i])
    elif (arr_dec[i] == 3):
      if(array_titik[i][1] >= 0 and array_titik[i][1] <20):
        array_titik[i][1] = array_titik[i][1] + step
      elif(array_titik[i][1] >= 20):
        array_titik[i][1] = random.randint(1,19)
      cek = [i for i, e in enumerate(covid) if e == "1"]
      # for j in range(len(cek)):
      #   if (covid[cek[j]] != covid[i]):
      #     covid[i] = "1"
      #     break
      #   else:
      #     pass
      # print(array_titik[i])
    elif (arr_dec[i] == 4):
      if(array_titik[i][1] >0 and array_titik[i][1] <= 20):
        array_titik[i][1] = array_titik[i][1] - step
      elif(array_titik[i][1] <= 0):
        array_titik[i][1] = random.randint(1,19)
      cek = [i for i, e in enumerate(covid) if e == "1"]
      # for j in range(len(cek)):
      #   if (covid[cek[j]] != covid[i]):
      #     covid[i] = "1"
      #     break
      #   else:
      #     pass
      # print(array_titik[i])
  for k in range(walker+1):
    plt.scatter(array_titik[k][0],array_titik[k][1],color=color[covid[k]])
    # plt.scatter(history_virus[k][0], history_virus[k][1], color="red")
  plt.xlim(-1,21)
  plt.ylim(-1,21)
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.show()

print(covid)