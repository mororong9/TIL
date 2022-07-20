print("enter the word")
word=input()
def remove(word):
    new=0
    for point in word:
        if 'a'==point:
            point=''
        new+=point
    return new

print(remove(word))
