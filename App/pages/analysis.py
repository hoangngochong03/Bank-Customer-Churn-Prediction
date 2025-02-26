import streamlit as st
from analyze import allocate_of_age,allocate_of_geo,allocate_of_gender,allocate_of_balance,allocate_of_creditscore,correlation_of_age_creditscore
from analyze import allocate_of_EstiSalary,allocate_of_tenure,allocate_of_Numofproduct,allocate_of_HasCrCard,allocate_of_ActiveMem,correlation_of_age_salary
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/prediction.py", label="Prediction", icon="💡")
if 'df' in st.session_state:
    df = st.session_state.df_raw  # Truy xuất df từ session_state
    st.title("Analysis")
    st.write("Dữ liệu dự đoán:")
    st.dataframe(df)
    if "Prediction" in df.columns:
        st.dataframe(df[df["Prediction"]==1].describe())
    st.table(df.groupby("Geography").agg(
    AverageCreditScore=('CreditScore','mean'),
    AverageAge=('Age','mean'),
    NumOfCustomers=("Geography","count"),
    AverageSalary=('EstimatedSalary','mean'),
    TotalBalance=('Balance','sum')
    ).reset_index())
    col1,col2=st.columns(2)
    
    with col1:
        st.write("Biểu đồ phân phối độ tuổi")
        st.pyplot(allocate_of_age(df))
        st.write("Biểu đồ phân phối số dư tài khoản")
        st.pyplot(allocate_of_balance(df))
        st.write("Biểu đồ phân phối số điểm tín dụng")
        st.pyplot(allocate_of_creditscore(df))
        st.write("Biểu đồ phân phối mức lương dự tính")
        st.pyplot(allocate_of_EstiSalary(df))
        st.write("Biểu đồ phân phối thời gian gắn bó với ngân hàng")
        st.pyplot(allocate_of_tenure(df))
    with col2:
        st.write("Biểu đồ phân phối vị trí địa lý")
        st.pyplot(allocate_of_geo(df))
        st.write("Biểu đồ phân phối giới tính")
        st.pyplot(allocate_of_gender(df))
        st.write("Biểu đồ phân phối số lượng sản phẩm")
        st.pyplot(allocate_of_Numofproduct(df))
        st.write("Biểu đồ phân phối Thẻ tín dụng")
        st.pyplot(allocate_of_HasCrCard(df))
        st.write("Biểu đồ phân phối Thành viên hoạt động")
        st.pyplot(allocate_of_ActiveMem(df))

    st.write("Mối tương quan giữa độ tuổi và điểm tín dụng")
    st.pyplot(correlation_of_age_creditscore(df))
    st.write("Mối tương quan giữa độ tuổi và điểm tín dụng")
    st.pyplot(correlation_of_age_salary(df))

else:
    st.error("Chưa có dữ liệu để thực hiện dự đoán. Vui lòng quay lại trang chính và tải file.")
    st.page_link("pages/preview.py", label="Preview", icon="📄")
