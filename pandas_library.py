# -*- coding: utf-8 -*-
"""pandas library.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UfXCNAI4oSXDzo4Sgyuvqx5mnZ2A4qET
"""

import pandas as pd
data=[1,2,3,4]
print(data)
Series =pd.Series(data)
print(Series)

#To change index name
list=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(list)

# Commented out IPython magic to ensure Python compatibility.
#importing  the libraries
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
x=np.arrange (0,0,1)
y=2*x+5
plt.plot(x,y)
plt.show()

#create data frame using list
import pandas as pd
data=[1,2,3,4,5,6,8,7,8,9,10]
df=pd.DataFrame(data)
print(df)

#creating dataframe using series
import pandas as pd
series=pd.Series([1,2,3,4],index=["a","b","c","d"])
print(Series)
type(Series)
df=pd.DataFrame(Series)
print(df)
type(df)

#create a DataFrame using Numpy array
import numpy as np
import pandas as pd
array=np.array([[1000,2000],["john","rohan"]])
df=pd.DataFrame({'name':array[1],'salary':array[0]})
df

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(0,10,(3,3)),columns=['x1','x2','x3'])

#Concantation(used to combine two or  more(either columns or rows) DataFrames along perticular axis)
#step1:create two DataFrames
import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
})

print(df1)

df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5']
})

print(df2)

# Concatenate DataFrames
result = pd.concat([df1, df2])

print(result)

#Along Columns
result = pd.concat([df1, df2], axis=1)

print(result)

#concatenate and reset index
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
})

df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5']
})
result=pd.concat([df1,df2],ignore_index=True)
print(result)

#inner merge
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value': [1, 2, 3, 4]
})
print(df1)
df2 = pd.DataFrame({
    'key': ['B', 'D', 'E', 'F'],
    'value': [5, 6, 7, 8]
})

print(df2)

result = pd.merge(df1, df2, on='key', how='outer')
print(result)

#left merge
result = pd.merge(df1, df2, on='key', how='left')
print(result)

#right
print(df1)
print(df2)

result = pd.merge(df1, df2, on='key', how='right')
print(result)

#outer merge
result = pd.merge(df1, df2, on='key', how='outer')
print(result)

#inner join
import pandas as pd

# DataFrame 1
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [23, 34, 25, 40]
})

# DataFrame 2
df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Department': ['HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [50000, 60000, 55000, 70000]
})

# Perform Inner Join
result = df1.merge(df2, on='ID', how='inner')

print(result)

result1=pd.merge(df1,df2, on='ID', how='inner')
print(result1)

import pandas as pd

# DataFrame 1
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [23, 34, 25, 40]
})

# DataFrame 2
df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Department': ['HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [50000, 60000, 55000, 70000]
})

# Set ID as the index
df1.set_index('ID', inplace=True)
df2.set_index('ID', inplace=True)

print(df1)

print(df2)

#creating a datafram using numpy array
import numpy as np
import pandas as pd
array=np.array([[5000,6000],["john","james"]])
df=pd.DataFrame({'name':array[1],'salary':array[0]})
df

df=pd.DataFrame(np.random.randint(0,10,(3,3)),columns=['x1','x2','x3'])

import pandas as pd
import numpy as np



df

#concatenation in pands(used to combine dataset)
import pandas as pd
DF1=pd.DataFrame({'A':['A0','A1','A2','A3'],
                  'B':['B0','B1','B2','B3'],
                  'C':['C0','C1','C2','C3']

})
print(DF1)
DF2=pd.DataFrame({'A':['A5','A6','A7','A8'],
                  'B':['B11','B10','B9','B8'],
                  'C':['C4','C5','C6','C7']


})
print(DF2)
#concatenate
result=pd.concat([DF1,DF2])
print(result)

import pandas as pd
DF1=pd.DataFrame({'A':['A0','A1','A2','A3'],
                  'B':['B0','B1','B2','B3'],
                  'C':['C0','C1','C2','C3']

})

DF2=pd.DataFrame({'A':['A5','A6','A7','A8'],
                  'B':['B11','B10','B9','B8'],
                  'C':['C4','C5','C6','C7']


})

#concatenate
result=pd.concat([DF1,DF2])
print(result)

#column concatenation
result=pd.concat([DF1,DF2],axis=1)
print(result)

#row
result=pd.concat([DF1,DF2],ignore_index=True)
print(result)

result=pd.concat([DF1,DF2],axis=1,ignore_index=True)
print(result)

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
file_path ='/content/mtcars.csv'

cars=pd.read_csv(file_path)

print(cars)

cars.mpg = cars.mpg.astype(str)

type(cars)

#to view first 10 records
cars.head(10)

#to view last records
cars.tail(3)

cars.shape

cars.info()

#mean
mean_values = cars.mean(numeric_only=True)
print(mean_values)

#median
median_values = cars.median(numeric_only=True)
print(median_values)

#standard deviation
std_values = cars.std(numeric_only=True)
std_values

#maximum of each attribute
cars.max(numeric_only=True)
#cars.max()

#minimum of each attribute
cars.min()

#number of non-null records in each column
cars.count()

#descriptive statistics summary
cars.describe()

