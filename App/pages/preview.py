import streamlit as st
import pandas as pd
from preprocessing_data import check_null,check_num_unique,handle_null
st.page_link("app.py", label="Home", icon="🏠")
st.title("Bank Customer Churn Prediction")
file=st.file_uploader("Upload file here",type=['csv','xlsx'])
if file is None:
    if 'df' in st.session_state:
        df = st.session_state.df_raw
        st.dataframe(df)
    else:
        st.write("Vui lòng upload file csv hoặc xlsx")
else:
    if file.name.lower().endswith("csv"):
        df=pd.read_csv(file)
    elif file.name.lower().endswith("xlsx"):
        df=pd.read_excel(file)
    
    st.dataframe(df)
    columns=['CreditScore', 'Geography',
    'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
    'IsActiveMember', 'EstimatedSalary']
    #df=df[columns]
    null_check=check_null(df[columns])
    st.write("Số lượng giá trị null của từng cột")
    st.dataframe(null_check,hide_index=True)
    nunique=check_num_unique(df)
    st.write("Số lượng giá trị duy nhất của từng cột")
    st.dataframe(nunique,hide_index=True)
    lst_null=[]
    for i in range(len(columns)):
        if null_check[i][1]!=0:
            lst_null.append(null_check[i][0])
    
    if lst_null:
        st.write("Các cột chứa null:",lst_null)
        opt=st.selectbox("Các lựa chọn xử lý null:",("DROP (loại bỏ null)","MODE (thay null bằng giá trị xuất hiện nhiều nhất trong cột đó)",
                                                        ),)
        if st.button("Xử lý Null"):
            df=handle_null(df,opt,default_value=0)
            st.dataframe(df,hide_index=True)
    st.session_state.df_raw=df.copy()
    st.session_state.df = df
st.page_link("pages/prediction.py", label="Prediction", icon="💡")
st.page_link("pages/analysis.py", label="Analysis", icon="📈")


