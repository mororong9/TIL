result={}
word='bananan'
for char in word:
    result[char]=result.get(char,0)+1
print(result)

for key in result:
    print(key, result[key])