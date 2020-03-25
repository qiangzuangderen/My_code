#字典推导式

main_text = "I'm in home,I'm in room,I'm in teatherroom"
check_count = {c:main_text.count(c) for c in main_text}
print(check_count)


#普通循环

check_count1 = {}
for c in main_text:
    check_count1[c] = main_text.count(c)
print(check_count1)

#生成器

gnt = (x**2 for x in range(8) if x**2 % 3 == 0)
print(tuple(gnt))
print(tuple(gnt))