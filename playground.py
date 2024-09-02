import os
import requests
import base64

# Configuration
GPT4V_KEY = "dd95a9f7fdb046ccbb7125527b3d3798"
IMAGE_PATH = r"C:\Users\johns\Documents\code\project\星河計畫人工智慧版\test image.png"
encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
headers = {
    "Content-Type": "application/json",
    "api-key": GPT4V_KEY,
}

# Payload for the request
payload = {
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "這是針對臺灣的非學校型態實驗教育，也就是俗稱自學的資料庫，我希望藉此資料庫匯流和自學生有關的經驗、內容。\n\n規則如下\n\nName:網站標題\n\nLINK:網站連結\n\n提及內容:休學:內容提到休學, 動機:內容提到申請者動機, 升學:內容提到升學, 困惑:作者在內容中留下問題, 學習資源:內容提及作者的學習資源或如何使用之, 審議(書):內容提到書面的審議, 審議(面):內容提到審議的面談, 心路轉變:內容提到作者的心路轉變, 申請計畫(內容):內容提到申請計畫書的學習內容, 申請計畫(動機):內容提到申請計畫的申請動機, 申請計畫(方式):內容提到申請計畫的執行或學習方式, 申請計畫(資源):內容提到申請計畫所需的學習資源欄位, 訪視:內容提到非學校型態實驗教育的審議委員訪視, 跨體制:內容橫跨高中、高職或專科學校, 轉學:內容提到轉學, 類休學:內容提到請假或請長假\n\n這篇文章想溝通的對象:外界, 學校, 家長, 教育局或審議委員, 自己\n\n發表者角色:同事/雇主/社會, 實驗教育工作者, 老師/學校, 自學家長, 自學生, 自學生友人/同儕\n\n資料類別:作者/人物, 內容, 匯流者, 社群, 社群(FB), 社群(IG), 社群(LINE), 網站\n\n內容所屬教育階段或形態:個人自學, 合作自學, 國中, 國小, 團體自學, 大專, 學校型態實教, 學校外, 機構自學, 社會, 高中\n\n學習領域:依照你分析到內容涉及的學習領域判斷，可以是多個領域，如果是多個領域請用逗號分開，例如:數學,設計,程式等等。\n\n發布時間:內容的發布時間\n\n期程:內容提及的自學計畫實施的時間，例如一學期、一學年、三年等等\n\n篇幅:分析內容的篇幅大約要花多少時間看完\n\n如果以上有無法辨識的內容，請留空"
        }
      ]
    }
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 800
}

GPT4V_ENDPOINT = "https://galacticproject-openai.openai.azure.com/openai/deployments/galacticproject/chat/completions?api-version=2024-02-15-preview"

# Send request
try:
    response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# Handle the response as needed (e.g., print or process)
print(response.json())