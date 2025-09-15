# 📰 Live News App

A simple Flask web application that displays live news headlines using the [NewsAPI.org](https://newsapi.org/) service.

Easily toggle between **live news** and **mock data** for offline development or testing.

## 🚀 Features

- 🧠 Displays real-time top headlines from the U.S.
- 🧪 Mock data mode for development (no API key required)
- 💡 Clean, responsive UI with news cards
- 🔧 Easy setup with Flask and Python

## 🛠️ Tech Stack

- **Backend:** Python + Flask
- **Frontend:** HTML + CSS (Jinja2 template)
- **API:** [NewsAPI.org](https://newsapi.org/)

## 📁 Project Structure

live-news-app/
├── app.py
├── templates/
│ └── index.html  
 └── README.md

## 🧰 Setup Instructions

### 1. Clone the Repository

````bash
git clone https://github.com/ummerafiya/Live-News.git
cd live-news-app

2. Create a virtual environment

 python3 -m venv venv
source venv/bin/activate          #macOS/Linux
venv\Scripts\activate             # On Windows

3.Install Dependencies

pip install flask

4.Run the application

python app.py

5.Open in browser

Go to 👉 http://127.0.0.1:5000/




Example Input and Output:

## 🧪 Input Type

The app doesn’t require user input from a form or API call. Instead, it fetches news automatically based on:

- A hardcoded country (`us`) in `app.py`
- Whether you're using:
  - `USE_MOCK_DATA = True` (offline mode)
  - `USE_MOCK_DATA = False` (live NewsAPI mode)


### ✅ Example 1: Mock Data Output (`USE_MOCK_DATA = True`)

This is the default when testing or running offline.

#### 📄 Mock Input (from `MOCK_ARTICLES` list)

```python
MOCK_ARTICLES = [
    {
        "title": "Python 3.13 Released with Cool New Features",
        "description": "The Python Software Foundation has released Python 3.13...",
        "url": "https://www.python.org",
        "urlToImage": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
    },
    ...
]


Output

🖼️ Image: Python logo
📰 Title: Python 3.13 Released with Cool New Features
📃 Description: The Python Software Foundation has released Python 3.13...
🔗 Link: https://www.python.org



📄 License

This project is licensed under the MIT License.