print(cars)

#rename column
cars=cars.rename(columns={'Unnamed: 0':'model'})
print(cars)

#rename column
cars=cars.rename(columns={'Unnamed: 0':'model'})
print(cars)

cars.describe()



#drop unwanted column
cars = cars.drop(columns=['S.No'])
cars

#Drop unwanted Row

cars = cars.drop(index=2)
cars

#view hp column only
print(cars.iloc[ : ,4])   #[ :  (Rows), 4(Columns)]

#first five records of hp column
cars.iloc[ 0:5,4]   #5-1=4th index

#all rows, all columns
cars.iloc[ : , : ]  #[ : , : ]

#for attributes from hp to carb see all the records from index 6
cars.iloc[6:,4:]

#View attributes from drat to vs and records from 2nd index to 10th index
cars.iloc[2:11,5:9]

#Now we want to look at all the rows and only the first column
cars.iloc[:,0]

#see all the record of mpg column
cars.loc[:,"mpg"]

cars.loc[0:6,"mpg":"qsec"]

cars['am'] = 1
cars

#double up records in 'am' using lambda fxn
f = lambda x: x*2
cars['am']= cars['am'].apply(f)
cars

#sorting(asending order)
cars.sort_values(by='cyl')

#sorting(decending order)
cars.sort_values(by='cyl', ascending=False)

cars.sort_values(by='mpg', ascending=False)

#sort mpg column by descending order
cars.sort_values(by='mpg', ascending=False)

#filtering(filter 6 cylinders)
cars['cyl'] >= 6

#filter records with more than 6 cylinders
filter1 = cars['cyl'] > 6
#apply filter to dataframe
filtered_new = cars[filter1]
#view filtered dataframe
filtered_new

cars[(cars["cyl"] > 6) & (cars["hp"] > 300)]

new=cars[cars['cyl'] > 6]
new

#filter records with more than 6 cyl and hp more than 300
filter2 = (cars["cyl"] > 6) & (cars["hp"] > 300)
#apply filter to dataframe
filtered_review = cars[filter2]
#display filtered data
filtered_review

# Commented out IPython magic to ensure Python compatibility.
#data visualization
#import matplotlib
import matplotlib.pyplot  as plt
# %matplotlib inline
#see how hp varies with each car with line plot
y = cars['hp']
x=range(44)
plt.plot(x,y)

# Commented out IPython magic to ensure Python compatibility.
#import matplotlib
import matplotlib.pyplot  as plt
# %matplotlib inline
#see how hp varies with each car with line plot
y2 = cars['disp']
x  = range(44)
plt.plot(x,y2)

# Commented out IPython magic to ensure Python compatibility.
#import matplotlib
import matplotlib.pyplot  as plt
# %matplotlib inline
y1 = cars['hp']
y2 = cars['disp']
#see how both hp and disp varies
x  = range(44)
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend()

# Commented out IPython magic to ensure Python compatibility.
#import matplotlib
import matplotlib.pyplot  as plt
# %matplotlib inline
y1 = cars['hp']
y2 = cars['disp']
x  = range(44)
#area plot of hp and disp
plt.stackplot(x,y1)#,colors = 'r', alpha = 0.7)
plt.stackplot(x,y2)#,colors = 'c', alpha = 0.5)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot  as plt
# %matplotlib inline
y1 = cars['hp']
y2 = cars['disp']
x  = range(44)
#plot both line plot and area plot to see the margin
plt.plot(x,y1, linewidth = 2.0, color = 'c')
plt.stackplot(x,y1,colors = 'gold', alpha = 0.7)
plt.plot(x,y2, linewidth = 1.0, color = 'gold')
plt.stackplot(x,y2,colors = 'b', alpha = 0.5)

# Commented out IPython magic to ensure Python compatibility.
#import matplotlib
import matplotlib.pyplot  as plt
# %matplotlib inline
y = cars['hp']
#x  = range(32)
#model to list
x1 = cars['model'].tolist()
#adding figure to adjust figsize
#fig = plt.figure(figsize = (30,15))
#see how hp changes with bar plot
plt.bar(x1,y,color="purple", alpha=0.9)

# Commented out IPython magic to ensure Python compatibility.
#import matplotlib
import matplotlib.pyplot  as plt
# %matplotlib inline
y = cars['hp']
x  = range(32)
x1 = cars['model'].tolist()
fig = plt.figure(figsize = (17,10))
#to avoid the overlapping issue plot horizontal bar plot
plt.barh(x1,y, color="purple", alpha=0.8)

import pandas as pd
data=pd.read_excel('/content/Sample - Superstore.xls')
data
data= data.drop(columns=['Customer ID'])
print(data)

data.shape

print(data)

data.index

data.columns

data

data['City']   #Subsetting of Data

data[['City','Segment']].head(2)

data[['City','Segment']].tail(3)

#i loc - integer location

data.iloc[0:2,0:2]

data.iloc[0:5,-3: ]

data.loc[0:3,['Row ID','Segment']]

data.loc[0:3,'Row ID':'Segment']

data.loc['Profit': ]

data['Segment'].unique()

data.shape[0]  #if I 0 it gives only Rows





