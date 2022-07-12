nums=[0,20,100,40]
max_num=nums[0]
second_num=nums[0]

for n in nums:
    if max_num<n:
        second_num=max_num
        max_num=n
    elif second_num<n and n<max_num:
        second_num=n
print(second_num)