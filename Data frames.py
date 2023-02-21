import pandas as pd

df=pd.read_excel('marks.xlsx')
print(df)
print("Columns:",df.columns)
print("First 2 columns:", df.columns[0:2])
print("Datatype:\n", df.dtypes)
print("Datatype of a column:", df['Maths'].dtypes)
print("First five rows:\n", df.head())
print("Last five rows:\n", df.tail())
print("First two rows:\n", df.head(2))
print("Last three columns:\n", df.tail(3))

#slicing
print("Rows:\n", df[1:3])
df.index=['one','two','three','four','five','six','seven','eight','nine','ten']
print("After changing the index:\n", df)
print("Using loc function:\n",df.loc[['two','four']])
print("Using iloc function:\n", df.iloc[3:5])
print("Using iloc function:\n", df.iloc[3:5,1:3])

#frequency distribution
print(df.value_counts('Maths', ascending=True))

#sorting
print(df.sort_values('Maths', ascending=True))

#describe function
print(df.describe())

#renaming variable
df.columns=['Name','Roll No.','Math','Eng','Phy','History','Hindi','Telugu','Bio','Chem']
print(df)

#addition of a column
df['PPS']=[95,69,45,78,96,96,74,85,74,65]
print(df)

#groupby function
print(df.groupby(['Name']).mean())

#missing values
print(df.isnull())

#filling missing vales
a=df.fillna(0)
print(a)

#dropping missing vales
b=df.dropna()
print(b)

#dropping columns
c=df.drop('Hindi', axis=1)
print(c)

#dropping rows
d=df.drop('one', axis=0)
print(d)

#rank
print(df.rank())

#concat
e=pd.concat([c,d])
print(e)

