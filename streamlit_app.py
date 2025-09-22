import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Load your data
df_gross = pd.read_pickle("sample_triangle.pkl")
df_net   = pd.read_pickle("sample_triangle1.pkl")

triangles = {
    "LT Engineering": {"Gross": df_gross.copy(), "Net": df_net.copy()},
    "ST Engineering": {"Gross": df_net.copy(), "Net": df_gross.copy()},
}

segment    = st.sidebar.selectbox("Choose a segment:", list(triangles.keys()))
sub_option = st.sidebar.radio("Choose type:", list(triangles[segment].keys()))

st.title("Unadjusted Link Ratios")
st.subheader(f"{segment} – {sub_option}")

# Editable DataFrame
edited_df = st.data_editor(
    triangles[segment][sub_option],
    height=800,
    width="stretch",
    key=f"{segment}-{sub_option}"  # unique key avoids conflicts
)

# If this is LT Engineering – Gross, update df_gross permanently
if segment == "LT Engineering" and sub_option == "Gross":
    df_gross = edited_df  # overwrite with edits
    # Optionally, save back to pickle file
    if st.button("💾 Save LT Engineering – Gross"):
        df_gross.to_pickle("sample_triangle.pkl")
        st.success("Changes saved permanently to sample_triangle.pkl")
