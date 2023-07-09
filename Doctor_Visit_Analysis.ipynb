#Import Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

#Load the Dataset
df = pd.read_csv("Visit_Data.csv")
print(df.head(15))

#Display complete Information about the columns of the dataset
df.info()

#Find out the Total No. of People based on their count of illness
df["illness"].value_counts()

#Visualize and Analyze Maximum, Minimum and Medium Income
y = list(df.salary_income)
plt.boxplot(y)
plt.title("Income")
plt.show()

#Find out the no of days of Reduced Activity of male and females due to illness
df.groupby(['gender','reduced']).mean()

#Visualize is there any missing values in the dataset based on heat map
sns.heatmap(df.isnull(),cbar=False,cmap='viridis')

#Find out the Correlation between variables and Different variables in the given Dataset
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True,annot=True,cmap='Blues')

#Analyse How the income of a patient that effects the no of visits to the Hospital
plt.figure(figsize=(10,10))
plt.scatter(x='salary_income',y='visits',data=df)
plt.xlabel('Income')
plt.ylabel('Visits')

#Count and Visualize the no of males and females affected by illness 
sns.histplot(df.gender,bins=2)

#Visualize the Percentage of people getting Govt Health Insurance due to low income, 
#due to old age and also the percentage of people having Private Health Insurance

# % of people getting govt Insurance due to Low income
label=['yes', 'no']
Y = df[df['freepoor']=='yes']
N = df[df['freepoor']=='no']
x = [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x, labels=label)
plt.title("% of people getting govt health Insurance due to low income ")
plt.show()
#% of people having private Insurance
Y = df[df['private']=='yes']
N = df[df['private']=='no']
x = [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x, labels=label)
plt.title("% of people having private health Insurance ")
plt.show()
#% of people getting govt Insurance due to old age, disability or veteran status
Y = df[df['freerepat']=='yes'] 
N = df[df['freerepat']=='no']
x = [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x, labels=label)
plt.title("% of people getting govt health Insurance due to old age, disability or veteran status")
plt.show()

#Plot a Horizontal Bar Chart to analyze the reduced days of activity due to illness based on gender
db= df.groupby('gender')['reduced'].sum().to_frame().reset_index()
#Creating the bar chart
plt.barh(db['gender'], db['reduced'], color = ['cornflowerblue', 'lightseagreen'])
#Adding the aesthetics
plt.title('Bar Chart')
plt.xlabel('Reduced Activity')
plt.ylabel('gender')
#Show the plot
plt.show()
