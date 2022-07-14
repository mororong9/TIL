word = input('enter:')
result = ''
for i in word:
    result+=chr(ord(i)+32)
print(result)