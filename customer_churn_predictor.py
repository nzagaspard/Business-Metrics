import streamlit as st
import pickle
import numpy as np
import pandas as pd

def churn_predictor():
    
    title = """<div style="background-color:#0D4493;padding:1px">
            <h1 style="color:white;text-align:center;">Customer Churn Predictor</h1></div>"""

    st.markdown(title, unsafe_allow_html = True)

    info = """<h4 style="color:#0D4493;text-align:justify;"><strong>This application uses the machine learning model trained on data from a certain bank to predict whether a customer will churn or not.</strong></h4>"""
    st.markdown(info, unsafe_allow_html = True)

    def predict_churn(features):

        with open('churn prediction model.sav', 'rb') as model_file:

            predicting_model = pickle.load(model_file)
            churn_status = predicting_model.predict(features)
            churn_probabilities = predicting_model.predict_proba(features)

        return churn_status, churn_probabilities

    with st.form('customer_info', clear_on_submit = True):
        st.markdown("##### Complete the customer information below and press on **Predict**.")
        country = st.selectbox("Choose the Country", ['', 'France', 'Germany', 'Spain'])
        gender = st.selectbox('Choose the Gender', ['', 'Male', 'Female'])
        st.write('')
        active = st.checkbox('Check if the customer is Active.')
        st.write('')
        credit_score = st.text_input('Enter the Credit Score')
        age = st.text_input('Enter the Age')
        balance = st.text_input('Enter the Balance')
        products = st.text_input('Enter the Number of Products')

        col1, col2, col3, col4, col5 = st.columns(5)

        predict_button = col3.form_submit_button("Predict")

        if predict_button:
            if '' in [country, gender, credit_score, age, balance, products]:
                st.error('One or More inputs are empty.')

            else:

                try:
                    credit_score = int(credit_score.strip())
                    age = int(age.strip())
                    balance = int(balance.strip())
                    products = int(products.strip())
                    ingermany = 1 if country == 'Germany' else 0
                    isfemale = 1 if gender == 'Female' else 0
                    isactive = 1 if active else 0
                    low_score = 1 if credit_score <= 500 else 0
                    isold =  1 if age > 40 else 0
                    low_balance = 1 if balance <= 75_000 else 0
                    prod1 = 1 if products == 1 else 0
                    prod2 = 1 if products == 2 else 0
                    prod3 = 1 if products >= 3 else 0

                    inputs = [ingermany, isfemale, isactive, low_score, isold, low_balance, prod1, prod2, prod3]
                    column_names = ['IsInGermany', 'IsFemale', 'IsActiveMember', 'IsCreditScoreLow',
                                    'IsOld', 'IsBalanceLow', 'NumOfProducts_1', 'NumOfProducts_2', 'NumOfProducts_3']

                    df = pd.DataFrame(np.array(inputs)).T
                    df.columns = column_names

                    with st.spinner('Predicting. Please wait...'):

                        prediction, probabilities = predict_churn(df)

                        churning_probability = int(probabilities[0][1]*100)
                        non_churning_probability = int(probabilities[0][0]*100)

                        formatted_probabilities = f"""<h5 style="color:#0D4493;text-align:center;"><strong>
                                                      Churning Probability: {churning_probability}%<br>
                                                      Not Churning Probability: {non_churning_probability}%
                                                      </strong></h5>"""

                        formatted_class = f"""<h2 style="color:red;text-align:center;"><strong>
                                                      Overall Prediction: Churning</strong></h2>""" if prediction == 1 \
                                          else f"""<h2 style="color:green;text-align:center;"><strong>
                                                      Overall Prediction: Not Churning</strong></h2>"""

                        st.markdown(formatted_probabilities, unsafe_allow_html = True)                  
                        st.markdown(formatted_class, unsafe_allow_html = True)

                except Exception as e:               
    #                 st.error(e)
                    st.error('###### One of the the expected inputs that should be numbers are not a valid number.')
    st.write('#')
    disclaimer = st.expander('Details & Disclaimer!')
    disclaimer.markdown("""⚠️ This project was developed for practice/testing purposes. Should not totally be considered for actual informed decisions!""")
    disclaimer.markdown(""" ℹ️ The notebook used to for explaratory data analysis and building machine learning models can be found [here](https://www.kaggle.com/code/gaspardnzasabimfura/gaspard-data-scientist-coding-exercise-bk-df/notebook)""")