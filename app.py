import streamlit as st
import pandas as pd

# Load data
undergrad_data = pd.read_csv("udata.csv")  # Undergraduate data
postgrad_data = pd.read_csv("data.csv")    # Postgraduate data

undergrad_data['Mat Number'] = undergrad_data['Mat Number'].astype(str)
postgrad_data['Mat Number'] = postgrad_data['Mat Number'].astype(str)
# Sidebar navigation
st.sidebar.title("Student Verification App")
menu = st.sidebar.radio("Navigation", ["Undergraduate", "Postgraduate"])

# Page 1: Undergraduate
if menu == "Undergraduate":
    st.title("Undergraduate Student Verification")

    sub_menu = st.radio("Select Option", ["Student Check", "Lecturer View"])

    if sub_menu == "Student Check":
        st.header("Check Your Registration Status")

        student_id = st.text_input("Enter your Matriculation Number:")
        
        if st.button("Verify Me"):
            if student_id in undergrad_data['Mat Number'].values:
                student = undergrad_data[undergrad_data['Mat Number'] == student_id]
                st.success(f"""
                Registration Found!  
                **Name**: {student['Name'].values[0]}  
                **Department**: {student['Department'].values[0]}  
                **Session**: {student['Session'].values[0]}  
                """)
            else:
                st.error("No registration found for the provided Matriculation Number.")

    elif sub_menu == "Lecturer View":
        st.header("View Undergraduate Registered Students")

        password = st.text_input("Enter Password:", type="password")
        correct_password = "lecturer123"  # Example password

        if password == correct_password:
            department = st.selectbox("Select Department", undergrad_data['Department'].unique())
            filtered_data = undergrad_data[undergrad_data['Department'] == department]

            if st.button("View Students"):
                if not filtered_data.empty:
                    st.write(filtered_data)
                    # Download button
                    csv = filtered_data.to_csv(index=False)
                    st.download_button(
                        label="Download Data as CSV",
                        data=csv,
                        file_name=f"{department}_undergrad_students.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No students found in the selected department.")
        elif password:
            st.error("Incorrect password. Access denied.")

# Page 2: Postgraduate
elif menu == "Postgraduate":
    st.title("Postgraduate Student Verification")

    sub_menu = st.radio("Select Option", ["Student Check", "Lecturer View"])

    if sub_menu == "Student Check":
        st.header("Check Your Registration Status")

        student_id = st.text_input("Enter your Matriculation Number:")
        
        if st.button("Verify Me"):
            if student_id in postgrad_data['Mat Number'].values:
                student = postgrad_data[postgrad_data['Mat Number'] == student_id]
                st.success(f"""
                Registration Found!  
                **Name**: {student['Name'].values[0]}  
                **Department**: {student['Department'].values[0]}  
                **Session**: {student['Session'].values[0]}  
                """)
            else:
                st.error("No registration found for the provided Matriculation Number.")

    elif sub_menu == "Lecturer View":
        st.header("View Postgraduate Registered Students")

        password = st.text_input("Enter Password:", type="password")
        correct_password = "lecturer123"  # Example password

        if password == correct_password:
            department = st.selectbox("Select Department", postgrad_data['Department'].unique())
            filtered_data = postgrad_data[postgrad_data['Department'] == department]

            if st.button("View Students"):
                if not filtered_data.empty:
                    st.write(filtered_data)
                    # Download button
                    csv = filtered_data.to_csv(index=False)
                    st.download_button(
                        label="Download Data as CSV",
                        data=csv,
                        file_name=f"{department}_postgrad_students.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No students found in the selected department.")
        elif password:
            st.error("Incorrect password. Access denied.")
