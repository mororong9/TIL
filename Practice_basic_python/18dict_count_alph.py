word=input()
dic = {}

for chr in word:
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr] = 1
print(dic)
