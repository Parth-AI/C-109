from random import randint
import statistics
import plotly.figure_factory as pff

dice = []

for i in range(0,1000):
     dice1 = randint(1,6)
     dice2 = randint(1,6)
     dice.append(dice1 + dice2)

mean = sum(dice)/len(dice)
print(mean)
std = statistics.stdev(dice)
print(std)
me = statistics.median(dice)
mo = statistics.mode(dice)
print(me)
print(mo)

st = []
for j in range(0,1000):
     first_std_start, first_std_end = mean - std, mean + std
     second_std_start, second_std_end = mean - (std*2), mean + (std*2)
     st.append((first_std_start + first_std_end) - (second_std_start + second_std_end))
print('{}% of data with in 1 standard deviation'.format(len(st) * 100.00/len(dice)))

fig = pff.create_distplot([dice], ['Dice'], show_hist = False)
fig.show()
