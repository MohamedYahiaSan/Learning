import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file=open('data.txt','w')

test=pd.Series(np.random.randint(0,100,10))

dates=pd.date_range('20240301', periods=10)
file.write(str(dates))
file.write('\n\n')


df=pd.DataFrame(np.random.randint(0,100,40).reshape(10,4),index=dates,columns=list('ABCD'))
file.write(str(df))
file.write('\n\n')

file.write(str(df.dtypes))
file.write('\n\n')

file.write(str(df.head()))
file.write('\n\n')

file.write(str(df.tail()))
file.write('\n\n')

file.write(str(df.index))
file.write('\n\n')

file.write(str(df.columns))
file.write('\n\n')

file.write(str(df.to_numpy()))
file.write('\n\n')

file.write(str(df.describe()))
file.write('\n\n')


df2 = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

file.write(str(df2))
file.write('\n\n')

x=df2.groupby(["A","B"]).sum()

print(x)

df.style

y=df.loc["foo","C"]
file.close()
  