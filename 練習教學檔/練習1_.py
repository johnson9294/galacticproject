# 這是練習文件
# string 字串
#helloworld="Hello World" #左邊是變數，第一個字必須要是字母
#hellopython="Hello Python" #右邊是變數值，也是字串
# number 數字
#a=100
#b=1
# print
#print(helloworld) #xxxx()是一個函式
#print(a+b)
# array 陣列
#hello=[helloworld, hellopython, a, 200, "100"] #變數,變數,數字,數字,字串
#print(hello[0]+ " " + hello[1])
#print(hello[2] + hello[3]) 
#print(hello[0] + str(hello[2])) #用str將數字轉換成字串，才印得出來 Hello World100
#print(str(hello[3]) + (hello[4])) #[4]本身就是字串 不用轉str 200100
#print(hello[3] + int(hello[4])) #用int把(hello[4])字串轉換成數字，才能運算 300
# 使用者輸入
# input_article = input("請輸入網址")
# if input_article:
#   print(input_article)
# else:
#   print("沒有資料")

#input_article = input("請輸入數字")
#print(type(input_article)) #檢查並印出輸入的類型

#if input_article and type(input_article) == int: # 值是存在的而且是整數 ==是比較的意思
  #input_article = int(input_article) #更新變數字串成數字
  #print(type(input_article)) #檢查並印出輸入的類型
  #if input_article > 10:  #有冒號下一行就要縮排
    #print("你的值大於 10")
  #else:
    #print("你的值小於 10")
#else:
  #print("沒有資料")

# 2024-9-1~2 學習進度 https://youtu.be/zdMUJJKFdsU?si=t5UR519l4aSWUXS0&t=6845
# list 列表和列表的基本涵式
list = [1,2,3] # 用中括號來包住資料
# tuple 元組
tuple = (1,2,3) # 用小括號來包住資料
# tuple不同於list，資料不能被新程式碼新增、刪除、變更，適合儲存經緯度等資料
# function 涵式
def hello(name, age): # 定義涵式
  text = ""
  if age < 18:
    text = "你還沒成年"
  elif age > 18 and age < 65:  # 除此除外
    text = "你成年了"
  else: # 以外
    text = "你退休了" 
  return [name, age, text] #回傳，還不太懂的部分。應該是把值帶入下行程式碼的意思

reply = hello("小白",87) # 呼叫涵式並填入資料
print("hello"+ reply[0] + "你今年" + str(reply[1]) + "歲" + reply[2])# return 可以接 none 
# return 後的程式碼不會被執行(那一縮排)
# if else

# 2024-9-2練習題 http://35.72.96.204/ShowProblem?problemid=a017
# 內容
# 某校為了不讓學生互相比較成績，所以成績上記錄的是成績等第而不是分數，它的規則如下：

# 90分(含)~100分(含)為A等
# 80分(含)~90分(不含)為B等
# 70分(含)~80分(不含)為C等
# 60分(含)~70分(不含)為D等
# 不滿60分者為E等
# 現在給你一個成績，請你判斷它是哪一個等第。

# 輸入說明
# 輸入一個整數 N (0<=N<=100) 代表要判斷的成績。

# 輸出說明
# 請輸出其對應的等第。

# 範例輸入 #1
# 95
# 範例輸出 #1
# A80
# 範例輸入 #2
# 85
# 範例輸出 #2
# B
# 讀取輸入並轉換為整數
score = int(input("請輸入成績")) #GPT輔助

def get_grade(score): # 定義一個函數來判斷成績等第
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "E"
grade = get_grade(score) # 呼叫函數並取得等第
print("你的成績等第為" + grade) # 輸出等第

# for loop 迴圈
# function 自訂函數

