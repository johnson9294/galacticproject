# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(beautifulsoup) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints


import azure.functions as func
import logging
from bs4 import BeautifulSoup
bp = func.Blueprint() 


@bp.route(route="beautifulsoup", auth_level=func.AuthLevel.FUNCTION)
def beautifulsoup(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    soup = BeautifulSoup(name, 'html.parser')

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

    if name:
        return func.HttpResponse(content)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )