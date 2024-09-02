import requests
import json

# 設置API端點和API密鑰
api_url = "https://galacticproject-OpenAI.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2023-03-15-preview"

# 設置請求頭
headers = {
    "Content-Type": "application/json",
    "api-key": "Bearer fccce143b0364755905cdd31933afd6d"
    
}

# 設置請求體
data = {
    "model": "text-davinci-003",
    "prompt": "Translate the following English text to French: \"Hello, how are you?\"",
    "max_tokens": 60
}

# 發送POST請求
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# 檢查請求是否成功
if response.status_code == 200:
    # 請求成功，打印回應內容
    print("Response:", response.json())
else:
    # 請求失敗，打印錯誤信息
    print("Error:", response.status_code, response.text)
