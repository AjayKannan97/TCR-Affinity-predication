import numpy as np
import pickle
import pandas as pd  
#import torch 
from pprint import pprint

data = pd.read_pickle('TCR_epitope_embedding_data.pkl')


df_emb = data[['epi','tcr','epi_embeds','tcr_embeds','binding']]#.sample(frac=1,random_state=1).reset_index()
#print(df_emb.head())
#print(df_emb['binding'].value_counts())
#df_emb = df_emb[df_emb['binding'] == 0]

counts = df_emb['epi'].value_counts().index.tolist()
print(counts[0])
d = df_emb.loc[(df_emb['epi']=='KLGGALQAK')]
for i in range(1,len(counts)):
    d = pd.concat([d,df_emb.loc[(df_emb['epi']==counts[i])]])
d = d.reset_index()
d = d[['epi','tcr','epi_embeds','tcr_embeds','binding']]

df_emb = d.to_dict()
print(len(df_emb['epi']))
print(d)

i = 0
d2 = {}
while i < 429078*20:
    i+=1
    d_1 = d.sample(1)
    d_2 = d.sample(1)
    if d_1.iloc[0]['tcr'] == d_2.iloc[0]['tcr'] or d_1.iloc[0]['epi'] == d_2.iloc[0]['epi'] or len(d_1.iloc[0]['tcr']) > len(d_2.iloc[0]['tcr']):
        i -= 1
        continue
    x = d_1.iloc[0]['tcr']
    y = d_2.iloc[0]['tcr']
    if (x,y) not in d2:
        if i % 1000 == 0:
            print(i)
        d2[(x,y)] = [d_1.iloc[0]['tcr_embeds'],d_2.iloc[0]['tcr_embeds'],0]
    else:
        i -= 1
    
tcr_pair1 = pd.DataFrame(d2).T.reset_index().rename(columns={'level_0':'tcr1','level_1':'tcr2',0:'tcr_embeds1',1:'tcr_embeds2',2:'binding'})
print(tcr_pair1)

tcr_pair1.to_pickle('TCR_pair_embedding_data_long.pkl')