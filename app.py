import streamlit as st 
import pandas as pd 

st.write(pd.DataFrame({
    '1st Col': [3, 4, 5, 6],
    '2nd Col': [40, 50, 60, 70]
}))