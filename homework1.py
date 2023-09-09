res = []
index = 0
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        res.append(i)

# res1 = []
# for num in range(2001, 3201, 2):
#     if num % 7 == 0 and num % 5 != 0:
#         res1.append(num)

# res2 = []
# for num in range(2001, 3201, 14):
#     if num % 5 != 0:
#         res2.append(num)
#     if num + 7 <= 3200 and (num + 7) % 5 != 0:
#         res2.append(num + 7)

res3 = []
for num in range(2000, 3201, 5):
    for i in range(1, 5):
        if (num + i) % 7 == 0:
            res3.append(num + i)

res4 = []
for num in range(2002, 3201, 7):
    if num % 5 != 0:
        res4.append(num)

# print('res1:', res1 == res)
# print('res2:', res2 == res)
print('res3:', res3 == res)
print('res4:', res4 == res)

class myclass:
    def __init__(self) -> None:
        self.string = ''
    def getString(self):
        string = input()
        self.string = string
    def printString(self):
        if self.string:
            print(self.string)
    
test = myclass()
test.getString()
test.printString()

