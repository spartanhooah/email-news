import requests
import os

from send_email import send_email

api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

content = requests.get(url).json()

message = f"""\
Subject: News digest

"""

for article in content["articles"]:
    message = message + "\n"
    if article["title"]:
        message = message + article["title"] + "\n"

    if article["description"]:
        message = message + article["description"] + "\n"

send_email(message)
