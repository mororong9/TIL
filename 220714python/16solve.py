word='apple'
count=0
for char in word:
    if char in 'aieou':
        count+=1
print(count)