import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('covid19.csv',encoding='cp949')
print(df)

indexWoman = df[df['gubun']=='여성'].index
indexman = df[df['gubun']=='남성'].index
df.drop(indexman,inplace=True )
df.drop(indexWoman,inplace=True )
print('droped df\n',df)

print(len(indexWoman))
print(len(indexman))
print(indexWoman)
print(indexman)

print(len(df))

indexage = df[(df['gubun']=='20-29') | (df['gubun']=='30-39')]
indexage_i = df[(df['gubun']=='20-29') | (df['gubun']=='30-39')].index

df_new = df.sort_values('createDt')

sns.countplot(x='confcase', data=df_new)
plt.show()
