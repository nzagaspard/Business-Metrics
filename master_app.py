import streamlit as st
from streamlit_option_menu import option_menu
from nps_calculator import nps
from customer_loyality_retention import clr
from churn_rate import churn_rate
from home import home

st.set_page_config(page_title="Business Metrics",page_icon=":bar_chart:")

#Application
hide_st_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# st.sidebar.title('Applications')
# apps = st.sidebar.selectbox('Choose the application', ['Net Promoter Score Calculator', 'Customer Loyality Retention', 
#                                                        'Churn Rate Analysis & Prediction'])
app_choices = ['Home','Net Promoter Score', 'Customer Loyality Retention', 'In Pipeline']

with st.sidebar:
    apps = option_menu("App Gallery", app_choices,
                         icons=['house','bookmark-heart', 'sort-numeric-down', 'bar-chart-steps'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
if apps == app_choices[0]:
    home()
elif apps == app_choices[1]:
    nps()
elif apps == app_choices[2]:
    clr()
elif apps == app_choices[3]:
    churn_rate()