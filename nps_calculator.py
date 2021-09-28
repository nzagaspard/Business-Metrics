import streamlit as st
from data_utils import get_sample_data, process_data, read_file
from graph_utils import distribution_fig, nps_fig
import pandas as pd

def nps():    
    title = """<div style="background-color:#00A170;padding:1px">
                <h2 style="color:white;text-align:center;">Net Promoter Score (NPS) Calculator<br>👎🤬😐😊👍</h2></div>"""

    st.markdown(title, unsafe_allow_html=True)

    st.header('Overview')
    description = """NPS shows the percentage difference between the people who are likely to keep using, promote, recommend or refer your products/services and those who may not. To get the data to measure this metric you can just ask your customers a question like:<br> **How likely are you to recommend us to your friends on a scale of 0 to 10?**"""
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
        file_sample = st.checkbox('Check the accepted sample format!')
        if file_sample:
            st.image('file_sample_and_format.png')
        custom_file = st.file_uploader('Upload your file', type = ['csv','xlsx','xls','txt'])
        if custom_file is not None:
            try:
                data = read_file(custom_file)
            except:
                st.error('Something is wrong with your uploaded file. Tick on Check the accepted sample format!')
                data = None
        else:
            data = None

    #Dataframes
    original, processed, statistics = st.columns(3)
    if data is not None:
        original.write('Sample Data')
        original.write(data)

        processed_data, stats, nps = process_data(data)

        processed.write('Categorized Data')
        processed.write(processed_data)

        statistics.write('Summary')                
        statistics.write(stats)
        statistics.write(f'Net Promoter Score: {nps:.2f}%')

        #Figures
        stats_figure, nps_figure = st.columns(2)

        stats_figure.plotly_chart(distribution_fig(processed_data))
        nps_figure.plotly_chart(nps_fig(nps), use_container_width=True)

        st.header('Interpretation')

        st.write("""The NPS can be a -100% if all customers are Detractors and 100% if all customers are Promoters. 
    According to [Relently](https://www.retently.com/blog/good-net-promoter-score/) the NPS can be interpreted as follows:""")
        results_summary ="""|Score|Description|
                            |:---| :----|
                            |-100 - 0|Need improvement|
                            |0 - 30|Good|
                            |30 - 70|Great|
                            |70 - 100| Excellent|"""
        st.write(results_summary, unsafe_allow_html=True)
        st.write("""**People should also consider looking the average NPS of their industry to see if they are doing better than the average of the industry.**""")