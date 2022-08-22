import streamlit as st
import contacts

def home():    
    title = """<div style="background-color:#02ab21;padding:1px">
                <h3 style="color:white;text-align:center;">Business Metrics (Explanation, Calculation, Intepretation)</h3></div>"""

    st.markdown(title, unsafe_allow_html=True)
    
    st.markdown('<br>', unsafe_allow_html=True)
    
    st.markdown("""<h6 style="text-align: justify;"> A one stop center application for business metrics insights and calculators. Even though it is still in development some of its applications are live. It will feature metrics such as Net Promoter Score, Churn Rate, Cohort Analytics, Customers Loyalty & Retention among others. </h6>""", unsafe_allow_html=True)
    
    st.markdown("""👈 On the left you can navigate to a desired app.""", unsafe_allow_html=True)
    st.markdown('---')
    contacts.contacts()