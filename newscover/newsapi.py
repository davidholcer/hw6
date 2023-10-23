import json
import requests
import logging
from datetime import datetime

logger=logging.getLogger(__name__)

# with open('config.json', 'r') as config_file:
#     config = json.load(config_file)
# GLOBAL_API_KEY = config['api_key']


# example fetch: https://newsapi.org/v2/everything?q=Apple&from=2023-10-23&sortBy=popularity&apiKey=API_KEY
NEWS_QUERY_STRING_TEMPLATE="https://newsapi.org/v2/everything?q={}&from={}&sortBy=popularity&apiKey={}"

def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    # Get the current date
    current_date = datetime.now()
    new_date = current_date - timedelta(days=lookback_days)
    # Format the new date if needed
    f_date = new_date.strftime("%Y-%m-%d")

    #join the keywords by AND to pass them into the api
    k_words="AND".join(news_keywords);

    query_string=NEWS_QUERY_STRING_TEMPLATE.format(k_words,f_date,api_key)


    # with open(output_path_json,'w') as f:
    #     json.dump(episodes,f,indent=4)

if __name__ == "__main__":
