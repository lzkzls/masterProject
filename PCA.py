import pandas as pd 
from sklearn.decomposition import PCA 

outputfile = 'C:\Users\Lushan\Desktop\new_own\out\8362_2_pca.csv'
data = pd.read_csv(r"C:\Users\Lushan\Desktop\new_own\2018-8-25\LZK\8362_2.csv",header = 0,index_col = ['RKSJ','CSSJ'])
pca = PCA(n_components = 'mle')
pca.fit(data)
low_dim = pca.transform(data)
pd.DataFrame(low_dim).to_csv(outputfile)
