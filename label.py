#-*-encoding:utf-8-*-
import pandas as pd

#标签的编码
print "begin to read data..."
data = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\data_label.csv',index_col=0)
print "end of read, and start to encoding ..."
for i in range(0,len(data)):
    if(cmp(str(data.ix[i,'label']),"地星量子隐形传态") == 0):
        data.ix[i,'labels'] = '001'
    elif(cmp(str(data.ix[i,'label']),"星地量子密钥分发") == 0):
        data.ix[i,'labels'] = '010'
    elif(cmp(str(data.ix[i,'label']),"星地量子纠缠分发") == 0):
        data.ix[i,'labels'] = '011'
    elif(cmp(str(data.ix[i,'label']),"星地相干通信") == 0):
        data.ix[i,'labels'] = '100'
    else:data.ix[i,'labels'] = '000'
data.drop(['label'],axis= 1,inplace=True)
print "end of encoding, output to the file..."
data.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\data_labels_encode.csv')
print "end of output..."
