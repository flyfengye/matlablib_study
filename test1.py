import numpy as np
import pandas as pd

s = pd.Series([1, 3, np.nan, 3])
# print(s)
dates = pd.date_range('20130101', periods=6)
# print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(df)
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
# print(df2)
# print(df2.dtypes)
# df2.<Tab>
# df2.A                  df2.bool
# df2.abs                df2.boxplot
# df2.add                df2.C
# df2.add_prefix         df2.clip
# df2.add_suffix         df2.clip_lower
# df2.align              df2.clip_upper
# df2.all                df2.columns
# df2.any                df2.combine
# df2.append             df2.combine_first
# df2.apply              df2.compound
# df2.applymap           df2.consolidate
# df2.D
# print(df2.A)
# print(df2.abs)

# print(df.sort_index(axis=0, ascending=False))
# print(df.sort_values(by='B'))

# print(df['A'])
# print(df.A)

# print(df[1:4])
# print(df["20130102":"20130104"])

# print(df.loc[dates[1]])
# print(df.loc["20130102"])
# print(df.loc["20130102":])
# print(df.loc["20130102": "20130103"])
# print(df.loc[:, "A"])
# print(df.loc["20130102": "20130103", ['A', 'B']])
# print(df.loc[[dates[1], dates[2]], "A": "B"])
# print(df.loc["20130102", "A": "B"])
# print(df.loc["20130102", "A"])
# print(df.at[dates[0], "A"])

# print(df.iloc[3])
# print(df.iloc[3:5, 0:2])
# print(df.iloc[3:5, 0:2])
# print(df.iloc[[3, 5], [0, 2]])
# print(df.iloc[1:3, :])
# print(df.iloc[:, 1:3])
# print(df.iloc[2, 2])
# print(df.iat[2, 2])


# print(df[df.A > 0])
# print(df[df > 0])

df2 = df.copy()

df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
# print(df2)
# print(df2[df2['E'].isin(['two', 'four'])])

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
# print(s1)
df['F'] = s1  # 新列根据索引自动对齐数据
# print(df)

df.at[dates[0], "A"] = 0
df.iat[0, 1] = 0
# print(df)

# df.loc[:, 'D'] = np.array([5] * len(df))
df.loc[:, 'D'] = [5] * len(df)
# print(df)

df2 = df.copy()
df2[df2 > 0] = -df2
# print(df2)


# np.nan
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
# print(df1)
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)

# df1.dropna(how='any')  # 没用啊删除nan
# print(df1)

# df1.fillna(value=5)  # 没用啊填nan
# print(df1)

# print(pd.isna(df1))

# 操作
