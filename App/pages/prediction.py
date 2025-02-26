import streamlit as st
from predict import prediction
st.page_link("app.py", label="Home", icon="🏠")
if 'df' in st.session_state:
    df = st.session_state.df 
    df_raw=st.session_state.df_raw
    st.title("Prediction")

    st.dataframe(df)
    model_name=st.selectbox("Chọn model để dự đoán:",("XGBoost Classifier","Voting Classifier"))
    if st.button("Predict"):
        df_raw["Prediction"]=prediction(df,model_name)
        st.dataframe(df_raw)
        st.page_link("pages/analysis.py", label="Analyze reusult", icon="📈")
    
else:
    st.error("Chưa có dữ liệu để thực hiện dự đoán. Vui lòng quay lại trang chính và tải file.")
    st.page_link("pages/preview.py", label="Preview", icon="📄")
