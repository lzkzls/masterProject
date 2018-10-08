#-*-encoding:utf-8 -*-
import pandas as pd
import time

time_initial = time.time()

startTime = time.time()
# data = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8356_01_data_convert_dec.csv')
data = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8365_data_drop_NanAndRemoveZeroMean.csv',index_col= 0)
print("数据读取结束，用时：%fs!"%(time.time()-startTime))

analysis = data.describe(include = "all").T
analysis["null"] = len(data) -analysis["count"]
# analysis.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8356_01_data_analysis_1.csv')
analysis.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\8365_data_drop_NanAndRemoveZeroMean_analysis_1.csv')

print("处理结束，用时： %fs!"%(time.time()-time_initial))