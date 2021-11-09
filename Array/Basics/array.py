list =[]
n=int(input("enter the size of array"))

for i in range(0,n):
    num=int(input())
    list.append(num)
# print(list)
# #list.pop()
# print(list)
# #print(list.remove(1)) #this will remove the no. 1
#i=0
# while i < len(list):
#    print(list[i])
#    i+=1

# #sorting the array
# asc=list.sort()
# print(list) # by default ascending order
#
# #sortinf array in desending order
# desc=list.sort(reverse=True)
# print(list)
#
# print(list)

# arr=[len(list)]
# # x=list[0]
# # for i in list:
# #     if (list[i]<list[i+1]):
# #         arr.insert(list[i])
# #     else:
# #         continue
# #
# # print(arr)
# #


thistuple = ("apple",) #, make realise the python that it is tuple ()
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))