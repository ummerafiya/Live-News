# app.py
from flask import Flask, render_template
import requests

app = Flask(__name__)

# ✅ Your NewsAPI key (replace if you get one later)
NEWS_API_KEY = 'your_real_api_key_here'

# ✅ Toggle this to True to use mock data (offline/dev mode)
USE_MOCK_DATA = True

# ✅ Example mock news data
MOCK_ARTICLES = [
    {
        "title": "Python 3.13 Released with Cool New Features",
        "description": "The Python Software Foundation has released Python 3.13...",
        "url": "https://www.python.org",
        "urlToImage": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
    },
    {
        "title": "NASA Discovers Water on Mars Again",
        "description": "In a stunning development, NASA scientists report finding water...",
        "url": "https://mars.nasa.gov",
        "urlToImage": "https://mars.nasa.gov/system/news_items/main_images/9444_PIA25834-FigureA-web.jpg"
    },
    {
        "title": "OpenAI Announces GPT-5 Launch",
        "description": "OpenAI officially launches GPT-5 with multimodal capabilities...",
        "url": "https://openai.com",
        "urlToImage": "https://openai.com/content/images/2022/05/openai-avatar.png"
    }
]

@app.route('/')
def home():
    if USE_MOCK_DATA:
        articles = MOCK_ARTICLES
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            articles = response.json().get('articles', [])
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error fetching live news: {e}")
            articles = []

    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)