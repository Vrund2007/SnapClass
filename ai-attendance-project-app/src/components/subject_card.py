import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    pills_html = ""
    if stats:
        pills_list = []
        for icon, label, value in stats:
            pills_list.append(
                f'<span style="background-color: #f1f5f9; color: #000000 !important; padding: 6px 14px; border-radius: 12px; font-size: 0.95rem; font-weight: 700; border: 1.5px solid #cbd5e1; display: inline-flex; align-items: center; gap: 6px; margin-right: 8px; margin-bottom: 8px;">'
                f'<span style="font-size: 1.1rem;">{icon}</span>'
                f'<b style="color: #000000 !important; font-weight: 800;">{value}</b>'
                f'<span style="color: #000000 !important; font-weight: 700;">{label}</span>'
                f'</span>'
            )
        pills_html = f'<div style="display: flex; flex-wrap: wrap; margin-top: 12px; margin-bottom: 4px;">{"".join(pills_list)}</div>'

    card_html = (
        f'<div class="subject-card" style="background-color: #ffffff !important; background: #ffffff !important; border: 2px solid #cbd5e1 !important; border-left: 8px solid #EB459E !important; border-radius: 20px !important; padding: 24px !important; margin-bottom: 16px !important; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08) !important;">'
        f'<div style="color: #000000 !important; font-family: Outfit, sans-serif !important; font-size: 1.65rem !important; font-weight: 800 !important; line-height: 1.2 !important; margin-bottom: 8px !important;">{name}</div>'
        f'<div style="color: #000000 !important; font-family: Outfit, sans-serif !important; font-size: 1.05rem !important; font-weight: 600 !important; margin-bottom: 8px !important;">'
        f'Code : <span style="background-color: #5865F2; color: #ffffff !important; padding: 2px 10px; border-radius: 6px; font-weight: 700; font-size: 0.95rem;">{code}</span>'
        f'&nbsp;|&nbsp; Section : <span style="color: #000000 !important; font-weight: 800;">{section}</span>'
        f'</div>'
        f'{pills_html}'
        f'</div>'
    )
    
    st.markdown(card_html, unsafe_allow_html=True)
    
    if footer_callback:
        footer_callback()
