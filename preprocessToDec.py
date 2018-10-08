#-*-encoding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
import uniout
import pandas as pd
from pandas import DataFrame
import random
import numpy as np
import re
from pandas.api.types import is_object_dtype

print "读取数据..."
data_raw_1 = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\8365_01.csv',header = 0)
data_raw_2 = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\8365_02.csv',header = 0)
data_raw_3 = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\8365_03.csv',header = 0)
data_raw_4 = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\8365_04.csv',header = 0)
data_raw_5 = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\8365_05.csv',header = 0)
data_raw_6 = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\8365_06.csv',header = 0)
data_raw_7 = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\8365_07.csv',header = 0)
data_raw_8 = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\8365_08.csv',header = 0)
result = [data_raw_1,data_raw_2,data_raw_3,data_raw_4,data_raw_5,data_raw_6,data_raw_7,data_raw_8]
pd.DataFrame(result).to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8365_0108_data.csv')
print "数据合并..."
data_raw = pd.concat(result)
print "数据合并结束..."
# print data_raw.ix[:,1]
# print data_raw[data_raw.columns[1]]

data_obj = {}
format1 = lambda x:repr(x)
format2 = lambda x:int(x,16)
# print data_raw.columns[192]
print "开始处理..."
for col in range(0,data_raw.columns.size):
	# if (cmp(str(data_raw.columns[col]),"RKSJ") == 0 or cmp(str(data_raw.columns[col]),"P0X8356WW244") == 0):
	if (cmp(str(data_raw.columns[col]), "P0X8356WW244") == 0 or cmp(str(data_raw.columns[col]), "P0X8362WW175") == 0
		or cmp(str(data_raw.columns[col]), "P0X8362WW7") == 0 or cmp(str(data_raw.columns[col]), "P0X8365WW137") == 0):
		# data_obj[data_raw.columns[col]] = data_raw.ix[:,col]
		continue
	# if(cmp(str(data_raw.columns[col]),"TIME") == 0 or cmp(str(data_raw.columns[col]),"P0X8356WW244") == 0):
	if (cmp(str(data_raw.columns[col]), "TIME") == 0):
		data_obj[data_raw.columns[col]] = data_raw.ix[:,col]
		continue
	if is_object_dtype(data_raw.ix[:,col].dtype):
		# d1 = data_raw[data_raw.columns[col]].apply(format1)
		print data_raw.columns[col]
		d2 = data_raw[data_raw.columns[col]].map(format2)
		data_obj[data_raw.columns[col]] = d2
		# data_raw = data_raw.drop(data_raw.columns[col],axis = 1)
		# data_raw[data_raw.columns[col]] = d2
		# data_obj[data_raw.columns[col]] = data_raw.ix[:,col]
	else:data_obj[data_raw.columns[col]] = data_raw.ix[:,col]
		
print "处理结束，准备输出...."
data_obj_df = DataFrame(data_obj)
# data_obj_df.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\8356_01_data_obj.csv')
data_obj_df.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8365_data_convert_dec.csv')
print "输出到文件结束..."

# print data_obj_df
# print data_8356['P0X8356WW181'].dtype
# print data_8356['P0X8356WW130'].dtype
# print "打印object数据类型"
# all = data_8356.columns #列索引

#找到object所在的列，正在每一类运用apply




# 十六进制转化为十进制
# data = pd.DataFrame({"a":['00A1','0002','0003','0004'],"b":[5,6,7,9]})
# print data
# format1 = lambda x:long(x,16)
# format2 = lambda x:repr(x)
# d1 = data['a'].apply(format2)
# print "===="
# d2 = data['a'].apply(format1)
# print "===="
# data = data.drop('a',axis = 1)
# data["a"] = d2
# print data
# a = "0xA1"
# print int(a,16)


# data_8356.dtypes.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\8356_dtypes.csv')
# print data_8356['P0X8356WW243'][1957]
# print 'convert'
# print int(data_8356['P0X8356WW243'][1957],16)


		
# print data_8356.dtypes
# print "数据读取结束..."

# print "开始处理十六进制数据..."
# t = int('0x047F',16)
# print (t)
