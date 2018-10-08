#-*-encoding:utf-8-*-
import pandas as pd
import time
import datetime

#链接不同的包的数据；
# print "读取数据..."
# data1 = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8362_data_zscore.csv',index_col= 0)
# data2 = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8356_data_zscore.csv',index_col= 0)
# data3 = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8365_data_zscore.csv',index_col= 0)
# print "数据读取结束..."
#
# print "开始merge..."
# data1['TIME'] = pd.to_datetime(data1['TIME'],format = "%Y-%m-%d %H:%M:%S")
# data2['TIME'] = pd.to_datetime(data2['TIME'],format = "%Y-%m-%d %H:%M:%S")
# data3['TIME'] = pd.to_datetime(data3['TIME'],format = "%Y-%m-%d %H:%M:%S")
#
# data = pd.merge(data1,data2,on = 'TIME',how= "inner",sort = True)
# data = pd.merge(data,data3,on = 'TIME',how= "inner",sort = True)
# print "merge结束，开始输出..."
#
# data.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\raw_data_link.csv')
# print "输出结束..."

data = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\raw_data_link.csv',index_col=0)
data['TIME'] =  pd.to_datetime(data['TIME'],format = "%Y-%m-%d %H:%M:%S")

#链接数据和标签
# print "label准备..."
# label_date_row = pd.read_csv('C:\\Users\\Lushan\\Desktop\\new_own\\2018-8-25\\LZK\\out\\foreLabel_delete_changeTime.csv',index_col= 0)
# label_date = label_date_row[['start_time','end_time','EXPERIMENTTYPE']]
# label_date['start_time'] = pd.to_datetime(label_date['start_time'],format = "%Y-%m-%d %H:%M:%S")
# label_date['end_time'] = pd.to_datetime(label_date['end_time'],format = "%Y-%m-%d %H:%M:%S")
# drop_list = []
# for i in range(0,len(label_date)):
#     if(cmp(str(label_date.iloc[i,2]),"地星量子隐形传态") == 0 or cmp(str(label_date.iloc[i,2]),"星地量子密钥分发") == 0
#        or cmp(str(label_date.iloc[i,2]),"星地量子纠缠分发") == 0 or cmp(str(label_date.iloc[i,2]),"星地相干通信") == 0):
#         continue
#     else:
#         drop_list.append(i)
#
# label_date.drop(label_date.index[drop_list],inplace = True)
# label_date = label_date.reset_index(drop=True)
# label_date.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\label_to_link.csv')
# print "label准备完成..."



label_date = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\label_to_link.csv',index_col=0)
label_date['start_time'] = pd.to_datetime(label_date['start_time'],format = "%Y-%m-%d %H:%M:%S")
label_date['end_time'] = pd.to_datetime(label_date['end_time'],format = "%Y-%m-%d %H:%M:%S")

print "开始链接..."
for i in range(0,len(data)):
    print "i is: ",data.ix[i,'TIME']
    ts1 = time.strptime(str(data.ix[i,'TIME']),"%Y-%m-%d %H:%M:%S")
    time_stamp1 = time.mktime(ts1)
    for j in range(0,len(label_date)):
        print "j is: ",label_date.ix[j,'start_time']
        print "j is: ", label_date.ix[j, 'end_time']
        ts2 = time.strptime(str(label_date.ix[j,'start_time']),"%Y-%m-%d %H:%M:%S")
        time_stamp2 = time.mktime(ts2)
        ts3 = time.strptime(str(label_date.ix[j,'end_time']),"%Y-%m-%d %H:%M:%S")
        time_stamp3 = time.mktime(ts3)
        if((time_stamp1-time_stamp2) >= 0.0 and (time_stamp3-time_stamp1)>=0.0):
            print "true,",i,"and",j
            data.ix[i, 'label'] = label_date.ix[j, 'EXPERIMENTTYPE']
        print "next"
        # if (data.ix[i,'TIME'] >= label_date.ix[j,'start_time'] and data.ix[i,'TIME'] <= label_date.ix[j,'end_time'] ):
        #     print "true,",i,"and",j
        #     data.ix[i,'label'] = label_date.ix[j,'EXPERIMENTTYPE']
print "链接结束..."
data.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\data_label.csv')
print  "输出到文件结束..."

#使用label_data来进行数据融合
# print label_date


