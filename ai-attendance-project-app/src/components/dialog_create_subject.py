import streamlit as st
from src.database.db import create_subject



@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.markdown('<p style="color: #475569 !important; font-size: 0.95rem; margin-bottom: 1.2rem; font-weight: 500;">Enter the details of the new subject below</p>', unsafe_allow_html=True)
    sub_id = st.text_input("Subject Code", placeholder="CS101")
    sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="A")


    if st.button("Create Subject Now", type='primary', width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast("Subject Created Succesfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all the fields")
