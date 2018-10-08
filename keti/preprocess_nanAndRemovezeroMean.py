#-*-encoding:utf-8-*-
import pandas as pd

print "开始读取数据..."
data = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8365_data_convert_dec.csv',index_col= 0)
print "数据读取完成..."

print "before delete the nan,the number of rows:",len(data)
data = data.dropna() #删除所有含有缺失值的行
print "after delete the nan,the number of rows:",len(data)
data = data.reset_index(drop = True)
# print len(data.columns)
# print data.columns[224]
count = 0
drop_list = []
for i in range(0,len(data.columns)):
    if (cmp(str(data.columns[i]),"TIME") == 0):
        continue
    if data.iloc[:,i].mean() == 0:
        count += 1
        print "mean is 0: ",data.columns[i]
        drop_list.append(i)
        # data.drop(data.columns[i],axis= 1,inplace= True)#删掉均值为0的列
    if data.iloc[:,i].std() == 0:
        count += 1
        print "std is 0: ",data.columns[i]
        drop_list.append(i)
print count
drop_list = list(set(drop_list))
data.drop(data.columns[drop_list],axis= 1,inplace= True) #删除均值为0的列
data = data.reset_index(drop = True)

# data.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8356_01_data_drop_nan.csv')
data.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8365_data_drop_NanAndRemoveZeroMean.csv')
print "end to output..."

