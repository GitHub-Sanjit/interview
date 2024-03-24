num = 1212
str1 = str(num)
reverse_str = str1[::-1]
reverse_num = int(reverse_str)
res = num == reverse_num
print(res)