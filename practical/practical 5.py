ist1 = input().split()
list2 = []
print(list1)

for i in list1 :
    userinp = int(i)
    if userinp % 2 == 0:
        list2.append(i)
        
print(list2)
