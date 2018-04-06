#coding=UTF-8
import numpy as ny
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei' #配置中文字体
matplotlib.rcParams['font.size'] = 14   # 更改默认字体大小  
df = pd.read_csv('E:/Python/movie_data/douban.txt',sep = '#',encoding='utf8')
#df_1_cut = df_1[['num','name','director_actor','time','nation','type','score','people','remark']]

df['director_actor'] = df['director_actor'].str.replace('&nbsp;','')#清洗掉不要的字符串

nation_split = df['nation'].str.split(' ').apply(pd.Series)

a = nation_split.apply(pd.value_counts).fillna('0') 
a.columns = ['area_1','area_2','area_3','area_4','area_5']
a['area_1'] = a['area_1'].astype(int)
a['area_2'] = a['area_2'].astype(int)
a['area_3'] = a['area_3'].astype(int)
a['area_4'] = a['area_4'].astype(int)
a['area_5'] = a['area_5'].astype(int)
a = a.apply(lambda x: x.sum(),axis = 1)
area_c = pd.DataFrame(a, columns = ['counts'])
#print(area_c)


type_split = df['type'].str.split(' ').apply(pd.Series)
t = type_split.apply(pd.value_counts)
t = t.unstack().dropna().reset_index()
t.columns = ['level_0','type', 'counts']
type_c = t.drop(['level_0'],axis = 1).groupby('type').sum()
#print(type_c)


director_split = df['director_actor'].str.replace('导演:','').str.split('主演:').apply(pd.Series)
director = director_split[0].str.split('/')
director = director.str[-1].apply(pd.Series)
#df['director_actor'] = director
d = director.apply(pd.value_counts)
d = d.unstack().reset_index()
d.columns = ['level_0','director','counts']
director_c = d.drop(['level_0'],axis = 1).groupby('director').sum()
#print(director_c)

actor_split = df['director_actor'].str.split('主演:')[1:].apply(pd.Series)
actor = actor_split[1].str.split('/')
actor = actor.str[0].apply(pd.Series)
df['director_actor'] = actor
#print(df['director_actor'].value_counts().head(5))

year_split = df['time'].apply(pd.Series)
y = year_split.apply(pd.value_counts)
y = y.unstack().reset_index()
y.columns = ['level_0','year','counts']
year_c = y.drop(['level_0'],axis = 1).groupby('year').sum()
#print(year_c)

#print(df.describe())

#print(df[['num','name']].head(10))

#===============================================================================
# Top10_score_num = df[['score','name']].sort_values(by = ['score'],ascending = False).head(10).reset_index()
# Top10_score_num.index = [1,2,3,4,5,6,7,8,9,10]
# print(Top10_score_num)
#===============================================================================

#===============================================================================
# Top10_comment_num = df[['people','name']].sort_values(by = ['people'],ascending = False).head(10).reset_index()
# Top10_comment_num.index = [1,2,3,4,5,6,7,8,9,10]
# print(Top10_comment_num)
#===============================================================================

#print(df['director_actor'].value_counts().head(11))

#排名与评分的关系
#===============================================================================
# plt.figure(figsize=(14,6)) 
# plt.subplot(1,2,1)
# plt.scatter(df['score'], df['num'])
# plt.xlabel('score')
# plt.ylabel('num')
# plt.gca().invert_yaxis()
# 
# plt.subplot(1,2,2)
# plt.hist(df['score'],bins = 15)
# plt.xlabel('score')
# 
# plt.show()
# print(df['num'].corr(df['score']))
#===============================================================================

#排名与评论人数的关系
#===============================================================================
# plt.figure(figsize=(14,6)) 
# plt.subplot(1,2,1)
# plt.scatter(df['people'], df['num'])
# plt.xlabel('people')
# plt.ylabel('num')
# plt.gca().invert_yaxis()
# 
# plt.subplot(1,2,2)
# plt.hist(df['people'])
# plt.xlabel('people')
# plt.show()
# print(df['num'].corr(df['people']))
#===============================================================================

#排名与上映年份的关系
#===============================================================================
# plt.figure(1)
# plt.figure(figsize=(14,6)) 
# plt.subplot(1,2,1)
# plt.scatter(df['time'], df['num'])
# plt.xlabel('time')
# plt.ylabel('num')
# plt.gca().invert_yaxis()
# plt.subplot(1,2,2)
# plt.hist(df['time'],bins = 30)
# plt.xlabel('time')
# plt.show()
# print(df['num'].corr(df['time']))
#===============================================================================

#出品的地区排名
#===============================================================================
# area_c.sort_values(by = 'counts',ascending = False).plot(kind ='bar', figsize = (12,6))
# plt.show()
#===============================================================================

#电影类型排名
#===============================================================================
# type_c.sort_values(by = 'counts',ascending = False).plot(kind ='bar', figsize = (12,6))
# plt.show()
#===============================================================================