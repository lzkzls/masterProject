#-*-encoding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from sklearn import preprocessing
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import matplotlib.pyplot as plt

# 分类模型，交叉验证准确率，计算准确率、召回率等问题
#在2018年前五个月的数据没有相干通信的的记录（2017年12月之后就没有相干通信了）

print "开始读取数据..."
train_data = pd.read_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\data_labels_encode.csv',index_col=0)
print "数据读入内存..."
target = 'labels'
time_col = 'TIME'
print "各类样本的数量：",train_data['labels'].value_counts()

x_columns = [x for x in train_data.columns if x not in [target,time_col]]
x = train_data[x_columns]
y = train_data['labels']
train_data_columns = x.columns
print "the number of training columns: ",train_data_columns.shape

print "split the training data into training_set and test_set..."
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state= 42)
print "about y_train: ", y_train.value_counts()
print "about y_test: ",y_test.value_counts()

#随机森林
# print "random forest start training ..."
# forest = RandomForestClassifier(n_estimators=3,random_state=0,n_jobs=-1)
# forest.fit(x_train,y_train)
# print "forest fit over ..."
# y_pred = forest.predict(x_test)
# print "forest predict over ..."
# result_label = {"pred":y_pred,"true":y_test}
# pd.DataFrame(result_label).to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\forest_predict_label.csv')
# print "output to the file over..."
# sco = forest.score(x_test,y_test)
# joblib.dump(forest,r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\forest_model.m')
# print "forest,the mean accuracy on the given data is:  ",sco
# print "forest over..."

# importances_forest = forest.feature_importances_
# imp = pd.DataFrame(importances_forest,index = train_data_columns)
# imp.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\forest_feature_importance.csv')
# imp.plot(kind = 'bar',title = "forest feature importance",color = "red",legend = False).set_xticklabels(imp.index)
# print "importance output end ..."

#GBDT
print "gbdt start training ..."
gbdt = GradientBoostingClassifier()
gbdt.fit(x_train,y_train)
print "gbdt fit over..."
y_pred = gbdt.predict(x_test)
print "gbdt predict over ..."
result_label = {"pred":y_pred,"true":y_test}
pd.DataFrame(result_label).to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\GBDT_predict_label.csv')
print "gbdt output to the file over ..."
# sco = gbdt.score(x_test,y_test)

joblib.dump(gbdt,r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\gbdt_model.m')
prec_score = metrics.precision_score(y_test,y_pred,average='weighted')
print "GBDT,the precision on the given data is:  ",prec_score
rec_score = metrics.recall_score(y_test,y_pred,average='weighted')
print "GBDT,the recall on the given data is:  ",rec_score
f1 = metrics.f1_score(y_test,y_pred,average='weighted')
print "GBDT,the f1_score on the given data is:  ",f1
print "gbdt over..."

#feature importance
importances = gbdt.feature_importances_
imp = pd.DataFrame(importances,index = train_data_columns)
imp.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\GBDT_feature_importance.csv')
imp.plot(kind = 'bar',title = "gbdt feature importance",color = "red",legend = False).set_xticklabels(imp.index)
print "importance output end ..."
plt.show()

#模型加载与预测
# model = joblib.load(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\gbdt_model.m')
# pre_result = model.predict(test_set)
# pre_result.to_csv(r'C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\out\pre_result.csv')