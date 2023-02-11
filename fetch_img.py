from requests import get
from wget import download

# cat_image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/2880px-Cat_August_2010-4.jpg'
cat_image_url = 'https://apod.nasa.gov/apod/image/2302/Rcw58_Selby_960.jpg'

response = get(cat_image_url)

# This doesn't work with the cat_image_url, but works with NASA's jpg
# I assume there is something related with the way the image is formatted
# it downloads the file, but can't correctly render

# wb stands for write binary
with open('cat_image.jpg', 'wb') as file:
    file.write(response.content)

# wget correctly downloads the image, but only for the first time.
# would need to manually check if image exists, and delete it before executing this code
# download(cat_image_url, out='cat_image.jpg')


