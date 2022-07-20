word='banana'
result={}
for char in word:
    if not char in result:
        result[char]=1
    else:
        result[char]=result[char]+1
print(result)

