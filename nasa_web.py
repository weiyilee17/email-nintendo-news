from streamlit import title, write, image
from os import getenv
from requests import get

NASA_API_KEY = getenv('NASA_API_KEY')

response = get('https://api.nasa.gov/planetary/apod', params={
    'api_key': NASA_API_KEY
}).json()

image_url = response['url']

image_content = get(image_url).content

with open('nasa_image.jpg', 'wb') as file:
    file.write(image_content)

title(response['title'])
image('nasa_image.jpg')
write(response['explanation'])
