import streamlit as st
from nps_calculator import nps
from customer_loyality_retention import clr
from churn_rate import churn_rate

st.set_page_config(page_title="Business Metrics",page_icon=":bar_chart:")

#Application
hide_st_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.sidebar.title('Applications')
apps = st.sidebar.selectbox('Choose the application', ['Net Promoter Score Calculator', 'Customer Loyality Retention', 
                                                       'Churn Rate Analysis & Prediction'])

if apps == 'Net Promoter Score Calculator':
    nps()
elif apps == 'Customer Loyality Retention':
    clr()
elif apps == 'Churn Rate Analysis & Prediction':
    churn_rate()