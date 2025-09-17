import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
    /* Primary color (buttons, sliders, radio, etc.) */
    .stButton > button,
    .stDownloadButton > button,
    .stRadio > div[role='radiogroup'] > label[data-baseweb='radio'] div:first-child,
    .stSlider [data-baseweb="slider"] [role="slider"] {
        background-color: #3835ebff !important;
        color: white !important;
    }

    /* Sidebar + secondary background */
    [data-testid="stSidebar"],
    .stAppViewContainer {
        background-color: #f1aeaeff !important;
    }

    /* Text color + font */
    html, body, [class*="css"] {
        color: #000000 !important;
        font-family: sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# 1. MUST be your first Streamlit call
st.set_page_config(layout="wide")

# 2. Load your data
df_gross = pd.read_pickle('sample_triangle.pkl')
df_net   = pd.read_pickle('sample_triangle1.pkl')

triangles = {
    'LT Engineering': {'Gross': df_gross.copy(), 'Net': df_net.copy()},
    'ST Engineering': {'Gross': df_gross.copy(), 'Net': df_net.copy()}
}

segment    = st.sidebar.selectbox("Choose a segment:", list(triangles.keys()))
sub_option = st.sidebar.radio("Choose type:", list(triangles[segment].keys()))

st.title("Unadjusted Link Ratios")
st.subheader(f"{segment} – {sub_option}")

# 3. Render the editable table
edited_df = st.data_editor(
    triangles[segment][sub_option],
    height=800,
    width="stretch"
)
