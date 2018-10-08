#-*-encoding:utf-8-*-
import pandas as pd
import numpy as np
from math import isnan

data = pd.read_csv('C:\\Users\\Lushan\\Desktop\\new_own\\2018-8-25\\LZK\\out\\foreLabel_change.csv')
# print data.dtypes
pd.set_option('display.max_rows', None)
data1 = data[['DATE','START','END','EXPERIMENTTYPE']]
# print data1
data = data1.dropna(how='all')
data = data.reset_index(drop = True)
# print data
# data.to_csv('C:\\Users\\Lushan\\Desktop\\new_own\\2018-8-25\\LZK\\out\\foreLabeldontknow.csv')
# print data.dtypes
# print np.isnan(data.iloc[7,2])
count = 0
# print len(data)
# print data.ix[:,1]
#填充DATE
for i in range(0,len(data)):
    if str(data.iloc[i,0]) == 'nan':
        count += 1
        data.iloc[i, 0] = data.iloc[i-1,0]
        print i

print data
#填充其他时间列，两列拼接成1列
# data['start_time'] = str(data['DATE']) + str(data['START'])
# data['end_time'] = str(data['DATE']) + str(data['END'])

# for i in range(0,len(data)):
#     if str(data.iloc[i, 1]) == 'nan':
#         data.drop([i], inplace=True)
#         print "i is:%d",i
#         print "drop"
data.to_csv('C:\\Users\\Lushan\\Desktop\\new_own\\2018-8-25\\LZK\\out\\foreLabel_addDate.csv')
print "end..."