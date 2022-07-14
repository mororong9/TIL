word='bananan'
is_a=False
for idx in range(len(word)):
    if word[idx]=='a':
        print(idx)
        is_a=True
        break
if is_a==False:
    print(-1)