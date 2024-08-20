import csv

# 從 CSV 檔案讀取資料並打印標題行
def read_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        print("CSV 標題行:", csv_reader.fieldnames)  # 打印 CSV 標題行
        for row in csv_reader:
            data.append(row)
    return data

# 主函數
def main():
    file_path = r"C:\Users\johns\Documents\code\project\星河計畫人工智慧版\article_analysis_updated.csv"
    data = read_csv(file_path)
    # 這裡暫時不調用 create_notion_page，只是為了確保我們能打印出標題行
    for row in data:
        print(row)

if __name__ == "__main__":
    main()
