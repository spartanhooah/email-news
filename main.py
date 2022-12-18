import requests
import os

from send_email import send_email

api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/top-headlines?language=en&pageSize=20&apiKey={api_key}"

content = requests.get(url).json()

message = "Subject: News digest\n"

for article in content["articles"]:
    message = message + "\n"

    if article["title"]:
        message = message + article["title"] + "\n"

    if article["description"]:
        message = message + article["description"] + "\n"

    if article["url"]:
        message = message + article["url"] + "\n"

send_email(message)
