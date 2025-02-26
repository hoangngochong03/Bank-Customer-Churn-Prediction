import numpy as np
import pandas as pd
from sklearn.utils import resample
import matplotlib.pyplot as plt
import seaborn as sns
def allocate_of_age(df):
    plt.figure(figsize=(10, 6))  
    if "Prediction" in df.columns:
        sns.histplot(data=df,x="Age", hue="Prediction",bins=20, color='skyblue', edgecolor='black',kde=True)  
    else:
        sns.histplot(data=df,x="Age", bins=20, color='skyblue', edgecolor='black')  
    plt.title('Distribution of Age') 
    plt.xlabel('Age')  
    plt.ylabel('Frequency')  
    return plt

def allocate_of_balance(df):
    plt.figure(figsize=(10, 6))  
    if "Prediction" in df.columns:
        sns.histplot(data=df,x="Balance", hue="Prediction",bins=20, color='skyblue', edgecolor='black')  
    else:
        sns.histplot(data=df,x="Balance", bins=20, color='skyblue', edgecolor='black')  
    plt.title('Distribution of Balance') 
    plt.xlabel('Balance') 
    plt.ylabel('Frequency') 
    return plt

def allocate_of_tenure(df):
    plt.figure(figsize=(10, 6))
    if "Prediction" in df.columns:
        sns.countplot(x="Tenure", data=df,hue="Prediction", color='skyblue', edgecolor='black')
    else:
        sns.countplot(x="Tenure", data=df, color='skyblue', edgecolor='black')
    plt.title('Distribution of Tenure')  
    plt.xlabel('Tenure')  
    plt.ylabel('Frequency') 
    return plt

def allocate_of_creditscore(df):
    plt.figure(figsize=(10, 6))  
    if "Prediction" in df.columns:
        sns.histplot(data=df,x="CreditScore", hue="Prediction",bins=20, color='skyblue', edgecolor='black')  
    else:
        sns.histplot(data=df,x="CreditScore", bins=20, color='skyblue', edgecolor='black')  
    plt.title('Distribution of CreditScore') 
    plt.xlabel('Credit Score') 
    plt.ylabel('Frequency') 
    return plt

def allocate_of_EstiSalary(df):
    plt.figure(figsize=(10, 6)) 
    if "Prediction" in df.columns:
        sns.histplot(data=df,x="EstimatedSalary", hue="Prediction",bins=20, color='skyblue', edgecolor='black')  
    else:
        sns.histplot(data=df,x="EstimatedSalary", bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of EstimatedSalary') 
    plt.xlabel('EstimatedSalary') 
    plt.ylabel('Frequency')  
    return plt

def allocate_of_geo(df):
    plt.figure(figsize=(10, 6)) 
    if "Prediction" in df.columns:
        sns.countplot(x="Geography",data=df,hue="Prediction")
    else:
        sns.countplot(x="Geography",data=df)
    plt.title('Distribution of Geography') 
    plt.xlabel('Geography') 
    plt.ylabel('Frequency')  
    return plt
def allocate_of_gender(df):
    plt.figure(figsize=(8, 4)) 
    if "Prediction" in df.columns:
        sns.countplot(x="Gender",data=df,hue="Prediction")
    else:
        plt.pie(df['Gender'].value_counts(), labels=df['Gender'].value_counts().index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Gender') 
    plt.xlabel('Gender') 
    plt.ylabel('Frequency')  
    plt.show()
    return plt
def allocate_of_Numofproduct(df):
    plt.figure(figsize=(10, 6)) 
    if "Prediction" in df.columns:
        sns.countplot(x="NumOfProducts",data=df,hue="Prediction")
    else:
        sns.countplot(x="NumOfProducts",data=df)
    plt.title('Distribution of NumOfProduct') 
    plt.xlabel('NumOfProduct') 
    plt.ylabel('Frequency')  
    return plt
def allocate_of_HasCrCard(df):
    plt.figure(figsize=(10, 6)) 
    if "Prediction" in df.columns:
        sns.countplot(x="HasCrCard",data=df,hue="Prediction")
    else:
        sns.countplot(x="HasCrCard",data=df)
    plt.title('Distribution of HasCrCard') 
    plt.xlabel('HasCrCard') 
    plt.ylabel('Frequency')  
    return plt
def allocate_of_ActiveMem(df):
    plt.figure(figsize=(10, 6)) 
    if "Prediction" in df.columns:
        sns.countplot(x="IsActiveMember",data=df,hue="Prediction")
    else:
        sns.countplot(x="IsActiveMember",data=df)
    plt.title('Distribution of IsActiveMember') 
    plt.xlabel('IsActiveMember') 
    plt.ylabel('Frequency')  
    return plt
def correlation_of_age_creditscore(df):
    plt.figure(figsize=(10, 6)) 
    plt.scatter(df["Age"],df["CreditScore"])  
    plt.title('Correlation between Age and CreditScore')  
    plt.xlabel('Age') 
    plt.ylabel('Credit Score')  
    return plt
def correlation_of_age_salary(df):
    plt.figure(figsize=(10, 6)) 
    plt.scatter(df["Age"],df["EstimatedSalary"])  
    plt.title('Correlation between Age and EstimatedSalary')  
    plt.xlabel('Age') 
    plt.ylabel('Estimated Salary')  
    return plt