import requests
import csv
import json

# OpenAI API 的 URL 和你的 API 密钥
openai_api_url = "https://galacticproject-openai.openai.azure.com/openai/deployments/galacticproject-OpenAI/completions?api-version=2022-12-01"
api_key = "YOUR_API_KEY"

# 你要分析的文章内容
article_text = "你的文章内容在这里"

# 发送请求到 OpenAI API
response = requests.post(
    openai_api_url,
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "text-davinci-003",
        "prompt": f"Analyze this article: {article_text}\n\nProvide the following details:\n提及內容:\n這篇文章想溝通的對象:\n發表者角色:\n資料類別:\n內容所屬教育階段或形態:\n學習領域:\n發布時間:\n期程:\n篇幅:",
        "max_tokens": 1500
    }
)

# 确保请求成功
if response.status_code == 200:
    response_json = response.json()
    analyzed_text = response_json["choices"][0]["text"]

    # 分析 API 返回的文本
    data = {
        "Name": "Example Article",
        "LINK": "http://example.com",
        "提及內容": {
            "休學": "提及內容" in analyzed_text,
            "動機": "動機" in analyzed_text,
            "升學": "升學" in analyzed_text,
            "困惑": "困惑" in analyzed_text,
            "學習資源": "學習資源" in analyzed_text,
            "審議(書)": "審議(書)" in analyzed_text,
            "審議(面)": "審議(面)" in analyzed_text,
            "心路轉變": "心路轉變" in analyzed_text,
            "申請計畫(內容)": "申請計畫(內容)" in analyzed_text,
            "申請計畫(動機)": "申請計畫(動機)" in analyzed_text,
            "申請計畫(方式)": "申請計畫(方式)" in analyzed_text,
            "申請計畫(資源)": "申請計畫(資源)" in analyzed_text,
            "訪視": "訪視" in analyzed_text,
            "跨體制": "跨體制" in analyzed_text,
            "轉學": "轉學" in analyzed_text,
            "類休學": "類休學" in analyzed_text
        },
        "這篇文章想溝通的對象": [],
        "發表者角色": [],
        "資料類別": [],
        "內容所屬教育階段或形態": [],
        "學習領域": "",
        "發布時間": "",
        "期程": "",
        "篇幅": 0
    }

    # 解析提及內容
    lines = analyzed_text.split('\n')
    for line in lines:
        if "這篇文章想溝通的對象:" in line:
            data["這篇文章想溝通的對象"] = line.split(':')[1].strip().split(', ')
        elif "發表者角色:" in line:
            data["發表者角色"] = line.split(':')[1].strip().split(', ')
        elif "資料類別:" in line:
            data["資料類別"] = line.split(':')[1].strip().split(', ')
        elif "內容所屬教育階段或形態:" in line:
            data["內容所屬教育階段或形態"] = line.split(':')[1].strip().split(', ')
        elif "學習領域:" in line:
            data["學習領域"] = line.split(':')[1].strip()
        elif "發布時間:" in line:
            data["發布時間"] = line.split(':')[1].strip()
        elif "期程:" in line:
            data["期程"] = line.split(':')[1].strip()
        elif "篇幅:" in line:
            data["篇幅"] = int(line.split(':')[1].strip())

    # 定义 CSV 文件的列
    columns = ["Name", "LINK", "提及內容", "這篇文章想溝通的對象", "發表者角色", "資料類別", "內容所屬教育階段或形態", "學習領域", "發布時間", "期程", "篇幅"]

    # 写入 CSV 文件
    with open('analysis_results.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns)

        writer.writeheader()
        # 将嵌套字典转换为字符串
        data["提及內容"] = json.dumps(data["提及內容"], ensure_ascii=False)
        data["這篇文章想溝通的對象"] = ",".join(data["這篇文章想溝通的對象"])
        data["發表者角色"] = ",".join(data["發表者角色"])
        data["資料類別"] = ",".join(data["資料類別"])
        data["內容所屬教育階段或形態"] = ",".join(data["內容所屬教育階段或形態"])

        writer.writerow(data)
else:
    print(f"Error: {response.status_code} - {response.text}")
