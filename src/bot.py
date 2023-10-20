import tweepy
from dotenv import load_dotenv
import os
import gdown
from time import strftime

class BOT:

    def __init__(self):
        load_dotenv()
        consumer_key = os.getenv("CONSUMER_KEY")
        consumer_secret = os.getenv("CONSUMER_SECRET")
        access_token = os.getenv("ACCESS_TOKEN")
        access_secret = os.getenv("ACCESS_TOKEN_SECRET")
        bearer_token = os.getenv("BEARER_TOKEN")
        self.client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_secret,
            bearer_token=r"{}".format(bearer_token)
        )
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
        auth.set_access_token(
            access_token,
            access_secret
        )
        self.api = tweepy.API(auth)

    def post(self, data: dict):
        try:
            post = f"{data['title']}\n\nValor antigo: {data['oldprice']}\nValor novo: {data['price']}\n\nLink para a oferta: {data['link']}"
            imageLink = data['image']
            if imageLink != "":
                path = r'C:\Users\larip\OneDrive\Documentos\PBL\Curso-Twitter\src\tmp\{}.jpg'.format((data['date']).strftime("%Y-%m-%d_%H-%M-%S"))
                gdown.download(imageLink, path)
                media = self.api.media_upload(filename=path)
                self.client.create_tweet(text=post, media_ids=[media.media_id])
            else:
                self.client.create_tweet(text=post)

            return True
        except Exception as e:
            print(str(e))
            return False
