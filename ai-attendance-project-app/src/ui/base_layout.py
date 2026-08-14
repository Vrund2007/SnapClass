import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 4rem !important;
                    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15) !important;
                    border: 1px solid rgba(255, 255, 255, 0.8) !important;
                    text-align: center !important;
                }

                .stApp div[data-testid="stColumn"] h2 {
                    color: #1e293b !important;
                    font-weight: 400 !important;
                    font-size: 2.2rem !important;
                    margin-bottom: 1.2rem !important;
                    letter-spacing: -0.01em !important;
                }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
                max-width: 980px !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                font-weight: 400 !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                font-weight: 400 !important;
                line-height:1.0 !important;
                margin-bottom:0rem !important;
                color: #1e293b !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }

            /* Input Labels - High Contrast Dark Color & Crisp Typography */
            label, [data-testid="stWidgetLabel"] label, [data-testid="stWidgetLabel"] p, .stTextInput label p, .stTextInput label {
                color: #0f172a !important;
                font-family: 'Outfit', sans-serif !important;
                font-size: 1rem !important;
                font-weight: 600 !important;
                margin-bottom: 6px !important;
            }

            /* Input Fields - Clean White Card Background, Dark Text & Sleek Border */
            .stTextInput input, div[data-testid="stTextInputRootElement"] input {
                background-color: #ffffff !important;
                color: #0f172a !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 500 !important;
                font-size: 1rem !important;
                border-radius: 12px !important;
                padding: 12px 16px !important;
                border: 1.5px solid #cbd5e1 !important;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04) !important;
                transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
            }

            .stTextInput input:focus, div[data-testid="stTextInputRootElement"] input:focus {
                border-color: #5865F2 !important;
                box-shadow: 0 0 0 3px rgba(88, 101, 242, 0.2) !important;
            }

            /* Placeholder Styling */
            .stTextInput input::placeholder {
                color: #64748b !important;
                opacity: 0.85 !important;
                font-weight: 400 !important;
            }

            /* Container for Password eye toggle icon */
            div[data-testid="stTextInputRootElement"] {
                background-color: #ffffff !important;
                border-radius: 12px !important;
                border: 1.5px solid #cbd5e1 !important;
            }

            div[data-testid="stTextInputRootElement"] button {
                background-color: transparent !important;
                color: #64748b !important;
                border: none !important;
                box-shadow: none !important;
                padding: 4px 8px !important;
            }

            div[data-testid="stTextInputRootElement"] button:hover {
                color: #5865F2 !important;
                transform: none !important;
            }

            /* Streamlit Dialog / Modal Styling - Clean Light White Card */
            div[data-testid="stModal"] > div[role="dialog"], div[data-testid="stModal"] > div, [data-testid="stDialog"] > div {
                background-color: #ffffff !important;
                border-radius: 28px !important;
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.25) !important;
                border: 1px solid rgba(0, 0, 0, 0.08) !important;
                padding: 2.2rem !important;
            }

            /* Modal Header Title & Subtitle Texts */
            div[data-testid="stModal"] h2, div[data-testid="stModal"] h1, div[data-testid="stModal"] h3 {
                color: #0f172a !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 700 !important;
                font-size: 1.8rem !important;
                margin-bottom: 6px !important;
            }

            div[data-testid="stModal"] [data-testid="stMarkdownContainer"] p, div[data-testid="stModal"] p, div[data-testid="stModal"] span {
                color: #475569 !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 500 !important;
            }

            /* Modal Input Labels & Input Fields */
            div[data-testid="stModal"] label, div[data-testid="stModal"] label p {
                color: #0f172a !important;
                font-weight: 600 !important;
                font-size: 0.95rem !important;
            }

            div[data-testid="stModal"] input {
                background-color: #f8fafc !important;
                color: #0f172a !important;
                border: 1.5px solid #cbd5e1 !important;
                border-radius: 12px !important;
                padding: 12px 16px !important;
                font-weight: 500 !important;
            }

            div[data-testid="stModal"] input:focus {
                border-color: #5865F2 !important;
                box-shadow: 0 0 0 3px rgba(88, 101, 242, 0.2) !important;
            }

            /* Modal Close Button */
            div[data-testid="stModal"] button[aria-label="Close"], div[data-testid="stModal"] button[data-testid="stBaseButton-header"] {
                color: #0f172a !important;
                background-color: #f1f5f9 !important;
                border-radius: 50% !important;
            }

            div[data-testid="stModal"] button[aria-label="Close"]:hover {
                background-color: #e2e8f0 !important;
            }

            /* High Contrast Warning & Alert Banners */
            div[data-testid="stAlert"] {
                background-color: #ffffff !important;
                border-radius: 16px !important;
                font-family: 'Outfit', sans-serif !important;
                border: 1.5px solid rgba(0, 0, 0, 0.08) !important;
                padding: 1rem 1.25rem !important;
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.04) !important;
            }

            div[data-testid="stAlert"] p, div[data-testid="stAlert"] span {
                color: #0f172a !important;
                font-weight: 600 !important;
                font-size: 1rem !important;
            }

            /* Form / Card Container Styling */
            div[data-testid="stForm"], div[data-testid="stVerticalBlockBorderWrapper"] > div {
                background: #ffffff !important;
                border-radius: 24px !important;
                padding: 2.2rem !important;
                border: 1px solid rgba(255, 255, 255, 0.9) !important;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08) !important;
            }

            button {
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                font-weight: 500 !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                font-weight: 500 !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            /* Sleek Tab / Inactive Action Buttons */
            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #ffffff !important;
                color: #0f172a !important;
                padding: 10px 20px !important;
                font-weight: 600 !important;
                border: 1.5px solid rgba(88, 101, 242, 0.25) !important;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04) !important;
                transition: all 0.25s ease-in-out !important;
            }

            button[kind="tertiary"]:hover{
                background-color: #f8fafc !important;
                border-color: #5865F2 !important;
                color: #5865F2 !important;
                transform :translateY(-2px) scale(1.02) !important;
                box-shadow: 0 8px 18px rgba(88, 101, 242, 0.15) !important;
            }

            button:hover{
                transform :scale(1.04);
            }
        </style>  

                """
            ,unsafe_allow_html=True)