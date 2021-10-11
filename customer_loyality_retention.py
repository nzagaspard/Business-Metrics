import streamlit as st
from data_utils import calculate_crr

def clr():
    title = """<div style="background-color:#2F4F4F;padding:1px">
            <h2 style="color:white;text-align:center;">Customer Retention Rate (CRR) Calculator</h2></div>"""

    st.markdown(title, unsafe_allow_html=True)
    st.write('')
    st.header('Overview')
    intro = """It is crucial to keep customers and acquire new ones for business growth. Customer Retention Rate (CRR) 
               is a business metric that can be calculated for any given time to show how good a business is in keeping 
               and acquiring customers. To calculate this metric 3 variables are required:"""
    variables = """
    - BC: Number of customers at the begining of the target period  
    - NC: Number of customers acquired during the target period
    - EC: Number of customers at the end of the target period
                """
    
    formula = """<h3 style="color:#D2386C;text-align:center;"><strong>CRR = ((EC-NC)/BC) x 100</strong></h3>"""
    
    st.markdown(intro, unsafe_allow_html=True)
    st.markdown(variables, unsafe_allow_html=True)
    st.markdown(formula, unsafe_allow_html=True)
    st.markdown('---')
    
    st.header('Example & Calculation')
    scenario = """If the company X had 200 customers at the begining of last month then got 30 new customers during that month 
                  and had 180 customers at the end of the month they are losing customers. <br> Their retention rate is ((180-30)/200) x 100 = 75%"""
    st.markdown(scenario, unsafe_allow_html=True)
    st.write('Custom calculation')

    with st.form(key='my_form'):
        bc = st.text_input(label='Enter number of customers at the begining')
        nc = st.text_input(label='Enter number of new customers')
        ec = st.text_input(label='Enter number of customers at the end')
        submit_button = st.form_submit_button(label='Calculate the CRR')
        
        if submit_button:
            try:
                crr = calculate_crr(bc, nc, ec)
                if crr == 'Not possible':
                    st.error("The customers at the end can't be greater than the customers at the begining plus the new customers.")
                    
                else:
                    st.write(f"Your Customer Retention Rate is {crr}  %")
            except Exception as e:
                st.error('Something went wrong, make sure the above fields are filled correctly!')
    
    st.markdown('---')
    st.header('Interpretation')
    interpretation = """According to [Salesforce](https://www.salesforce.com/ap/resources/articles/customer-retention-rate/) the most ideal                       rate would be 100% which means that the business didn't loose any customer or the number of lost customers equals the
                      number of new customers."""
    
    rate_analysis = """
            |Rate (%)| Description|
            |:---| :----|
            |Less than 0|You lose some new and old customers|
            |0 to 99|You don't retain a portio of old and new customers|
            |100|You keep all old and new customers|
        """
    
    st.markdown(interpretation, unsafe_allow_html = True)
    st.markdown(rate_analysis)
