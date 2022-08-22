import streamlit as st
import contacts

def pipeline():
    st.title('Coming soon, stay tuned...')
    st.markdown("""
                   1. Churn Rate Analysis & Prediction (In development)
                   2. Cohort Analysis
                   3. Market Basket Analysis
                   4. Sentiments' Analysis: Customers' Reviews/Feedbacks, ...
                   5. Customers' Segmentation
                   6. Anomaly/Fraud Detection
                   
                   And so much more!
                """)
    st.markdown('---')
    contacts.contacts()