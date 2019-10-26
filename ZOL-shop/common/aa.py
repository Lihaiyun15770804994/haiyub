str1 = 'asfjkahfkjahfkjahfhaj'
list1 =list(str1)
# res = list1.index('f')
# print(res)
# list1.remove('f')
# print(list1)
list2 = list(set(list1))

# for j in list2:
#     list1.count(j)
#     print(j,list1.count(j))
for j in list2:
    count = 0
    for i in list1:
        if i == j:
            count+=1
    print(j,count)
