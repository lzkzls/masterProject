#-*-encoding:utf-8-*-
import pandas as pd

#Z-Score标准化是数据处理的一种常用方法，通过它能够将不同量级的数据转化为统一量度的Z-Score分值进行比较，以保证数据之间的可比性。
data = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8365_data_drop_NanAndRemoveZeroMean.csv',index_col= 0)
print "数据读取完成..."

data1 = data.drop(columns = ['TIME'])

data1 = (data1 - data1.mean(axis=0))/data1.std(axis=0)
data1['TIME'] = data['TIME']

data1.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8365_data_zscore.csv')
print "数据输出结束..."