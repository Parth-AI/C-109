import csv
import pandas as pd
import plotly.figure_factory as pff
import statistics

df = pd.read_csv('height-weight.csv')
height_list = df['Height(Inches)'].to_list()
weight_list = df['Weight(Pounds)'].to_list()

h_m = statistics.mean(height_list)
w_m = statistics.mean(weight_list)
h_me = statistics.median(height_list)
w_me = statistics.median(weight_list)
h_mo = statistics.mode(height_list)
w_mo = statistics.mode(weight_list)
h_std = statistics.stdev(height_list)
w_std = statistics.stdev(weight_list)

print(h_m)
print(w_m)
print(h_me)
print(w_me)
print(h_mo)
print(w_mo)
print(h_std)
print(w_std)

h_std_first, h_std_end = h_m - h_std, h_m + h_std
w_std_first, w_std_end = w_m - w_std, w_m + w_std

h_std_sec_s, h_std_sec_e = h_m - (h_std*2), h_m + (h_std*2)

height_l = [result for result in height_list if result > h_std_first and result < h_std_end]
print('{}% of data with in 1 standard deviation'.format(len(height_l) * 100.00/len(height_list)))

weight_l = [result for result in weight_list if result > w_std_first and result < w_std_end]
print('{}% of data with in 1 standard deviation'.format(len(weight_l) * 100.00/len(weight_list)))

height_l1 = [result for result in height_list if result > h_std_sec_s and result < h_std_sec_e]
print('{}% of data with in 2 standard deviation'.format(len(height_l1) * 100.00/len(height_list)))
