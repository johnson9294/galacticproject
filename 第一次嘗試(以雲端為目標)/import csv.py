import csv
from notion_client import Client

# 初始化 Notion API 客戶端
notion = Client(auth="") #這裡設定填入.env裡的金鑰

# 設定 Notion 資料庫 ID
database_id = "fed1e473959746cb8658c3b3cb29efeb"

# 從 CSV 檔案讀取資料
def read_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        print("CSV 標題行:", csv_reader.fieldnames)  # 打印 CSV 標題行
        for row in csv_reader:
            data.append(row)
    return data

# 建立 Notion 頁面
def create_notion_page(database_id, row):
    notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "標題": {"title": [{"text": {"content": row["標題"]}}]},
            "發表者角色": {"multi_select": [{"name": row["發表者角色"]}]},
            "提及內容": {"multi_select": [{"name": item.strip()} for item in row["提及內容"].split(",")]},
            "內容所屬教育階段或形態": {"multi_select": [{"name": item.strip()} for item in row["內容所屬教育階段或形態"].split(",")]},
            "這篇文章想溝通的對象": {"multi_select": [{"name": item.strip()} for item in row["這篇文章想溝通的對象"].split(",")]},
            "學習領域": {"multi_select": [{"name": item.strip()} for item in row["學習領域"].split(",")]},
            "篇幅": {"rich_text": [{"text": {"content": row["篇幅"]}}]},
            "簡述": {"rich_text": [{"text": {"content": row["簡述"]}}]},
            "期程": {"rich_text": [{"text": {"content": row["期程"]}}]},
            "發布時間": {"date": {"start": row["發布時間"]}},
            "LINK (網站連結)": {"url": row["LINK (網站連結)"]},
            "資料類別": {"multi_select": [{"name": item.strip()} for item in row["資料類別"].split(",")]},
        }
    )

# 主函數
def main():
    file_path = r"C:\Users\johns\Documents\code\project\星河計畫人工智慧版\article_analysis_updated.csv"
    data = read_csv(file_path)
    for row in data:
        create_notion_page(database_id, row)

if __name__ == "__main__":
    main()