import streamlit as st
from PIL import Image


@st.dialog("Capture or Upload Photos")
def add_photos_dialog():
    st.markdown("""
    <div style="color: #475569 !important; font-size: 0.95rem; font-weight: 500; font-family: 'Outfit', sans-serif; margin-bottom: 16px;">
        Add classroom photos via camera snapshot or upload from your device to scan for attendance.
    </div>
    """, unsafe_allow_html=True)

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'secondary'
        if st.button('📸 Camera', type=type_camera, width='stretch', key='tab_cam'):
            st.session_state.photo_tab = 'camera'
            st.rerun()

    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'secondary'
        if st.button('📁 Upload Photos', type=type_upload, width='stretch', key='tab_upload'):
            st.session_state.photo_tab = 'upload'
            st.rerun()

    st.space()

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Take Classroom Snapshot', key='dialog_cam')
        if cam_photo:
            if 'attendance_images' not in st.session_state:
                st.session_state.attendance_images = []
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast('Photo Captured Successfully!', icon='📸')
            st.rerun()

    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader('Choose photo files', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key='dialog_upload')
        if uploaded_files:
            if 'attendance_images' not in st.session_state:
                st.session_state.attendance_images = []
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))
            st.toast(f'{len(uploaded_files)} Photo(s) Uploaded Successfully!', icon='📁')
            st.rerun()

    # Photo counter summary
    count = len(st.session_state.get('attendance_images', []))
    if count > 0:
        st.success(f"📸 {count} classroom photo(s) ready for scanning")

    st.divider()
    if st.button(f'Done ({count} photos added)', type='primary', width='stretch'):
        st.rerun()
