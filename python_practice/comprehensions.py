num = [1,2,3,4,5,6,7,8,9,10]

# my_list = []
# for n in num:
#     my_list.append(n)
#
# print(my_list)
#
# my_list = [n for n in num]
# print(my_list)

# my_list = map(lambda x: x*2, num)
# print(my_list)

l = [(n,m) for n in 'abc' for m in range(3)]
print(l)