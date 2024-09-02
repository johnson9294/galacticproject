import requests #使用 Python 網路爬蟲抓取網頁內容。首先，你需要抓取網頁內容。這裡是一個簡單的示例，使用 BeautifulSoup 抓取書籍介紹頁面：
from bs4 import BeautifulSoup

def fetch_webpage_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_webpage_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.find('title').text
    description = soup.find('meta', {'name': 'description'})['content']
    return title, description

url = 'https://www.books.com.tw/products/0010985418'
html_content = fetch_webpage_content(url)
if html_content:
    title, description = parse_webpage_content(html_content)
    print(f'Title: {title}')
    print(f'Description: {description}')


import spacy #使用 NLP 技術分析文章內容。接下來，你可以使用 NLP 技術來分析文章內容並提取所需信息。以下是使用 spaCy 的簡單示例：

nlp = spacy.load('en_core_web_sm')

def analyze_content(content):
    doc = nlp(content)
    # 分析內容並提取所需信息
    keywords = [token.text for token in doc if token.is_alpha]
    return keywords

description = "Your fetched description text here"
keywords = analyze_content(description)
print(keywords)


import requests
import json

NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_TOKEN = "secret_bo2NWzC9O0EbwlgWMQ2YoOkfpK5rpCQghR5B202ELrf"
DATABASE_ID = "fed1e473959746cb8658c3b3cb29efeb"

def create_page_in_notion(title, description):
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }

    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {"title": [{"text": {"content": title}}]},
            "Description": {"rich_text": [{"text": {"content": description}}]}
        }
    }

    response = requests.post(NOTION_API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("Page created successfully in Notion")
    else:
        print(f"Failed to create page. Status code: {response.status_code}")

create_page_in_notion(title, description)


