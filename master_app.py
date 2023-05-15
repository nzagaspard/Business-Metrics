import streamlit as st
from streamlit_option_menu import option_menu
from nps_calculator import nps
from customer_loyality_retention import clr
from pipeline import pipeline
from customer_churn_predictor import churn_predictor
from home import home

st.set_page_config(page_title="Business Metrics",page_icon=":chart_increasing:")

#Application
hide_st_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

app_choices = {'Home':'home','Net Promoter Score':'nps', 'Customer Loyality Retention':'clr', 
               'Customer Churn Predictor':'ccp', 'In Pipeline':'pipeline'}

with st.sidebar:
    apps = option_menu("App Gallery", list(app_choices.keys()),
                         icons=['house','bookmark-heart', 'sort-numeric-down', 'people-fill', 'bar-chart-steps'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
    
if app_choices[apps] == 'home':
    home()  
elif app_choices[apps] == 'nps':
    nps()
elif app_choices[apps] == 'clr':
    clr()
elif app_choices[apps] == 'ccp':
    churn_predictor()
elif app_choices[apps] == 'pipeline':
    pipeline()
    