import requests
from urllib.parse import urlparse
import pandas as pd

keyword = 'e편한세상'
displaynum = str(100)
text_news = []
text_blog = []

for i in range(1,1000,100):
    startnum = str(i)
    url_news = 'https://openapi.naver.com/v1/search/news.json?query=' + keyword + '&display='+ displaynum + '&start='+startnum
    result_news = requests.get(urlparse(url_news).geturl(),
                      headers = {'X-NAver-Client-Id':'cX2fkCKhbGiMgomkCYbv',
                                 'X-Naver-Client-Secret':'yjYNiqHCjQ'} )

    url_blog = 'https://openapi.naver.com/v1/search/blog?query=' + keyword + '&display=' + displaynum + '&start=' + startnum
    result_blog = requests.get(urlparse(url_blog).geturl(),
                               headers={'X-NAver-Client-Id': 'cX2fkCKhbGiMgomkCYbv',
                                        'X-Naver-Client-Secret': 'yjYNiqHCjQ'})

    json_news = result_news.json()
    json_blog = result_blog.json()

    for item in json_news['items']:
        text_news.append(item['description'])

    for item in json_blog['items']:
        text_blog.append(item['description'])


#text1 = text.replace('<b>','').replace('</b>','' )
text1_news = pd.DataFrame(text_news)
text1_blog = pd.DataFrame(text_blog)

def text_clear (text_old):
    text_new = text_old.applymap(lambda x : x.replace('\u2219','').replace('\u2022','').replace('\xa0','').replace('\u200b','').
                       replace('\u2027','').replace('\u2024','').replace('<b>','').replace('</b>','' ))
    return text_new

text1_news = text_clear(text1_news)
text1_blog = text_clear(text1_blog)

print(text1_news.head(10))

text1_blog.to_csv('D:/Python/Crawling/e편한세상_naver_blog.csv', encoding='cp949')
text1_news.to_csv('D:/Python/Crawling/e편한세상_naver_news.csv', encoding='cp949')
    #print(item['title'].replace('<b>','').replace('</b>','' ), item['link'])

#print(json_obj['display'])
#print(json_obj['items'])

