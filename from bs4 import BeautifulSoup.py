from bs4 import BeautifulSoup
import requests

# 定義要抓取的網頁 URL
url = 'https://medium.com/70cc/%E7%82%BA%E4%BB%80%E9%BA%BC%E6%88%91%E8%A6%81%E7%94%B3%E8%AB%8B%E8%87%AA%E5%AD%B8-%E4%BE%86%E8%87%AA%E5%9C%A8%E5%AD%B8%E9%AB%98%E4%BA%8C%E7%94%9F%E7%9A%84%E6%83%B3%E6%B3%95-4ce0779f2605'

# 發送 GET 請求以獲取網頁內容
response = requests.get(url)

# 確保請求成功
if response.status_code == 200:
    # 解析 HTML 內容
    soup = BeautifulSoup(response.content, 'html.parser')

    # 排除不需要的元素，例如廣告、導航欄、頁尾等
    for element in soup(['aside', 'footer', 'nav', 'script', 'style', 'header']):
        element.decompose()  # 完全移除元素及其內容

    # 嘗試從 <article> 標籤中提取內容
    article = soup.find('article')
    if article:
        content = article.get_text(separator='\n', strip=True)
    else:
        # 如果沒有 <article>，則嘗試從最大的 <div> 標籤提取
        divs = soup.find_all('div')
        largest_div = max(divs, key=lambda div: len(div.get_text(separator='\n', strip=True)))
        content = largest_div.get_text(separator='\n', strip=True)

    # 打印或處理文本
    print(content)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
