import streamlit as st
import pandas as pd

# Sidebar navigation
st.sidebar.title("Student Verification App")
menu = st.sidebar.radio("Navigation", ["Student Check", "Lecturer View"])
undergrad_data = pd.read_csv("data.csv")
postgrad_data  = pd.read_csv("data.csv")
# Page 1: Student Check
if menu == "Student Check":
    st.title("Check Your Registration Status")

    section = st.radio("Select Section", ["Undergraduate", "Postgraduate"])

    if section == "Undergraduate":
        data = undergrad_data
    else:
        data = postgrad_data

    student_id = st.text_input("Enter your Student ID:")
    
    if st.button("Check Status"):
        if student_id in data['ID'].values:
            student = data[data['ID'] == student_id]
            st.success(f"Registration Found!\nName: {student['Name'].values[0]}\nDepartment: {student['Department'].values[0]}\nSession: {student['Session'].values[0]}")
        else:
            st.error("No registration found for the provided Student ID.")

# Page 2: Lecturer View
elif menu == "Lecturer View":
    st.title("View Registered Students")

    password = st.text_input("Enter Password:", type="password")
    correct_password = "lecturer123"  # Example password

    if password == correct_password:
        section = st.radio("Select Section", ["Undergraduate", "Postgraduate"])

        if section == "Undergraduate":
            data = undergrad_data
            st.subheader("Undergraduate Students")
        else:
            data = postgrad_data
            st.subheader("Postgraduate Students")

        department = st.selectbox("Select Department", data['Department'].unique())

        filtered_data = data[data['Department'] == department]

        if st.button("View Students"):
            if not filtered_data.empty:
                st.write(filtered_data)
                # Download button
                csv = filtered_data.to_csv(index=False)
                st.download_button(
                    label="Download Data as CSV",
                    data=csv,
                    file_name=f"{department}_students.csv",
                    mime="text/csv"
                )
            else:
                st.warning("No students found in the selected department.")
    elif password:
        st.error("Incorrect password. Access denied.")
