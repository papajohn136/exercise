number = int(input("enter number: "))
max_sum = 0
max_m = 0
while number != 0:
    m = number
    s = 0
    while number>0:
        s += number%10
        number //= 10
    if s > max_sum:
        max_sum = s
        max_m = m
    number = int(input())
print('Number:',max_m,' has a maximum sum of digits: ', max_sum)