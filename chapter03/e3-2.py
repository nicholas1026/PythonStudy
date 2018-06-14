invite_list=['xiyunfei','zhangwenyuan','xiyucheng']

print(invite_list)

print(invite_list[1]+"无法参加晚餐聚会")

new_person="fanbingbing"

invite_list[1]=new_person

print(invite_list)

invite_list.insert(0,"afei")
print(invite_list)

invite_list.insert(2,"yuanyuan")
print(invite_list)

invite_list.append("choubao")
print(invite_list)

f=invite_list.pop()
print(f)
s=invite_list.pop()
print(s)
t=invite_list.pop()
print(t)
fo=invite_list.pop()
print(fo)
print(invite_list)

del invite_list[0]
print(invite_list)
del invite_list[0]
print(invite_list)
