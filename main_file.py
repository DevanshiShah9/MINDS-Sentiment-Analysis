import time
from data_collection import *
from sentiment_analysis import *
from result_plot import *

start = time.time()
news_df=add_articles()
convert_to_json(news_df)
news_df=sentiment_analyzer(news_df)
plot_graph(news_df)
end = time.time()
total_time = (end - start)
print("Total time taken is",total_time)