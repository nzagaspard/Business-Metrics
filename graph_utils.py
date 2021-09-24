import plotly.express as px
import plotly.graph_objects as go

def nps_fig(nps):
    positive = [{'range': [0, 30], 'color': '#99ff99'},
                  {'range': [30, 70], 'color': '#33ff33'},
                 {'range': [70, 100], 'color': '#00cc00'}]
    negative = [{'range': [0, -30], 'color': '#ffe6e6'},
                  {'range': [-30, -70], 'color': '#ff8080'},
                 {'range': [-70, -100], 'color': '#ff3333'}]
    nps_fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = nps,
        number = {'suffix': '% '},
        title = {'text': "Net Promoter Score (NPS)"},
        gauge = {'steps': positive if nps > 0 else negative,
            'axis': {'range': [0, 100] if nps > 0 else [-100, 0]}, 
            'bar' :  {'color': 'black'},
            'threshold' : {'line': {'color': 'black', 'width': 4}, 
                           'thickness': 1, 'value': nps}},
        domain = {'x': [0, 1], 'y': [0, 1]}))

    nps_fig.update_layout(title = dict(x=0.5, y = 0.9, yanchor = 'top', xanchor = 'center'),
                      titlefont = {'family': 'Arial','size':16, 'color':'rgb(37,37,37)'},  
                      margin = {'l':5, 'r':5, 'b':20, 't':35}, paper_bgcolor='rgb(248, 248, 255)', 
                      showlegend = False, height = 300, width = 500)

    return nps_fig

def distribution_fig(stats):
    stats = stats.reset_index()
    stats_fig = px.pie(stats, values= '%', names='index', hole = 0.4,
                    title = "Categories Distribution", color = 'index',
                    color_discrete_map = {'Promoters':'forestgreen', 'Detractors':'red','Passives':'yellow'})
    
    stats_fig.update_traces(textposition='inside',texttemplate = "%{label} <br> %{percent:.2%f}", hovertemplate='<b>%{label} </b> <br> Number of People: %{value:,}<br> Percentage: %{percent:.2%f}')
    stats_fig.update_layout(title = dict(x=0.5, y = 0.99, yanchor = 'top', xanchor = 'center'),
                             titlefont = {'family': 'Arial','size':16, 'color':'rgb(37,37,37)'},  margin = {'l':5, 'r':5, 'b':20, 't':25},
                            paper_bgcolor='rgb(248, 248, 255)', showlegend = False, height = 300, width = 300)
    
    return stats_fig