import requests
import json
from bs4 import BeautifulSoup

# 設置你的 GPT-4 API Key 和端點
GPT4V_KEY = "dd95a9f7fdb046ccbb7125527b3d3798"
GPT4V_ENDPOINT = "https://galacticproject-openai.openai.azure.com/openai/deployments/galacticproject/chat/completions?api-version=2024-02-15-preview"

# 設置請求頭
headers = {
    "Content-Type": "application/json",
    "api-key": GPT4V_KEY,
}

# 爬取網站內容的函數
def fetch_website_content(url):
    response = requests.get(url)
    response.raise_for_status()  # 確保請求成功

    soup = BeautifulSoup(response.text, 'html.parser')
    # 根據網站的 HTML 結構提取內容，這裡假設網站內容在 <div class="content"> 中
    content = soup.find('div', class_='content').get_text()
    return content

# 設置爬取的網站 URL
url = "https://vocus.cc/article/5b5070e7fd89780001cbfc11"
content = fetch_website_content(url)

# 設置請求 payload
payload = {
    "messages": [
        {
            "role": "system",
            "content": (
                "這是針對臺灣的非學校型態實驗教育，也就是俗稱自學的資料庫，我希望藉此資料庫匯流和自學生有關的經驗、內容。\n\n"
                "規則如下\n\n"
                "Name:網站標題\n\n"
                "LINK:網站連結\n\n"
                "提及內容:休學:內容提到休學, 動機:內容提到申請者動機, 升學:內容提到升學, 困惑:作者在內容中留下問題, "
                "學習資源:內容提及作者的學習資源或如何使用之, 審議(書):內容提到書面的審議, 審議(面):內容提到審議的面談, "
                "心路轉變:內容提到作者的心路轉變, 申請計畫(內容):內容提到申請計畫書的學習內容, 申請計畫(動機):內容提到申請計畫的申請動機, "
                "申請計畫(方式):內容提到申請計畫的執行或學習方式, 申請計畫(資源):內容提到申請計畫所需的學習資源欄位, "
                "訪視:內容提到非學校型態實驗教育的審議委員訪視, 跨體制:內容橫跨高中、高職或專科學校, 轉學:內容提到轉學, 類休學:內容提到請假或請長假\n\n"
                "這篇文章想溝通的對象:外界, 學校, 家長, 教育局或審議委員, 自己\n\n"
                "發表者角色:同事/雇主/社會, 實驗教育工作者, 老師/學校, 自學家長, 自學生, 自學生友人/同儕\n\n"
                "資料類別:作者/人物, 內容, 匯流者, 社群, 社群(FB), 社群(IG), 社群(LINE), 網站\n\n"
                "內容所屬教育階段或形態:個人自學, 合作自學, 國中, 國小, 團體自學, 大專, 學校型態實教, 學校外, 機構自學, 社會, 高中\n\n"
                "學習領域:依照你分析到內容涉及的學習領域判斷，可以是多個領域，如果是多個領域請用逗號分開，例如:數學,設計,程式等等。\n\n"
                "發布時間:內容的發布時間\n\n"
                "期程:內容提及的自學計畫實施的時間，例如一學期、一學年、三年等等\n\n"
                "篇幅:分析內容的篇幅大約要花多少時間看完\n\n"
                "如果以上有無法辨識的內容，請留空"
            )
        },
        {
            "role": "user",
            "content": content
        }
    ],
    "temperature": 0.7,
    "top_p": 0.95,
    "max_tokens": 800
}

# 發送請求
try:
    response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # 如果請求返回了不成功的狀態碼，將引發 HTTPError
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# 處理回應
result = response.json()
print(json.dumps(result, indent=2, ensure_ascii=False))
