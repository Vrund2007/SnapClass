import streamlit as st
import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    live_url = "https://vrundsnapclass.streamlit.app"
    join_url = f"{live_url}/?join-code={subject_code}"

    # Generate clean high-res QR code
    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=8, border=2, dark='#0f172a', light='#ffffff')

    st.markdown(f"""
    <div style="margin-bottom: 16px;">
        <div style="font-size: 1.3rem; font-weight: 800; color: #000000 !important; margin-bottom: 4px; font-family: 'Outfit', sans-serif;">
            {subject_name}
        </div>
        <div style="font-size: 0.95rem; color: #475569 !important; font-weight: 500; font-family: 'Outfit', sans-serif;">
            Share this link or QR code with your students to automatically enroll them in this class.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.1, 0.9], gap="medium", vertical_alignment="top")

    with col1:
        # Subject Code Card
        st.markdown(f"""
        <div style="background-color: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 12px 16px; margin-bottom: 12px;">
            <div style="font-size: 0.8rem; font-weight: 700; color: #64748b !important; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">Subject Code</div>
            <div style="font-size: 1.4rem; font-weight: 800; color: #5865F2 !important; letter-spacing: 0.05em;">{subject_code}</div>
        </div>
        """, unsafe_allow_html=True)

        # Class Join Link Card
        st.markdown(f"""
        <div style="background-color: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 12px 16px; margin-bottom: 12px;">
            <div style="font-size: 0.8rem; font-weight: 700; color: #64748b !important; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px;">Direct Invite Link</div>
            <div style="font-size: 0.85rem; font-weight: 600; color: #0f172a !important; word-break: break-all; background: #ffffff; padding: 8px 10px; border-radius: 8px; border: 1px solid #cbd5e1;">
                {join_url}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.info("Students can click the link or scan the QR code to join instantly.", icon="ℹ️")

    with col2:
        st.markdown("""
        <div style="text-align: center; background-color: #ffffff; padding: 12px; border-radius: 16px; border: 1.5px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
            <div style="font-size: 0.9rem; font-weight: 700; color: #0f172a !important; margin-bottom: 8px; font-family: 'Outfit', sans-serif;">Scan to Join</div>
        """, unsafe_allow_html=True)
        st.image(out.getvalue(), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
