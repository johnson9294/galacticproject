#練習2_迴圈

# a=100
# b=1
# hello=["helloworld", "hellopython", a, b, 200, "100"] #變數,變數,數字,數字,字串
# print(len(hello)) # 6 個

# print(hello[0])
# print(hello[1])
# print(hello[2])
# print(hello[0:3])
# for i in range(0,3): # 把range0~3以前的帶入i(C語言的作法)
#     print(hello[i]) # 印出指定範圍的值

# for i in hello:
#     print(i) #印出所有值

# numbers = [1,2,3,4,6]
# total = 0  # total宣告在外，正確做法
# for number in numbers:
#     #print(number)
#     # total = 0 + numbers[0] -> 1
#     # total = 2 + numbers[1] -> 3
#     # total = 3 + numbers[2] -> 6
#     # total = 10 + numbers[3] -> 10
#     # total = 10 + numbers[4] -> 16
#     total = total + number
#     print(total)

# for number in numbers:
#     #print(number)
#     # total = 0 + numbers[0] -> 1
#     # total = 0 + numbers[1] -> 2
#     # total = 0 + numbers[2] -> 3
#     # total = 0 + numbers[3] -> 4
#     # total = 0 + numbers[4] -> 6
#     total = 0  # total宣告在內，每次運算完歸零
#     total = total + number
#     print(total) 

numbers = [1,2,3,4,6]
total = 0  # total宣告在外，正確做法
time = 1
for number in numbers:
    if time > 3: 
        break  # 停下程式
    #print(number)
    # total = 0 + numbers[0] -> 1
    # total = 2 + numbers[1] -> 3
    # total = 3 + numbers[2] -> 6
    # total = 10 + numbers[3] -> 10
    # total = 10 + numbers[4] -> 16
    total = total + number
    time = time + 1
print(total)


