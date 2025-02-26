import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
def preprocessing_data(df):
    df=pd.get_dummies(df,drop_first=True)
    return df
def Scaler(df):
    col=["CreditScore","Balance","EstimatedSalary","Age","Tenure","NumOfProducts"]
    scaler = StandardScaler()
    scale=scaler.fit(df[col])
    df[col]=scale.transform(df[col])
    return df

def prediction(df,model_name):
    columns=['CreditScore', 'Geography',
    'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
    'IsActiveMember', 'EstimatedSalary']
    df=df[columns]
    df=preprocessing_data(df)
    df=Scaler(df)
    if model_name=="XGBoost Classifier":
        model=joblib.load('xgb_model.pkl')
    else: model=joblib.load('voting_model.pkl')
    result=model.predict(df)
    return result