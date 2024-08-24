# string 字串
helloworld="Hello World" #左邊是變數，第一個字必須要是字母
hellopython="Hello Python" #右邊是變數值，也是字串
# number 數字
a=100
b=1
#print
print(helloworld) #xxxx()是一個函式
print(a+b)
# array 陣列
hello=[helloworld, hellopython, a, 200, "100"] #變數,變數,數字,數字,字串
print(hello[0]+ " " + hello[1])
print(hello[2] + hello[3]) 
print(hello[0] + str(hello[2])) #用str將數字轉換成字串，才印得出來 Hello World100
print(str(hello[3]) + (hello[4])) #[4]本身就是字串 不用轉str 200100
print(hello[3] + int(hello[4])) #用int把(hello[4])字串轉換成數字，才能運算 300
# for loop 迴圈
# function 自訂函數
