#!/usr/bin/env python

import pandas as pd

filename = 'seoul.csv'
df = pd.read_csv(filename)
print(df)


result = df.loc[df['시군구'].str.lstrip() == '서울특별시 강남구 신사동']
print(result)

result = df.loc[(df['시군구'].str.strip() == '서울특별시 강남구 신사동') & (df['단지명']== '삼지')]
print(result)

newdf = df.set_index(keys=['도로명'])
print(newdf)
result = newdf.loc['언주로']
count = newdf.loc['언주로'].count()
# count = len(newdf.loc['언주로'])
print(result)
print('count :', count)