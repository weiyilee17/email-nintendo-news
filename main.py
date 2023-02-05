from requests import get
from os import getenv

from send_email import send_email

news_api_key = getenv('NEWS_API_KEY')

topic = 'nintendo'
news_url = 'https://newsapi.org/v2/everything'

query = {
    'q': topic,
    'from': '2023-01-05',
    'sortBy': 'publishedAt',
    'apiKey': news_api_key,
    # language : english prevents the unicode out of ascii range error, but making send email more robust is still worth it
    'language': 'en'
}

request = get(news_url, params=query)
response = request.json()

titles_descriptions_and_links = ''

for single_article in response['articles'][:20]:
    if single_article['title'] and single_article['description']:
        titles_descriptions_and_links += f'{single_article["title"]}\n'
        titles_descriptions_and_links += f'{single_article["description"]}\n'
        titles_descriptions_and_links += f'{single_article["url"]}\n\n'

email_content = f"""\
{titles_descriptions_and_links}
"""

send_email(f"Today's news related to {topic} 1 month ago", email_content)
