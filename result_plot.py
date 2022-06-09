import plotly.express as px


def plot_graph(news_df):
    fig = px.scatter(data_frame=news_df,y='sentiment',color='sentiment')
    fig.show()