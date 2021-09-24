import streamlit as st
from data_utils import get_sample_data, process_data
from graph_utils import distribution_fig, nps_fig

st.set_page_config(page_title="Business Metrics",page_icon=":bar_chart:")

#Application
hide_st_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

title = """<div style="background-color:#00A170;padding:1px">
            <h1 style="color:white;text-align:center;">Net Promoter Score (NPS)</h1></div>"""

st.markdown(title, unsafe_allow_html=True)

st.header('Overview')
description = """Shows the percentage difference between the people who are likely to keep buying/using, promote, recommend or refer your products/services and those who may not. To get the data to measure this metric you can just ask your customers a question like:<br> **How likely are you to recommend us to your friends on a scale of 0 to 10?**"""
st.write(description, unsafe_allow_html=True)


summary = """
            |Answer| Category| Description|
            |:---| :----| :---|
            |0 to 6| Detractors| Unhappy, Disrecommend|
            |7 or 8| Passive| Neutral, Uncommitted|
            |9 or 10| Promoters| Happy, Loyal, Recommend|
        """
st.markdown(summary)
formula = """<h3 style="color:#D2386C;text-align:center;"><strong>NPS = % Promoters - % Detractors </strong></h3>"""
st.markdown(formula, unsafe_allow_html=True)

st.header('Calculation')

demo_custom = st.radio('Choose My file to upload your custom file',['Demo','My file'])

if demo_custom == 'Demo':
    data = get_sample_data()
else:
    custom_file = st.file_uploader('Upload your file', type = ['csv','xlsx'])
    if custom_file is not None:
        data = pd.read_csv(customfile)
    else:
        data = None
    

#Dataframes
original, processed, statistics = st.beta_columns(3)
if data is not None:
    original.write('Sample Data')
    original.write(data)

    processed_data, stats, nps = process_data(data)

    processed.write('Categorized Data')
    processed.write(processed_data.set_index('CustId'))

    statistics.write('Summary')                
    statistics.write(stats)
    statistics.write(f'Net Promoter Score: {nps:.2f}%')

    #Figures
    stats_figure, nps_figure = st.beta_columns(2)

    stats_figure.plotly_chart(distribution_fig(stats))
    nps_figure.plotly_chart(nps_fig(nps), use_container_width=True)
