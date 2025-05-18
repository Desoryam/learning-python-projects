from newsapi import NewsApiClient
from bs4 import BeautifulSoup
# Init
newsapi = NewsApiClient(api_key='3d559f9483cc428eb4b0ebf33d524e1c')

# # /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2025-04-02',
                                      to='2025-04-30',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()
# print(all_articles)
print(sources)
# soup=BeautifulSoup(top_headlines,"html.parser")
# print(soup.prettify())
# for i in top_headlines:
#     for w in i:
#         print(w)