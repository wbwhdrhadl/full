import openai
from IPython.display import Image, display

response = openai.Image.create(
    prompt="Happy robots playing in the playground",
    n=1,
    size="512x512"
)

for data in response['data']:
    image_url = data['url']
    print(image_url)
    display(Image(url=image_url))

    print(image_url.split("?")[0].split("/")[-1])