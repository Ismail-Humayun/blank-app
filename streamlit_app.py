import streamlit as st
import pandas as pd


# 1. MUST be your first Streamlit call
st.set_page_config(layout="wide")

# 2. Load your data
df_gross = pd.read_pickle('sample_triangle.pkl')
df_net   = pd.read_pickle('sample_triangle1.pkl')

triangles = {
    'LT Engineering': {'Gross': df_gross.copy(), 'Net': df_net.copy()},
    'ST Engineering': {'Gross': df_net.copy(), 'Net': df_gross.copy()}
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
